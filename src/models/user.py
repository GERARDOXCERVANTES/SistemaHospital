from dataclasses import dataclass
from service.database import Database

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str

    @staticmethod # LEE LA INFORMACION DE LA TABLA USERS
    def get_all(db: Database) : #recibe la instancia de la base de datos
        with db.cursor() as cursor: #cursor es el objeto que se encarga de ejecutar las consultas a la base de datos
            cursor.execute("SELECT * FROM users")#
            return [User(**row) for row in cursor.fetchall()]

    @staticmethod # LEE LA INFORMACION DE LA TABLA USERS
    def get_by_id(db: Database, id: int): #recibe la instancia de la base de datos y el id del usuario
        with db.cursor() as cursor: #cursor es el objeto que se encarga de ejecutar las consultas a la base de datos
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))# ejecuta la consulta y recibe el id del usuario
            return User(**cursor.fetchone())    
