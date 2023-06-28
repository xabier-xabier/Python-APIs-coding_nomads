import sqlalchemy
from pprint import pprint


#engine = sqlalchemy.create_engine('mysql+pymysql://username:____________@localhost/mydatabase')
engine = sqlalchemy.create_engine('mysql+pymysql://root:___________@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
#actor = sqlalchemy.Table('actor', metadata,autoload=True, autoload_with=engine)
actor = sqlalchemy.Table('actor',metadata, autoload_with=engine)

#print(actor.columns.keys())
#print(repr(metadata.tables['actor']))

query=sqlalchemy.select((actor))
result_proxy=connection.execute(query)

result_set=result_proxy.fetchall()
pprint(result_set)