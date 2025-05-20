from dataclasses import dataclass
from src.service.db_connection import get_db_connection

@dataclass
class Cita:
    id: int
    fecha: str
    hora: str
    medico_id: int
    paciente_id: int

    
    
    
    
    @classmethod
    def obtener_citas_por_medico(cls,medico_id: int):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                
            SELECT citas.id_cita,pacientes.nombre,citas.fecha,citas.hora,citas.estado
	        FROM citas
	        INNER JOIN pacientes ON citas.id_paciente = pacientes.id_paciente WHERE id_medico = %s AND fecha = CURRENT_DATE;
            """
            cursor.execute(consulta,(medico_id,))
            citas = cursor.fetchall()
            return citas
        except Exception as e:
            print(f"Error al obtener citas por médico: {e}")
        finally:
            db.close()
            
            
    @classmethod
    def obtener_citas_pendientes(cls, medico_id):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                SELECT COUNT(*) 
                FROM citas
                WHERE id_medico = %s AND estado = 'PENDIENTE' AND fecha = CURRENT_DATE;
            """
            cursor.execute(consulta, (medico_id,))
            result = cursor.fetchone()
            return result[0] 
        except Exception as e:
            print(f"Error al obtener citas pendientes: {e}")
            return 0  
        finally:
            db.close()
    
            
    @classmethod
    def obtener_all_citas(cls):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                SELECT citas.id_cita,pacientes.nombre,citas.fecha,citas.hora,citas.estado
	            FROM citas
	            INNER JOIN pacientes ON citas.id_paciente = pacientes.id_paciente;
            """
            cursor.execute(consulta)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener citas pendientes: {e}")
            return 0  
        finally:
            db.close()
    
    @classmethod
    def aceptar_cita(cls, id_cita):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                UPDATE citas
                SET estado = 'ACEPTADO'
                WHERE id_cita = %s and estado = 'PENDIENTE' or estado = 'CANCELADO';
            """
            cursor.execute(consulta, (id_cita,))
            db.commit()
        except Exception as e:
            print(f"Error al aceptar la cita: {e}")
        finally:
            db.close()
            
    @classmethod
    def rechazar_cita(cls, id_cita):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                UPDATE citas
                SET estado = 'CANCELADO'
                WHERE id_cita = %s and estado = 'PENDIENTE' OR estado = 'ACEPTADO';
            """
            cursor.execute(consulta, (id_cita,))
            db.commit()
        except Exception as e:
            print(f"Error al rechazar la cita: {e}")
        finally:
            db.close()
            
    @classmethod
    def nueva_cita(cls, fecha, hora, id_medico, id_paciente):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                INSERT INTO citas (fecha, hora, id_paciente,id_medico)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(consulta, (fecha, hora, id_medico, id_paciente))
            db.commit()
        except Exception as e:
            print(f"Error al crear la cita: {e}")
        finally:
            db.close()
            
        