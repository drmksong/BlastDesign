# import PyRx as Rx
# import PyGe as Ge
# import PyGi as Gi
# import PyDb as Db
# import PyAp as Ap
# import PyEd as Ed
# from lib import *
import psycopg2 as pg
from pgconfig import config

def OnPyInitApp():
    print("\nOnPyRx PGCON Init")
    print("\ncommand = pgcon")

def test():
    PyRxCmd_pgcon()



def PyRxCmd_pgcon():
    con = None
    try:
        params = config()
        
        # conn = pg.connect(host="localhost", database="tbtest", user="postgres", password="postgres")
        
        print("Connecting to PostgreSQL database...")
        
        con = pg.connect(**params)
        crsr = con.cursor()
        print('PostgreSQL database version:')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
        print("Connection successful")
        # print(conn)
    except (Exception, pg.DatabaseError) as e:
        print("Connection failed")
        print(e)    
    finally:
        if con is not None:
            con.close()
            print("Connection closed")
        
if __name__ == "__main__":
    test()
