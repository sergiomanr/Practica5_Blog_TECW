import psycopg2

with psycopg2.connect(database = 'prueba',
                      user  = 'postgres',
                      password='12345',
                      host = 'localhost',
                      port = '5432') as conn :
    with conn.cursor() as cur:
        cur.execute(""" CREATE TABLE producto ( id serial PRIMARY KEY, nombre text, precio float) """)
        cur.execute( "INSERT INTO producto (nombre, precio) VALUES (%s, %s)", ('arroz',1.25))
        cur.execute("SELECT * FROM producto")
        cur.fetchone() 
        for record in cur:
            print(record)
        conn.commit()


def show_puertas_embarque(maximo):
    query = db.select(puertas_embarque)