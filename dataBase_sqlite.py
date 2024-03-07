import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect('C:\\sqlite\\db\\book.db')
    
    
    def populateTable(self):

        cursor = self.connection.cursor()      
        cursor.execute("SELECT rowId,* FROM booking")
        records = cursor.fetchall()
        return records
      

        