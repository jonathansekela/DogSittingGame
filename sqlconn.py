#!/usr/bin/env python
import mysql.connector as conn

class SqlConn():
	def __init__(self, host, user, password):
		self.db = conn.connect(
			#@todo: get rid of this and pass it in instead
			host="localhost",
			user="root",
			password="Thug4Lyfe"
		)
		self.cursor = self.db.cursor()

	#qry: the sql query string
	#val: array of value tuples to insert
	def insert(self, qry, val):
		#@todo: get rid of example queries
		qry = "INSERT INTO customers (name, address) VALUES (%s, %s)"
		val = [
			('Peter', 'Lowstreet 4'),
			('Amy', 'Apple st 652'),
			('Hannah', 'Mountain 21'),
			('Michael', 'Valley 345'),
			('Sandy', 'Ocean blvd 2'),
			('Betty', 'Green Grass 1'),
			('Richard', 'Sky st 331'),
			('Susan', 'One way 98'),
			('Vicky', 'Yellow Garden 2'),
			('Ben', 'Park Lane 38'),
			('William', 'Central st 954'),
			('Chuck', 'Main Road 989'),
			('Viola', 'Sideway 1633')
		]
		self.cursor.executemany(qry, val)

		self.db.commit()

		print(self.cursor.rowcount, "record(s) inserted")

	#qry: the sql query string
	def select(self, qry):
		self.cursor.execute(qry)
		myresult = self.cursor.fetchall()

		for x in myresult:
			print(x)

	#qry: the sql query string
	def update(self, qry):
		self.cursor.execute(qry)
		self.db.commit()

		print(self.db.rowcount, "record(s) affected")