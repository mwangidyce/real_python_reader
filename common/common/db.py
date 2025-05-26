import datetime
import logging

import mysql.connector


class DBConnection:
	def __init__(self, db_config):
		self.logger = logging.getLogger(__name__)
		self.db_config = db_config
		self.connect = None
		self.dbConnect()

	def dbConnect(self):
		if not self.connect or not self.connect.is_connected():
			self.logger.info("DB: Connecting to DB")
			self.connect = mysql.connector.connect(
				host=self.db_config["DBHOST"],
				user=self.db_config["DBUSER"],
				password=self.db_config["DBPASSWORD"],
				database=self.db_config["DBNAME"],
			)
		return self.connect

	# --------------------------------------------
	# GET Records - Raw Query
	# --------------------------------------------
	def getRecordRawQuery(self, raw_sql):
		connection = self.dbConnect()
		cursor = connection.cursor(dictionary=True)

		try:
			self.logger.debug("\tExecuting statement: %s" % raw_sql)
			cursor.execute(raw_sql)
			records = cursor.fetchall()
			# connection.close()
			return records
		# TODO: write specific errors
		except Exception as e:
			self.logger.error("\tError at db.getRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % raw_sql)
			raise e

	# --------------------------------------------
	# GET Records
	# --------------------------------------------
	def getRecord(self, column, table, condition=None):
		connection = self.dbConnect()
		cursor = connection.cursor(dictionary=True)
		sql = f"SELECT {column} from {table}"
		if condition:
			sql += f" WHERE {condition}"

		try:
			self.logger.debug("\tExecuting statement: %s" % sql)
			cursor.execute(sql)
			records = cursor.fetchall()
			# connection.close()
			return records
		# TODO: write specific errors
		except Exception as e:
			self.logger.error("\tError at db.getRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % sql)
			raise e

	# --------------------------------------------
	# INSERT Records
	# --------------------------------------------
	def insertRecord(self, table, fields, string_format, values):
		connection = self.dbConnect()
		cursor = connection.cursor()
		sql = f"INSERT INTO {table} ({fields}) VALUES ({string_format})"
		self.logger.debug("\tExecuting statement: %s" % sql % values)
		try:
			cursor.execute(sql, values)
			record = cursor.lastrowid
			connection.commit()
			# connection.close()
			return record
		# TODO: write specific errors
		except Exception as e:
			self.logger.error("\tError at db.insertRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % sql)
			raise e

	# --------------------------------------------
	# UPSERT Records
	# --------------------------------------------
	def upsertRecord(self, table, fields, string_format, values):
		connection = self.dbConnect()
		cursor = connection.cursor()
		sql = f"REPLACE INTO {table} ({fields}) VALUES ({string_format})"
		self.logger.debug("\tExecuting statement: %s" % sql % values)
		try:
			cursor.execute(sql, values)
			record = cursor.lastrowid
			connection.commit()
			# connection.close()
			return record
		# TODO: write specific errors
		except Exception as e:
			self.logger.error("\tError at db.upsertRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % sql)
			raise e

	# --------------------------------------------
	# UPDATE Records
	# --------------------------------------------
	def updateRecord(self, table, field_values, condition):
		connection = self.dbConnect()
		cursor = connection.cursor()
		sql = f"UPDATE {table} SET {field_values} WHERE {condition}"
		self.logger.debug("\tExecuting statement: %s" % sql)
		try:
			cursor.execute(sql)
			record = cursor.lastrowid
			connection.commit()
			# connection.close()
			return record
		# TODO: write specific errors
		except Exception as e:
			self.logger.error("\tError at db.updateRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % sql)
			raise e

	# --------------------------------------------
	# DELETE Records
	# --------------------------------------------
	def deleteRecord(self, table, field_values, condition):
		connection = self.dbConnect()
		cursor = connection.cursor()
		sql = f"UPDATE {table} SET {field_values} WHERE {condition}"
		self.logger.debug("\tExecuting statement: %s" % sql)
		try:
			cursor.execute(sql)
			record = cursor.lastrowid
			connection.commit()
			# connection.close()
			return record
		# TODO: write specific errors
		except mysql.connector.errors.ProgrammingError as e:
			self.logger.error("\tError at db.deleteRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % sql)
			raise e
		except Exception as e:
			self.logger.error("\tError at db.deleteRecord: %s: %s, args of %s" % (type(e).__name__, e.args, e))
			self.logger.error("\tAttempted to run the SQL statement: %s" % sql)
			raise e
