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
    def contar_m(cls):
        try:
            db = get_db_connection()  # Tu función que devuelve la conexión
            db.connect()
            cursor = db.get_cursor()
            
            consulta = """ 
                SELECT COUNT(*)
                FROM medicos;
            """
            cursor.execute(consulta)
            db.commit()
            paciente = cursor.fetchone()  
            return paciente[0]  

        except Exception as e:
            print(f"Error : {e}")
            raise
        finally:
            db.close()
            
        
    
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
                SELECT citas.id_cita, citas.fecha, citas.hora, citas.estado 
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
        
    @staticmethod
    def buscar_sesiones(paciente_id):
            
            try:
                db = get_db_connection()
                db.connect()
                cursor = db.get_cursor()
                consulta = """
                    SELECT sesiones.fecha,sesiones.duracion,sesiones.peso_pre,sesiones.peso_post,utl_t 
                        FROM sesiones
                        JOIN pacientes ON sesiones.id_paciente  = pacientes.id_paciente
                        WHERE pacientes.id_paciente = %s; 
                """
                cursor.execute(consulta,(paciente_id,))
                sesiones = cursor.fetchall()
                return sesiones
            
            except Exception as e:
                print(f"error al buscar sesiones de hemodialisis del paciente: {e}")
            finally:
    
    
                db.close()
                
                
    @classmethod
    def buscar_medico(cls, id_usuario):
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()
            
            consulta = """
                SELECT id_medico, nombre, especialidad, email
                FROM medicos
                WHERE id_usuario= %s;
            """
            cursor.execute(consulta, (id_usuario,))
            medico = cursor.fetchone()  
            
            if medico != None:
                return medico  
            else:
                print("Médico no encontrado")
                return   
        except Exception as e:
            print(f"Error al buscar médico: {e}")
        finally:
            db.close()
        
    
    @classmethod
    def add_medico(cls, *medico):
        
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()
            consulta = """
                INSERT INTO medicos(nombre, especialidad, email, telefono, id_usuario)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id_medico;
            """
            cursor.execute(consulta, medico)
            id_creado = cursor.fetchone()[0]  # Aquí obtienes el ID generado
            db.commit()
            return id_creado
        except Exception as e:
            print("Error al agregar médico:", e)
            return None
        finally:
            cursor.close()
            db.close()
    @classmethod
    def dell_medico(cls, id_medico):
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()
            consulta = """
                DELETE FROM medicos
                WHERE id_medico = %s;
            """
            consulta2 = """
                DELETE FROM citas
                WHERE id_medico = %s;
            """
            cursor.execute(consulta, (id_medico,))
            cursor.execute(consulta2, (id_medico,))
            db.commit()
        except Exception as e:
            print("Error al eliminar médico o cita:", e)
        finally:
            cursor.close()
            db.close()