import flet as ft
from src.components.TextoIcono import TextoIcono
from src.components.TextfieldsIcons import vitalField
from src.components.ActionButton import ActionButton
from src.models.medico import Medico
from src.pages.paciente.components.paciente_info import PacienteInfo
from src.pages.paciente.components.condiconies import Condiciones
from src.pages.paciente.components.citasA import CitasAgendadas
class BuscadorPaciente(ft.Container):
    def __init__(self, paciente_info: PacienteInfo,condiciones_info : Condiciones,citas : CitasAgendadas):
        self.citas = citas
        self.paciente_info = paciente_info  
        self.condiciones_info = condiciones_info
        self.campo = vitalField(
            'ID DE USUARIO',
            ft.Icons.PERSON_3_ROUNDED,
            on_submit=self.search_id
        )

        super().__init__(
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Column(
                        controls=[
                            TextoIcono(
                                'BUSCAR PACIENTE',
                                ft.icons.PERSON_3_ROUNDED,
                                '#111184'
                            ),
                            ft.Divider(),
                        ]
                    ),
                    ft.Container(
                        height=150,
                        padding=40,
                        width=800,
                        content=ft.Row(
                            spacing=120,
                            controls=[
                                self.campo,
                                ActionButton(
                                    'BUSCAR',
                                    ft.icons.SEARCH_ROUNDED,
                                    on_click=self.search_id
                                )
                            ]
                        )
                    )
                ]
            )
        )
        
    def search_id(self, e):
        paciente_id = self.campo.value.strip()
        if not paciente_id:
            print("Por favor, ingresa un ID válido.")
            return

        paciente_data = Medico.buscar_paciente_id(paciente_id)
        lista_alergias = Medico.buscar_alergias(paciente_id)
        lista_condiciones = Medico.buscar_condiciones(paciente_id)
        citas_pacientes = Medico.buscar_citas(paciente_id)
        
        self.citas.update_citas(citas_pacientes)
        self.paciente_info.update_info(paciente_data)
        self.condiciones_info.update_alergias(lista_alergias)
        self.condiciones_info.update_condiciones(lista_condiciones)
        # Limpiamos el campo
        self.campo.value = ""
        
