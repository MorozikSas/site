import configparser
import psycopg2

configuration = configparser.ConfigParser()
configuration.read('config.ini')
config = configuration['database']

def getById(id):
    if id != 'NULL':
        try:
            connection = psycopg2.connect(
                dbname=config['dbname'],
                user=config['username'],
                host=config['host'],
                port=config['port']
            )

            cursor = connection.cursor()

            with connection.cursor() as cursor:
                cursor.execute("SELECT VERSION();")

                print(f"{cursor.fetchone()}")


        except Exception as e:
            print(f"pizda {e}")
        finally:
            if connection:
                connection.close()
    else:
        print("no id provided")
