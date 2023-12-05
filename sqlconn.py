#!/usr/bin/env python
import mysql.connector as conn
from datetime import datetime
import dog #for Directions and Actions enums

class SqlConn():

#region constructors
	def __init__(self, host, user, password, database):
		self.db = conn.connect(
			# @todo: get rid of this and pass it in instead
			host="localhost",
			user="root",
			password="Thug4Lyfe",
			database="testdb"
		)
		self.cursor = self.db.cursor()
#endregion

#region public functions
	#@todo: implement function logic
	def new_player_login(self, user_id, access_time):
		print("new player detected, inserting into db...")
		qry = ""
		val = [()]
		self.__insert(qry, val)

	#@todo: implement function logic
	def new_player_demographics(self, user_id, age, eth_id, gender, game_familiarity, dog_familiarity):
		print("new player demographics detected, inserting into db...")
		qry = ""
		val = [()]
		self.__insert(qry, val)

	#@todo: test function
	#@todo: translate datetime.now() into mysql datetime format
	def animation_change(self, user_id, new_animation):
		print("animation change detected. Inserting into db...")
		qry = "INSERT INTO game_data (user_id, user_input, animation, input_is_correct, time_to_input_ms) VALUES (%s, 2, %s, 0, %s)" #2 is 'None' input
		val = [(user_id, new_animation, datetime.now())]
		self.__insert(qry, val)

	#@todo: test function
	#@todo: translate datetime.now() into mysql datetime format
	def user_input(self, user_id, user_input, current_animation, input_is_correct):
		print("user input detected. Inserting into db..")
		qry = "INSERT INTO game_data (user_id, user_input, animation, input_is_correct, time_to_input_ms) VALUES (%s, %s, %s, %s, %s)"
		val = [(user_id, user_input, current_animation, input_is_correct, datetime.now())]
		self.__insert(qry, val)
#endregion

#region private functions

	# qry: the sql query string
	# val: array of value tuples to insert
	def __insert(self, qry, val):
		# @todo: get rid of example queries
		self.cursor.executemany(qry, val)
		self.db.commit()
		print(self.cursor.rowcount, "record(s) inserted")

	# qry: the sql query string
	def __select(self, qry):
		self.cursor.execute(qry)
		result = self.cursor.fetchall()

		for x in result:
			print(x)

	# qry: the sql query string
	def __update(self, qry):
		self.cursor.execute(qry)
		self.db.commit()
		print(self.db.rowcount, "record(s) affected")
#endregion