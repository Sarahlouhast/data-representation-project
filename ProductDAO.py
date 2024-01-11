# Import mysql for database connection and config file for access
import mysql.connector
import dbconfig as cfg

class ProductDAO:
    #  Class variables to store connection details
    connection = None
    cursor = None
    host = ''
    user = ''
    password = ''
    database = ''

    # Initialize connection details from imported from configuration file
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        # Attempt to establish a connection and create a cursor
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
            # Print on successful connection
            print("Connection @ init made with ProductDAO.py")            
        except mysql.connector.Error as err:
            # Print an error message if connection fails
            print(f"Error: {err}")
    
    # Method to get a cursor, creates a new connection if not present or not connected
    def getcursor(self): 
        if not self.connection or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
        return self.cursor

    # Method to close both connection and cursor
    def closeAll(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
        if self.cursor:
            self.cursor.close()

    # Method to insert a new record into the productdata table
    def create(self, values):
        cursor = self.getcursor()
        # SQL query to insert a new record into the productdata table
        sql = "INSERT INTO productdata (Product, Manufacturer, Model, Price) VALUES (%s, %s, %s, %s)"
        # Execute the SQL query with values provided 
        cursor.execute(sql, (values['Product'], values['Manufacturer'], values['Model'], values['Price']))
        # Commit changes
        self.connection.commit()
        new_id = cursor.lastrowid
        self.closeAll()
        return new_id

    # Method to retrieve all records from the productdata table
    def getAll(self):
        cursor = self.getcursor()
        sql = "select * from productdata"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            # Convert each result to a dictionary and append to the returnArray
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        return returnArray

    # Method to retrieve a record by ID from the productdata table
    def findByID(self, id):
        cursor = self.getcursor()
        sql = "select * from productdata where ID = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    # Method to update a record in the productdata table
    def update(self, values):
        cursor = self.getcursor()
        # SQL query to insert a new record into the productdata table
        sql = "UPDATE productdata SET Product=%s, Manufacturer=%s, Model=%s, Price=%s WHERE ID = %s"
        # Execute the SQL query with values provided 
        cursor.execute(sql, (values['Product'], values['Manufacturer'], values['Model'], values['Price'], values['ID']))  
        # Commit changes
        self.connection.commit()
        self.closeAll()

    # Method to delete a record from the productdata table    
    def delete(self, id):
        cursor = self.getcursor()
        sql = "delete from productdata where ID = %s"
        values = (id,)

        cursor.execute(sql, values)
        # Commit changes
        self.connection.commit()
        self.closeAll()
        
        print("Deletion completed.")

    # Method to convert a result tuple to a dictionary
    def convertToDictionary(self, result):
        colnames = ['ID', 'Product', 'Manufacturer', 'Model', 'Price']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

