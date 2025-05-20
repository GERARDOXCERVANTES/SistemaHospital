
from src.service.db_connection import get_db_connection



class Paciente:
    
     
    @classmethod
    def new_paciente(cls, *paciente):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                INSERT INTO pacientes(nombre, sexo, fecha_nacimiento, tipo_sangre, telefono, direccion)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor.execute(consulta, paciente)
            db.commit()
        except Exception as e:
            print(f"Error al guardar nuevo paciente: {e}")
        finally:
            db.close()


    
    @classmethod
    def eliminar_paciente(cls,id_paciente):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                DELETE FROM pacientes
                WHERE id_paciente = %s;
            """
            cursor.execute(consulta,(id_paciente))
            db.commit()
        except Exception as e:
            print(f"Error al eliminar  paciente: {e}")
        finally:
            db.close()
            
            
    @classmethod
    def add_alergias(cls,id_paciente,alergia):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                INSERT INTO alergias(alergia,id_paciente)
	            VALUES(%s,%s);
            """
            cursor.execute(consulta, (alergia,id_paciente))
            db.commit()
        except Exception as e:
            print(f"Error al guardar nueva alergia: {e}")
        finally:
            db.close()
            
    @classmethod
    def add_condicones(cls,id_paciente,condicion):
        db = get_db_connection()
        db.connect()
        cursor = db.get_cursor()
        try:
            consulta = """
                INSERT INTO condiciones(condicion,id_paciente)
	            VALUES(%s,%s);
            """
            cursor.execute(consulta, (condicion,id_paciente))
            db.commit()
        except Exception as e:
            print(f"Error al guardar nueva condcion: {e}")
        finally:
            db.close()
