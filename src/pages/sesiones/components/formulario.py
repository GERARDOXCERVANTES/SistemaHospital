import flet as ft
from src.components.TextoIcono import TextoIcono
from src.components.TextfieldsIcons import vitalField
class formulario(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding= 30,
            content = 
            ft.Column(
                spacing= 20,
                controls= [
                    ft.ResponsiveRow(
                        spacing= 60,
                        controls= [
                        ft.Column(
                            spacing= 30,
                            col={"xs": 12, "sm": 6, "md": 6, "lg": 6},
                            controls=[
                               vitalField(
                                   "PESO INICIAL",
                                   ft.icons.MONITOR_WEIGHT,
                                   "kg",
                                   "0.0"
                                   ),
                                vitalField(
                                    "PESO SECO",
                                    ft.icons.SCALE,
                                    "kg",
                                    "0.0"
                                    ),
                                vitalField(
                                    "FRECUENCIA CARDIACA",
                                    ft.icons.FAVORITE,
                                    "lpm",
                                    "0"
                                    ),
                                
                                
                                
                                
                            ]
                            
                        ),ft.Column(
                            spacing= 20,
                            col={"xs": 12, "sm": 6, "md": 6, "lg": 6},
                            controls= [
                                vitalField(
                                    "TEMPERATURA ACTUAL",
                                    ft.icons.THERMOSTAT,
                                    "°C",
                                    "0.0"
                                    ),
                                vitalField(
                                    "DURACIÓN DE LA SESION",
                                    ft.icons.TIMELAPSE,
                                    "horas",
                                    "0.0"
                                    ),
                                vitalField(
                                    "PRESIÓN ARTERIAL",
                                    ft.icons.SPEED,
                                    "mmHg",
                                    "120/80"
                                    ),
                            ]
                        )
                          
                        ]
                        
                    )
                ]
                
            )
        )


    


