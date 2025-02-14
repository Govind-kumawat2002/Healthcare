from Healtcare.logger import logging
from Healtcare.exception import HealthcareException
from Healtcare.dpconfig import connect_to_mogodb , connect_to_mysql

def is_mongoconnected(mongo_connections):
    if mongo_connections is not None:
        print("connected ")
    else:
        print("not connected")
def is_mysqlconnected(mysql_connections):
    if mysql_connections is not None:
        print("connected")
    else:
        print("not connected ")