import sqlalchemy
from pprint import pprint


#engine = sqlalchemy.create_engine('mysql+pymysql://username:password#@localhost/mydatabase')
engine = sqlalchemy.create_engine('mysql+pymysql://root:_________@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
#actor = sqlalchemy.Table('actor', metadata,autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film',metadata, autoload_with=engine)

#print(actor.columns.keys())
#print(repr(metadata.tables['actor']))

query = sqlalchemy.select((film)).where(sqlalchemy.and_(film.columns.length > 60, film.columns.rating == "PG"))
result_proxy=connection.execute(query)

result_set=result_proxy.fetchall()
pprint(result_set)