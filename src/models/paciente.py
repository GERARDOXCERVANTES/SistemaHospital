from dataclasses import dataclass, field
from datetime import date
from typing import Optional

@dataclass
class Paciente:
    
    id_paciente: Optional[int] = None 
    nombre: str
    apellido: str
    fecha_nacimiento: date
    documento: str
    tipo_sangre: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    fecha_registro: date = field(default_factory=date.today)
    
    

            
        
            
    