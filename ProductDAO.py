import mysql.connector
import dbconfig as cfg

class ProductDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getcursor()
        sql = "insert into productdata (Product, Manufacturer, Model, Price) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        new_id = cursor.lastrowid
        self.closeAll()
        return new_id

    def getAll(self):
        cursor = self.getcursor()
        sql = "select * from productdata"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql = "select * from productdata where ID = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        cursor = self.getcursor()
        sql = "update productdata set Product=%s, Manufacturer=%s, Model=%s, Price=%s  where ID = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql = "delete from productdata where ID = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("Deletion completed.")

    def convertToDictionary(self, result):
        colnames = ['ID', 'Product', 'Manufacturer', 'Model', 'Price']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

# Create an instance of ProductDAO and use its methods as needed
productDAO = ProductDAO()
