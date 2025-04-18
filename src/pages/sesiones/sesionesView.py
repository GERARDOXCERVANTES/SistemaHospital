import flet as ft
from src.pages.sesiones.components.formulario import formulario
from src.pages.sesiones.components.dataP import infoPaciente
from src.pages.sesiones.components.monitoreo import MonitoreoIu
from src.pages.sesiones.components.aceesoVascular import accesoVascularIu

class sesionV(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
            content= ft.Row(
                spacing= 30,
                controls= [
                   ft.Card(
                       expand= True,
                       color= ft.colors.WHITE,
                       elevation= 5,
                       content= ft.Container (
                           expand= True,
                           padding= 20,
                           content= ft.Column(
                                    spacing= 20,
                                    controls=[
                                        infoPaciente(),
                                         ft.Card(
                                             expand= True,
                                             color= ft.colors.WHITE,
                                             elevation= 5,
                                             content=ft.Tabs(
                                                tab_alignment= ft.TabAlignment.CENTER,
                                                selected_index= 0,
                                                animation_duration= 300,
                                                tabs= [
                                                    ft.Tab(
                                                        tab_content= ft.Icon(ft.icons.INFO_OUTLINE_ROUNDED),
                                                        content= formulario()
                                                    ),
                                                    ft.Tab(
                                                        tab_content= ft.Icon(ft.icons.PERSONAL_INJURY_ROUNDED),
                                                        content=  accesoVascularIu()
                                                    ),
                                                    
                                                    
                                                ]
                                            )
                                         )
                                       
                                        
                                    ]
                                )
                           
                       )

                   ),
                   ft.Card(
                       expand= True,
                       color= ft.colors.WHITE,
                       elevation= 5,
                       content= ft.Container(
                           expand= True,
                           padding= 20,
                           content= ft.Column(
                               spacing= 30,
                               controls= [
                                   MonitoreoIu(),
                               ]
                               
                           )
                       )
                   )
                ]
            )
        )
        
