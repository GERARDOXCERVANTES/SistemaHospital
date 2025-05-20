import bcrypt


'''salt = bcrypt.gensalt()
text = "nubeRecepcionista".encode('utf-8')
hashed = bcrypt.hashpw(text, salt)
print(hashed)

pw1  = b'$2b$12$QR08emaQ11gkcE3TMgOBuOxMC4Ne2WzhOeCdLPBz0k8KcImc7gkBO' #arbolmedico
pw2  = b'$2b$12$wMVtRI6TVkIiGkf7O/zRbOZzlonTOYKH/qowZBdybY8owSyVaovMK' #nubeRecepcionista
'''

''' text = bytes(input("Introduce la contraseña: "), 'utf-8')
if bcrypt.checkpw(text, pwd):
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
'''

class SequentialIDGenerator:
    def __init__(self):
        self.counter = 1
    
    def generate_id(self, ROL,APELLIDO):
        pieza = ROL[0:2]
        pieza2 = APELLIDO[0:2]
        unique_id = f"{pieza}{pieza2}{self.counter}"
        self.counter += 1
        return unique_id

# Ejemplo de uso
generator = SequentialIDGenerator()
print(generator.generate_id("MEDICO","JUAN"))  # "USER1"
print(generator.generate_id("RECEPCIONISTA","GERARDO"))  # "USER2"
