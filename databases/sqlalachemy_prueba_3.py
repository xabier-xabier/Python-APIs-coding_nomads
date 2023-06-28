import sqlalchemy


engine = sqlalchemy.create_engine('mysql+pymysql://___________@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload_with=engine)

print(actor.columns.keys())
#print(repr(metadata.tables['actor']))