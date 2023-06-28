import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:_____________@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('table_xabi',metadata , autoload_with=engine)

query = sqlalchemy.update(newTable).values(surname="roberto").where(newTable.columns.Id == 1)

result = connection.execute(query)
result_proxy1=connection.commit()   # need to commit to send the data to database
pprint(newTable)