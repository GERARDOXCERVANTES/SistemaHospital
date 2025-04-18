import flet as ft
from src.components.TextfieldsIcons import vitalField
class PostSesionIu(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
            padding= 20,
            content= ft.Row(
                spacing= 40,
                controls= [
                    ft.Column(
                        spacing= 20,
                        controls= [
                            vitalField(
                                "PESO POST SESION",
                                ft.icons.MONITOR_WEIGHT_ROUNDED,
                                'kg',
                                '0.0'
                            ),vitalField(
                                "PRESIÓN ARTERIAL FINAL",
                                ft.icons.SPEED,
                                "mmHg",
                                "120/80"
                            ),
                            
                        ]
                    ),
                    ft.Column(
                        spacing= 20,
                        controls= [
                            vitalField(
                                "FRECUENCIA CARDIACA FINAL",
                                ft.icons.FAVORITE,
                                "lpm",
                                "0"
                            ),
                                vitalField(
                                "TEMPERATURA FINAL",
                                ft.icons.THERMOSTAT,
                                "°C",
                                "0.0"
                            ),
                        ]
                    )
                ]
            )
        )