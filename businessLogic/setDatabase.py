import databaseModel
import time
import datetime

connection = databaseModel.connect()

def setMainTables():    
    databaseModel.create_tables(connection)


setMainTables()

