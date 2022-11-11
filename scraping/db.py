import psycopg2,os
import scraping_scr
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(database="scrap", user = "postgres", password = "1",host='127.0.0.1', port= '5432')
		
        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('''CREATE TABLE EMPLOYEE(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT
            )''')
        print('running>>>>>>>>>>>>>>>',os.environ)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error: >>>>>>>>>>>>>>',error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()