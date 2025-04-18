from src.service.db_connection import get_db_connection
from src.models.medico import Medico

# Obtener (o crear) la instancia de Database a partir de la config
db = get_db_connection()

try:
    db.connect()
    paciente = Medico.buscar_paciente_id(1)  # Cambia el ID según lo que necesites
    print("Paciente encontrado:", paciente[1])

    print("Conexión exitosa")
except Exception as e:
    print("Error al conectar con la base de datos:", e)
