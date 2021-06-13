import pymysql
from sqlalchemy import create_engine, Table, Column, select, MetaData

engine = create_engine('mysql+pymysql://asterisk:asterisk@192.168.0.106:3306/asterisk')

# Print the table names
print(engine.table_names())

metadata = MetaData()
auths = Table('ps_auths'
, metadata, autoload=True,
autoload_with=engine)
print(repr(auths))