from dataclasses import dataclass
from service.database import Database

@dataclass
class Cita:
    id: int
    fecha: str
    hora: str
    medico_id: int
    paciente_id: int

    @staticmethod
    def get_all(db: Database):#devuelve todas las citas
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM citas")
            return [Cita(**row) for row in cursor.fetchall()]

    @staticmethod
    def get_by_id(db: Database, id: int):#devuelve la informacion de la cita por el id
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM citas WHERE id = %s", (id,))
            return Cita(**cursor.fetchone())
        
