import psycopg2
from config import config

def create_tables():
    sql = """   CREATE TABLE log (
                id              SERIAL PRIMARY KEY,
                logtext         VARCHAR(255)
                );

                CREATE TABLE gender (
                id              SERIAL PRIMARY KEY,
                description     VARCHAR(5)
                );

                CREATE TABLE nationality (
                id              SERIAL PRIMARY KEY,
                name            VARCHAR(5)
                );
    
                CREATE TABLE users (
                id              SERIAL PRIMARY KEY,
                name            VARCHAR(255),
                age             INTEGER,
                password        VARCHAR(255),
                genderId        INTEGER,
                preferenceId    INTEGER,
                nationalityId   INTEGER,
                CONSTRAINT gender_fk FOREIGN KEY (genderId) REFERENCES gender (id),
                CONSTRAINT preference_fk FOREIGN KEY (preferenceId) REFERENCES gender (id),
                CONSTRAINT nationality_fk FOREIGN KEY (nationalityId) REFERENCES nationality (id)
                );

                CREATE TABLE matches (
                id              SERIAL PRIMARY KEY,
                user1Id         INTEGER,
                user2Id         INTEGER,
                CONSTRAINT user1_fk FOREIGN KEY (user1Id) REFERENCES users (id),
                CONSTRAINT user2_fk FOREIGN KEY (user2Id) REFERENCES users (id)
                );  
        """

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')



if __name__ == '__main__':
    create_tables()