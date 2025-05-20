from src.models.medico import Medico
from src.pages.medico import medico_view
from src.pages.recepcionista import recepcionista_View

class Identificador:
    
        
    @classmethod
    def identificar_rol(cls, autentificacion, rol,user,page):
            if autentificacion:
                if rol != "medico":
                    page.controls.clear()
                    page.add(recepcionista_View(page))
                    page.update()
                    
                if rol != "recepcionista":
                    medico = Medico.buscar_medico(user)
                    page.controls.clear()
                    page.add(medico_view(page,medico))
                    page.update()
                   
                else:
                    return
        