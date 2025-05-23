import mysql.connector
import pytest

from common.common.db import DBConnection
from services.events.config import DB_CONFIG


@pytest.fixture()
def hash_db():
	DB_CONFIG = DB_CONFIG
	connection = mysql.connector.connect(
		host=DB_CONFIG['DBHOST'],
		user=DB_CONFIG['DBUSER'],
		password=DB_CONFIG['DBPASSWORD'],
		database=DB_CONFIG['DBNAME'],
	)
	db_connection = DBConnection(DB_CONFIG)
	yield db_connection
	cursor = connection.cursor()
	delete_sql = F"DELETE FROM smartcare_providers"
	cursor.execute(delete_sql)
	connection.commit()
	connection.close()


def test_version(hash_db):
    assert True
    assert True
