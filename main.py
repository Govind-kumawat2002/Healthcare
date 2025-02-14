from Healtcare.logger import logging
from Healtcare.exception import HealthcareException
from Healtcare.dpconfig import connect_to_mogodb ,connect_to_mysql
from Healtcare.utils import is_mongoconnected 
from Healtcare.utils import is_mysqlconnected
# is_mysqlconnected(mysql_connections=connect_to_mysql)
# is_mongoconnected(mongo_connections=connect_to_mogodb)
# connect_to_mysql()
connect_to_mogodb(mogodb_string='mongodb+srv://jaikrishan2001:MuG5lYzwxJ0jMW5l@testing.w2n2r.mongodb.net/')

