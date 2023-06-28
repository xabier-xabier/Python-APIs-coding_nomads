import sqlalchemy


#engine = sqlalchemy.create_engine('mysql+pymysql://username:_____________@localhost/mydatabase')
engine = sqlalchemy.create_engine('mysql+pymysql://root:____________@localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()
#actor = sqlalchemy.Table('actor', metadata,autoload=True, autoload_with=engine)
actor = sqlalchemy.Table('actor',metadata, autoload_with=engine)

print(actor.columns.keys())
#print(repr(metadata.tables['actor']))