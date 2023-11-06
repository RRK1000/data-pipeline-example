import psycopg2
import models

conn = None
def get_db_conn():
    global conn
    if not conn:
        conn = psycopg2.connect(
            database="data-pipeline-example",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port="5432",
        )

        conn.autocommit = True
    return conn


def setup_db():
    conn = get_db_conn()
    cursor = conn.cursor()
    dbName = "data-pipeline-example"
    sqlCreateDatabase = "create database " + dbName + ";"
    cursor.execute(sqlCreateDatabase)

    tableName = "subscriptions"
    sqlCreateTable = "create table " + dbName + "." + tableName
    +" (username VARCHAR(255) PRIMARY_KEY), payment_method VARCHAR(255), plan VARCHAR(255), status VARCHAR(255), term VARCHAR(255)"
    cursor.execute(sqlCreateTable)


def upsert_subscription(sub: models.Subscription):
    conn = get_db_conn()
    cursor = conn.cursor()
    sql = """INSERT INTO subscriptions(username,payment_method,plan,status,term)
             VALUES(%s, %s, %s, %s, %s) ON CONFLICT (username) DO UPDATE SET payment_method = %s, plan = %s, status = %s, term = %s"""
    cursor.execute(sql, (sub.username, sub.payment_method, sub.plan, sub.status, sub.term, sub.payment_method, sub.plan, sub.status, sub.term))
    conn.commit()
    cursor.close()
