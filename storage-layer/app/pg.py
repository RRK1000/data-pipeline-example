import psycopg2
from app.models import Subscription

conn = None
dbName = "postgres"
def get_db_conn():
    global conn, dbName

    if not conn:
        conn = psycopg2.connect(
            database=dbName,
            user="postgres",
            password="password",
            host="postgres",
            port="5432",
        )

        conn.autocommit = True
    return conn


def setup_db():
    global dbName

    conn = get_db_conn()
    cursor = conn.cursor()
    sqlCreateDatabase = "create database " + dbName + ";"
    cursor.execute(sqlCreateDatabase)

    tableName = "subscriptions"
    sqlCreateTable = "create table " + dbName + "." + tableName
    +" (username VARCHAR(255) PRIMARY_KEY), payment_method VARCHAR(255), plan VARCHAR(255), status VARCHAR(255), term VARCHAR(255)"
    cursor.execute(sqlCreateTable)


def upsert_subscription(sub: Subscription):
    conn = get_db_conn()
    cursor = conn.cursor()
    sql = """INSERT INTO subscriptions(username,payment_method,plan,status,term)
             VALUES(%s, %s, %s, %s, %s) ON CONFLICT (username) DO UPDATE SET payment_method = %s, plan = %s, status = %s, term = %s"""
    cursor.execute(sql, (sub.username, sub.payment_method, sub.plan, sub.status, sub.term, sub.payment_method, sub.plan, sub.status, sub.term))
    conn.commit()
    cursor.close()
