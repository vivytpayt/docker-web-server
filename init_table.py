import time
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData, INT, BIGINT, FLOAT, TEXT
from config import DATABASE, TABLE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def create_tables(engine):
    meta = MetaData()
    table = Table(
        TABLE, meta,
        Column('id', INT),
        Column('title', TEXT),
        Column('description', TEXT),
        Column('price', BIGINT),
        Column('discountpercentage', FLOAT),
        Column('rating', FLOAT),
        Column('stock', INT),
        Column('brand', TEXT),
        Column('category', TEXT),
        Column('thumbnail', TEXT),
        Column('images', TEXT)
    )
    meta.create_all(engine)


def connect__to_db():
    dsn = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/' \
          f'{DATABASE}'
    engine = create_engine(dsn)

    with engine.connect():
        create_tables(engine)


if __name__ == '__main__':
    time.sleep(5)
    connect__to_db()
