import psycopg
from dataclasses import dataclass

@dataclass
class Database:
    host: str
    dbname: str
    user: str
    password: str
    port: int = 5432
    conn: psycopg.Connection = None

    
    @property
    def connection_params(self):
        return {
            "host": self.host,
            "dbname": self.dbname,
            "user": self.user,
            "password": self.password,
            "port": self.port,
        }
        
        
    def connect(self):
        try:
            if self.conn is None or self.conn.closed:
                    self.conn = psycopg.connect(**self.connection_params)
            return self.conn
        except psycopg.OperationalError as e:
                print(f"Error al conectar a la base de datos: {e}")
        raise
    
    def get_cursor(self):#retorna el cursor de la conexion de la db
        try:
            return self.connect().cursor()
        except psycopg.OperationalError as e:
            print(f"Error al obtener cursor: {e}")
            raise
    
    def close(self):
        try:
            if self.conn and not self.conn.closed:
                self.conn.close()
        except psycopg.OperationalError as e:
            print(f"Error al cerrar la conexión: {e}")