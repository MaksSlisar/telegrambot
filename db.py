import re

import mysql.connector
from mysql.connector import IntegrityError


def read():
    cnx = mysql.connector.connect(user='tfbs5ukkslz22vzy', password='aptludv1rylm9qq3',
                                  host='durvbryvdw2sjcm5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                  database='h3xsjq73ve0t68m0')

    cursor = cnx.cursor()
    cursor.execute("select link from links")
    records = cursor.fetchall()

    cnx.close()

    return records

def insert(link):
    cnx = mysql.connector.connect(user='tfbs5ukkslz22vzy', password='aptludv1rylm9qq3',
                                  host='durvbryvdw2sjcm5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                  database='h3xsjq73ve0t68m0')



    mySql_insert_query = "insert into links(link) VALUES('"+link+"')"

    cursor = cnx.cursor()
    cursor.execute(mySql_insert_query)
    cnx.commit()
    cnx.close()

def insertUserId(id, name):
    cnx = mysql.connector.connect(user='tfbs5ukkslz22vzy', password='aptludv1rylm9qq3',
                                  host='durvbryvdw2sjcm5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                  database='h3xsjq73ve0t68m0')

    mySql_insert_query = "insert into uid(id, name) VALUES('" + str(id) + "','" + name + "')"

    try:

        cursor = cnx.cursor()
        cursor.execute(mySql_insert_query)
    except IntegrityError:
        pass
    cnx.commit()
    cnx.close()
def readUsers():
    cnx = mysql.connector.connect(user='tfbs5ukkslz22vzy', password='aptludv1rylm9qq3',
                                  host='durvbryvdw2sjcm5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                  database='h3xsjq73ve0t68m0')

    mySql_insert_query = "select * from uid"

    cursor = cnx.cursor()
    cursor.execute(mySql_insert_query)
    records = cursor.fetchall()

    cnx.close()

    return records
