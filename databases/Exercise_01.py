'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:___________@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload_with=engine)

query = sqlalchemy.select((film))
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

category=sqlalchemy.Table("category", metadata, autoload_with=engine)

query1=sqlalchemy.select((category))
result_p=connection.execute(query1)

res=result_p.fetchall()
pprint(res)