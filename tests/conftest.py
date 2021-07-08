
def pytest_addoption(parser):
    parser.addoption("--dbecho", action='store_true')
    parser.addoption("--nopattern", action='store_true')