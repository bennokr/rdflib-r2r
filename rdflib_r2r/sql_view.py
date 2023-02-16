import logging

import sqlparse

from sqlalchemy import literal_column, literal
from sqlalchemy import func as sqlfunc
import sqlalchemy.sql.expression as sqlexpr


# TODO: Just replace this by https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.TextClause.columns !!!

def view2obj(sqlquery):
    Sym = sqlparse.tokens.String.Symbol
    Keyw = sqlparse.tokens.Keyword
    Punct = sqlparse.tokens.Punctuation
    Op = sqlparse.tokens.Token.Operator
    Wild = sqlparse.tokens.Token.Wildcard
    Str = sqlparse.tokens.Token.Literal.String.Single

    def no_whitespace(toks):
        return [l for l in toks if not l.is_whitespace]
            
    def parse_node(ls, from_table):
        if isinstance(ls, sqlparse.sql.Operation):
            ls = no_whitespace(ls)
            # for l in ls:
            #     logging.warn(f"OPERATION PART {l} {type(l)} {l.ttype}")
            if (len(ls) == 3) and (ls[1].ttype == Op):
                a, b = parse_node(ls[0], from_table), parse_node(ls[-1], from_table)
                if (ls[1].normalized == '||'):
                    return a + b
                if (ls[1].normalized in ['==', '=']):
                    return a == b
            
        elif isinstance(ls, sqlparse.sql.Case):
            value = None
            else_ = None
            whens = []
            for cond, val in ls.get_cases():
                cond, val = no_whitespace(cond), no_whitespace(val)
                if not val:
                    value = parse_id(cond[0], from_table)
                elif str(cond[0]) == 'ELSE':
                    else_ = literal(str(cond[1]))
                else:
                    a = parse_node(cond[1], from_table)
                    b = parse_node(val[1], from_table)
                    whens.append((a,b))
            logging.warn(whens)
            if value is not None:
                return sqlexpr.case(dict(whens), value=value, else_=else_)
            else:
                return sqlexpr.case(*whens, else_=else_)

        elif (ls.ttype == Str):
            return literal(str(ls).strip("'"))
            
        elif isinstance(ls, sqlparse.sql.Identifier):
            return parse_id(ls, from_table)
                
        raise Exception(f"Invalid SQL node {ls}")


    def parse_id(identifier, from_table):
        ls = no_whitespace(identifier)
        label = None
        if (len(ls) > 2) and (ls[-2].ttype == Keyw) and (ls[-2].normalized == 'AS'):
            label, ls = str(ls[-1]), ls[:-2]
            
        op = None
        ttypes = tuple(l.ttype for l in ls)
        if (ttypes == (Sym,)):
            # TODO get from from_table
            op = literal_column(str(ls[0]).strip('"'))
        elif (ttypes == (Sym, Punct, Sym)):
            # TODO get from specified table
            label = str(ls[-1]).strip('"')
            op = literal_column(''.join(str(l) for l in ls)).label(label)
        elif (ttypes == (Sym, Punct, Wild)):
            # TODO get all columns from specified table
            op = literal_column(''.join(str(l) for l in ls))
        elif isinstance(ls[0], sqlparse.sql.Parenthesis):
            op = next(parse_node(l, from_table) for l in ls[0] if not l.ttype == Punct)
        elif isinstance(ls[0], sqlparse.sql.Function):
            op = parse_id(ls[0], from_table)
        elif isinstance(ls[0], sqlparse.sql.Identifier) and ls[0].normalized == 'COUNT':
            op = sqlfunc.count(parse_id(ls[1:], from_table))
            
        if (op is not None):
            if label:
                op = op.label(label.strip('"'))
            ostr = op.compile(compile_kwargs={"literal_binds": True})
            logging.warn(f"{ostr} LABEL: {label}")
            return op
            
        raise Exception(f"Problem with SQL Identifier {ls}")

    for stmt in sqlparse.parse(sqlquery):
        logging.warn('\n'+sqlquery)
        toks = no_whitespace(stmt.tokens)
        selecttok, select_ids, fromtok, from_table, *rest = toks
        assert selecttok.normalized == 'SELECT'
        assert fromtok.normalized == 'FROM'
        logging.warn(from_table)
        for s in select_ids.get_identifiers():
            ex = parse_id(s, from_table)
            logging.warn((str(s), type(s), ex, ex.key, ex.type ))
            yield ex
