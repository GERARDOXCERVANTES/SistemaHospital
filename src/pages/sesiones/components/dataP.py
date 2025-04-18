import flet as ft
from src.components.TextoIcono import TextoIcono
import datetime as dt
class content(ft.Container):
    def __init__(self):
        super().__init__(
            padding= 30,
            expand= True,            
            content= ft.Column(
                spacing= 20,
                controls=[
                    TextoIcono(
                        "DATOS DE PACIENTE ",
                        icono= ft.Icons.PERSON_SEARCH,
                        IconC= ft.Colors.BLUE
                        
                    ),ft.Divider(),
                    ft.Column(
                       spacing= 40,
                       controls= [
                        TextoIcono(
                            texto= f"ID:  ",
                            icono= ft.icons.BADGE_ROUNDED, 
                            IconC= ft.colors.BLUE
                            ),
                        TextoIcono(
                            f"NOMBRE: ",
                            icono= ft.Icons.PERSON,
                            IconC= ft.Colors.BLUE
                            ),
                        TextoIcono(
                            f"INICIO DE SESION:  ",
                            icono= ft.Icons.TIMELAPSE,
                            IconC= ft.Colors.BLUE
                        ),
                        TextoIcono(
                            f"FECHA SESION:  ",
                            icono= ft.Icons.CALENDAR_TODAY,
                            IconC= ft.Colors.BLUE
                        )
                        
                        
                       ]
                    )
                ]
            )
        )
        
class infoPaciente(ft.Card):
    def __init__(self):
        super().__init__(
            expand= True,
            elevation= 5,
            color= ft.colors.WHITE,
            content= content()
        )
        
def horaA():
    ahora = dt.datetime.now()
        
    return ahora.strftime("%H:%M:%S")
    
 