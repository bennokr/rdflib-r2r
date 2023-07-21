import logging

from sqlalchemy import create_engine


def setup_engine(name, echo=False, creator=None):
    if name == "sqlite":
        import sqlite3

        sqlite3.register_adapter(bool, int)
        sqlite3.register_converter("BOOLEAN", lambda v: bool(int(v)))

        return create_engine(
            "sqlite:///:memory:",
            echo=echo,
            future=True,
            connect_args={
                "detect_types": sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
                'timeout': 30 * 1000
            },
            # native_datetime=False, # breaks rdb2rdf test D016
            native_datetime=True, # breaks BSBM test 3
            creator = creator,
        )

    if name == "duckdb":
        db = create_engine(
            "duckdb:///:memory:",
            echo=echo,
            # future=True,
            connect_args={"read_only": False},
        )
        db.dialect.server_version_info = (0,)
        return db


def create_database(db, path, *sql_fnames):
    for sql_fname in sql_fnames:
        sql_script = path.joinpath(sql_fname).open().read()
        conn = db.raw_connection()
        try:
            if hasattr(conn.connection, "c"):
                cursor = conn.connection.c
            else:
                cursor = conn.cursor()
            cursor.execute(sql_script, (), None)
        except Exception as e:
            try:
                cursor = conn.cursor()
                cursor.executescript(sql_script)
            except Exception as e:
                raise Exception(f"Problem with {path}: {e}")
            finally:
                conn.close()
        finally:
            conn.close()
