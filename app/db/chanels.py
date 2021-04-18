from sqlalchemy import sql,Table, Column, Integer, String, Boolean
from .base import metadata

chanels = Table('chanels',
                metadata,
                Column('id', Integer, primary_key=True, autoincrement=True, unique=True),
                Column('title', String(256)),
                Column('icon', String(256)),
                Column('disabled', Boolean, server_default=sql.expression.false())
                )
