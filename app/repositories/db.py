import os

import psycopg

_db_url = os.environ["DATABASE_URL"]


def connect():
    return psycopg.connect(_db_url)


def format_placeholders(statement, column_names):
    def by_type(bind_type, names):
        return psycopg.sql.SQL(", ").join(map(bind_type, names))

    return psycopg.sql.SQL(statement).format(
        by_type(psycopg.sql.Identifier, column_names),
        by_type(psycopg.sql.Placeholder, column_names),
    )
