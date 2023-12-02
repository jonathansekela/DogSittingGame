#!/usr/bin/env python
import mysql.connector as conn
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

	#@todo: implement function logic
	def animation_change(self, user_id, new_animation):
		print("animation change detected. Inserting into db...")
		qry = "INSERT INTO game_data (user_id, user_input, animation, input_is_correct, time_to_input_ms) VALUES (%s, [INPUT], %s, [INPUT_CORRECT], [INPUT_TIME])"
		val = [()]
		self.__insert(qry, val)
		

	#@todo: implement function logic
	def user_input(self, user_id, user_input, current_animation):
		print("user input detected. Inserting into db..")
		qry = ""
		val = [()]
		self.__insert(qry, val)
#endregion

#region private functions

	# qry: the sql query string
	# val: array of value tuples to insert
	def __insert(self, qry, val):
		# @todo: get rid of example queries
		# qry = "INSERT INTO test_deez (id, describe_deez) VALUES (%s, %s)"
		# val = [(1, "my name jeff"), (2, "my name also jeff")]
		self.cursor.executemany(qry, val)

		self.db.commit()

		print(self.cursor.rowcount, "record(s) inserted")

	# qry: the sql query string
	def __select(self, qry):
		self.cursor.execute(qry)
		myresult = self.cursor.fetchall()

		for x in myresult:
			print(x)

	# qry: the sql query string
	def __update(self, qry):
		self.cursor.execute(qry)
		self.db.commit()

		print(self.db.rowcount, "record(s) affected")
#endregion