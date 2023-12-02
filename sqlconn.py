#!/usr/bin/env python
import mysql.connector as conn


class SqlConn():
    def __init__(self, host, user, password, database):
        self.db = conn.connect(
            # @todo: get rid of this and pass it in instead
            host="localhost",
            user="root",
            password="Thug4Lyfe",
            database="testdb"
        )
        self.cursor = self.db.cursor()

	#@todo: make one function per static event possible within the game.

    # qry: the sql query string
    # val: array of value tuples to insert
    def insert(self, qry, val):
        # @todo: get rid of example queries
        qry = "INSERT INTO test_deez (id, describe_deez) VALUES (%s, %s)"
        val = [(1, "my name jeff"), (2, "my name also jeff")]
        self.cursor.executemany(qry, val)

        self.db.commit()

        print(self.cursor.rowcount, "record(s) inserted")

    # qry: the sql query string
    def select(self, qry):
        self.cursor.execute(qry)
        myresult = self.cursor.fetchall()

        for x in myresult:
            print(x)

    # qry: the sql query string
    def update(self, qry):
        self.cursor.execute(qry)
        self.db.commit()

        print(self.db.rowcount, "record(s) affected")
