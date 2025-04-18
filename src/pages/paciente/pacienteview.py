import flet as ft
from src.pages.paciente.components.paciente_info import PacienteInfo
from src.pages.paciente.components.condiconies import Condiciones
from src.pages.paciente.components.sesiones_hemodialisis import SesionesHemodialisis
from src.pages.paciente.components.buscador_paciente import BuscadorPaciente
from src.pages.paciente.components.citasA import CitasAgendadas

class PacienteView(ft.Container):
    def __init__(self):
        paciente_info = PacienteInfo()
        Condiciones_info = Condiciones()
        citas = CitasAgendadas()
        super().__init__(
            expand=True,
            padding= 0,
            content= ft.Row(
                spacing= 20,
                controls= [
                    ft.Card(
                        expand= True,
                        elevation=5,
                        color= ft.colors.WHITE,
                        content= ft.Column(
                        spacing= 20,
                        controls= [
                            paciente_info,
                            ft.Divider(),
                            Condiciones_info,
                            ft.Divider(),
                            SesionesHemodialisis(),
                            
                            ]
                        )
                    ),
                    ft.Card(
                        expand= True,
                        elevation=5,
                        color= ft.colors.WHITE,
                        content= ft.Column(
                            spacing= 20,
                            controls= [
                                BuscadorPaciente(paciente_info,Condiciones_info,citas),
                                ft.Divider(),
                                citas,
                            ]
                        )
                    )
                    
                ]
            )
        )

        