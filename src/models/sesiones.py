from dataclasses import dataclass
from src.service.db_connection import get_db_connection
@dataclass
class Sesiones:
    fecha: str
    duracion: str
    peso_pre : float
    peso_post : float
    utl:float
    id_paciente: int
    
    @classmethod
    def obtener_sesiones(cls, paciente_id):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                SELECT sesiones.id_sesion, sesiones.fecha, sesiones.hora, sesiones.estado,medicos.nombre,medicos.apellido
                FROM sesiones
                INNER JOIN medicos ON sesiones.id_medico = medicos.id_medico 
                WHERE id_paciente = %s;
            """
            cursor.execute(consulta,(paciente_id,))
            sesiones = cursor.fetchall()
            return sesiones
        except Exception as e:
            print(f"Error al obtener sesiones por paciente: {e}")
        finally:
            db.close()

