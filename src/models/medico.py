from dataclasses import dataclass
from src.service.db_connection import get_db_connection

@dataclass
class Medico:
    id_medico: int
    nombre: str
    especialidad: str
    telefono: str
    direccion: str

    @staticmethod
    def buscar_paciente_id(paciente_id):
        try:
            db = get_db_connection()  # Tu función que devuelve la conexión
            db.connect()
            cursor = db.get_cursor()
            
            consulta = """ 
                SELECT id_paciente, nombre, sexo, fecha_nacimiento, tipo_sangre
                FROM pacientes 
                WHERE id_paciente = %s;
            """
            cursor.execute(consulta, (paciente_id,))
            paciente = cursor.fetchone()  
            return paciente  

        except Exception as e:
            print(f"Error al conectar a buscar paciente por ID: {e}")
            raise
        finally:
            db.close()
            
            
    @staticmethod
    def buscar_alergias(paciente_id):
        
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()
            consulta = """
                SELECT alergias.alergia
                FROM alergias
                JOIN pacientes ON alergias.id_paciente = pacientes.id_paciente
                WHERE pacientes.id_paciente = %s; 

            """
            cursor.execute(consulta,(paciente_id,))
            alergia = cursor.fetchall()
            return alergia
        
        except Exception as e:
            print(f"error al buscar la alergias del paciente: {e}")
        finally:
            db.close()
            
    @staticmethod
    def buscar_condiciones(paciente_id):
        
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()
            consulta = """
                SELECT condiciones.condicion
                FROM condiciones
                JOIN pacientes ON condiciones.id_paciente = pacientes.id_paciente
                WHERE pacientes.id_paciente = %s;

            """
            cursor.execute(consulta,(paciente_id,))
            condicion = cursor.fetchall()
            return condicion
        
        except Exception as e:
            print(f"error al buscar condiciones previas del paciente: {e}")
        finally:
            db.close()
            
    @staticmethod
    def buscar_citas(paciente_id):
        
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()
            consulta = """
                SELECT citas.id_cita, citas.fecha, citas.hora, citas.estado,citas.medico 
                FROM citas
                JOIN pacientes ON citas.id_paciente = pacientes.id_paciente
                WHERE pacientes.id_paciente = %s;
            """
            cursor.execute(consulta,(paciente_id,))
            cita = cursor.fetchall()
            return cita
        
        except Exception as e:
            print(f"error al buscar citas agendadas del paciente: {e}")
        finally:
            db.close()
        
    
        
    
    