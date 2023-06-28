import sqlalchemy
from pprint import pprint


engine = sqlalchemy.create_engine('mysql+pymysql://root:____________@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload_with=engine)

query = sqlalchemy.insert(newTable).values(Id=1, name='Software Ninjaneer', salary=60000.00, active=True)
result_proxy = connection.execute(query)
result_proxy1=connection.commit()      # need to commit the data to the database

#new_records = [{'Id':'2', 'name':'record1', 'salary':80000, 'active':False},
               #{'Id':'3', 'name':'record2', 'salary':70000, 'active':True}]
#result_proxy = connection.execute(query,new_records)


# I can`t insert the data in the table, no error but no data, i have issues with autoload=True.`

pprint(newTable)
