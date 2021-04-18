from sqlalchemy import Table, Column, Integer, String, Text, DateTime, BigInteger
from .base import metadata

shows = Table('shows',
              metadata,
              Column('id', BigInteger, primary_key=True),
              Column('title', String(256)),
              Column('description', Text),
              Column('start_t', DateTime),
              Column('end_t', DateTime),
              Column('chanel_id', Integer)
              )
