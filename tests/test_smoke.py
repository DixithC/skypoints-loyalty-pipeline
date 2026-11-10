import duckdb

import skypoints


def test_package_imports():
    assert skypoints.__version__


def test_duckdb_is_available():
    con = duckdb.connect()  # in-memory database
    assert con.execute("SELECT 42").fetchone() == (42,)