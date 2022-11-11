import scraping_scr
from config import config
import psycopg2,os

conn = None
try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    for v in os.environ:
        print(v)
        cur.execute(f"INSERT INTO movie_data(id,movie_name,release_date) values(%s, %s, %s);",v)
    cur.close()
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
