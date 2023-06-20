import sqlite3
from datetime import datetime


def create_connection():
    db_file: str = "/home/shey/Desktop/PhishFinder/database/PhishFinder.db"
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except ConnectionError as e:
        print(e)
    return connection


def execute_query(query):
    connection = create_connection()
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    element = cur.fetchall()
    cur.close()
    connection.close()
    if len(element) > 0:
        return element


def set_domain(sus_domain):
    domain = f"'{sus_domain}'"
    set_domain_query = f'INSERT INTO SuspiciousDomain (Domain) VALUES ({domain});'
    execute_query(set_domain_query)


def set_time(sus_domain):
    domain = f"'{sus_domain}'"
    time = datetime.now()
    current_time = f"'{time}'"
    set_time_query = f'UPDATE SuspiciousDomain SET Time = {current_time} WHERE Domain = {domain};'
    execute_query(set_time_query)


def set_statuscode(sus_domain, status_code):
    domain = f"'{sus_domain}'"
    status = f"'{status_code}'"
    set_statuscode_query = f'UPDATE SuspiciousDomain SET StatusCode = {status} WHERE Domain = {domain};'
    execute_query(set_statuscode_query)


def mobile_app_exist(sus_domain, existence):
    domain = f"'{sus_domain}'"
    exist = f"'{existence}'"
    mobile_app_exist_query = f'UPDATE SuspiciousDomain SET MobileApp = {exist} WHERE Domain = {domain};'
    execute_query(mobile_app_exist_query)


def domain_existence(sus_domain):
    domain = f"'{sus_domain}'"
    domain_existence_query = f'SELECT COUNT(1) FROM SuspiciousDomain WHERE Domain = {domain};'
    element = execute_query(domain_existence_query)
    if element[0][0] > 0:
        return True
    else:
        return False


def set_application(sus_domain, application):
    domain = f"'{sus_domain}'"
    app = f"'{application}'"
    set_application_query = f'INSERT INTO Applications (susDomain, applicationLink) VALUES ({domain}, {app});'
    execute_query(set_application_query)


