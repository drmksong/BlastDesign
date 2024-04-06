import psycopg2 as pg
from configparser import ConfigParser

def config(fname='pg.ini', section='postgresql')->dict:
    parser = ConfigParser()
    parser.read(fname)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {fname} file')
    return db

if __name__ == "__main__":
    db = config()
    print(db)
    con = None
    try:
        # params = config()
        params = db
        print("Connecting to PostgreSQL database...")
        con = pg.connect(**params)
        crsr = con.cursor()
        print('PostgreSQL database version:')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
        print("Connection successful")
    except (Exception, pg.DatabaseError) as e:
        print("Connection failed")
        print(e)

