import psycopg2
import psycopg2.extras as ext
def run_sql(sql, values = None):
    conn = None
    results = []
    # Change the name of db in any proyect.
    try:
        conn=psycopg2.connect("dbname='authors_and_books'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results