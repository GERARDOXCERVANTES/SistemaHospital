import flet as ft
from src.components.TextoIcono import TextoIcono

class Condiciones(ft.Container):
    def __init__(self):
        self.alergias =  []
        self.condiciones = []
        self.listView_condiciones = ft.ListView( 
            expand= True,
            spacing= 20,
            controls=
                    self.condiciones
                
                )
        self.listView_Alergias = ft.ListView(
            expand= True,
            spacing= 20,
            controls= self.alergias                          
            )
        
        
        super().__init__(
            height= 200,
            width= 800,
            content= ft.Container(
                    padding= 20,
                    content=ft.Row(
                        spacing= 20,
                        controls=[
                            ft.Column(
                                expand= True,
                                spacing= 20,
                                controls=[
                                    ft.Row(
                                        spacing= 20,
                                        controls=[
                                            ft.Icon(
                                                ft.icons.MEDICAL_INFORMATION_OUTLINED,
                                                size= 24,

                                            ),
                                            ft.Text(
                                                'ALERGIAS',
                                                color= "#111184",
                                                size= 18,
                                                weight= ft.FontWeight.BOLD 
                                            )
                                        ]
                                    ),
                                    self.listView_Alergias
                                    
                                ]
                            ),
                            ft.Column(
                                expand= True,
                                spacing= 20,
                                controls= [
                                    ft.Row(
                                        spacing= 20,
                                        controls= [
                                            ft.Icon(
                                                ft.icons.MEDICATION_SHARP,
                                                size= 24
                                            ),
                                            ft.Text(
                                                'CONDICIONES PREVIA',
                                                color= "#111184",
                                                size= 18,
                                                weight= ft.FontWeight.BOLD
                                            )
                                        ]
                                    ),
                                    self.listView_condiciones
                                    
                                ]
                                                                                            
                            ) 
                                                   
                        ]
                    )
                    
                
            )
                                             
        )
        
    def update_alergias(self, alergia_date):
        
        self.alergias.clear()
        
        if alergia_date:
            for alergias in alergia_date:
                self.alergias.append(ft.Text(f"-{alergias[0]}"))
        
        self.listView_Alergias.controls = self.alergias
        self.update()
        
    def update_condiciones(self,condiciones_date):
        self.condiciones.clear()
        if condiciones_date:
            for condiciones in condiciones_date:
                self.condiciones.append(ft.Text(f"-{condiciones[0]}"))
                
        self.listView_condiciones.controls = self.condiciones
        self.update()
        