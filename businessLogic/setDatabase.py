import databaseModel
import time
import datetime

connection = databaseModel.connect()

def setMainTables():    
    databaseModel.create_tables(connection)


# setMainTables()

# dateCreate = datetime.date.today()
# dateUpdate = dateCreate
# # title = "Заголовок 1"
# # body = "Тело 1"
# # databaseModel.add_note(connection, title, dateCreate, dateUpdate, body)

# title2 = "Очень длинный заголовок прям очень длиииииииный"
# body2 = "Тело 2"
# databaseModel.add_note(connection, title2, dateCreate, dateUpdate, body2)


# allNotes = databaseModel.get_all_notes(connection)
# [print(n) for n in allNotes]

# find = databaseModel.get_all_notesByText(connection, "%Нормальный%", "%Нормальный%")
# print(find)

# cellDict = {'Text': 'text', 'Date': 'date', 'Color': 'color'}
# print(cellDict['Date'])

data = [[]] + [['', '', '', '', '', ''] for n in range(0, 25%3)]
# print(data)


columns    = ["NUMBER", "CardView1", "CardVie2"]
columnNumber = 8
columnNow    = 3 - 1
addColumns   = columnNumber - columnNow
if addColumns > 0:
    addList = ['New Column' for n in range(0, addColumns)]
    columns = columns + addList

print(f"Columns now: {columnNow}, Columns we want: {columnNumber}, ColumnsAdd: {addColumns}")    
print(f"AddList: {len(addList)}") 
print(f"Columns after add: {columns}")