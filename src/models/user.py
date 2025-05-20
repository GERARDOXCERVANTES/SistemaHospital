import bcrypt
from dataclasses import dataclass
from src.service.db_connection import get_db_connection


@dataclass
class User:
    id_user: str
    password: str
        
    @staticmethod
    def get_user(id_user: str, password: str):
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()        
            consulta = "SELECT contra,rol FROM usuarios WHERE id_usuario = %s"
            cursor.execute(consulta, (id_user,))
            row = cursor.fetchone()
            if row != None:
                hashed_password, rol = row
                if User.check_hash_password(password, hashed_password):
                    return True, rol
                else:
                    return False, None
            else:
                print("Credenciales incorrectas")
                return
        except Exception as e:
            print(f"Error  datos no correctos: {e}")
        finally:
            db.close()
            
             
    @classmethod
    def check_hash_password(cls, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
                
    @classmethod
    def addUser(clc, id_user: str, password: str, rol: str):
        try:
            db = get_db_connection()
            db.connect()
            cursor = db.get_cursor()        
            consulta = "INSERT INTO usuarios (id_usuario, contra, rol) VALUES (%s, %s, %s)"
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursor.execute(consulta, (id_user, hashed_password, rol))
            db.commit()
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            db.close()

            