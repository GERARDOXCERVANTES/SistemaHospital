import flet as ft
from src.components.TextoIcono import TextoIcono
from src.components.TextfieldsIcons import vitalField
from src.components.ActionButton import ActionButton
class campos(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding= 30,
            bgcolor=ft.colors.WHITE,
            content=ft.Column(
                spacing= 20,
                controls= [
                    TextoIcono(
                        'BUSCAR HISTORIAL',
                        ft.icons.SEARCH_SHARP,
                        ft.colors.BLUE
                    ),
                    ft.Divider(),
                    ft.Column(
                        spacing= 20,
                        controls= [
                           ft.Row(
                               spacing= 20,
                               controls= [
                                   vitalField(
                                       'ID',
                                       ft.icons.BADGE_OUTLINED,
                                   ),
                                   ft.Column(
                                       spacing= 20,
                                       controls= [
                                           ActionButton(
                                                'BUSCAR',
                                                ft.icons.SEARCH,
                                            ),
                                            ActionButton(
                                                'AÑADIR ',
                                                ft.icons.ADD,
                                            ),
                                            
                                       ]
                                   )
                                   
                               ]
                           )
                           
                            
                        ]
                    )
                  
                  
                    
                ]
                
            )
        )
