import flet as ft
from src.components.SectionHeader import SectionHeader
from src.components.ActionButton import ActionButton
from src.components.StatusTag import StatusTag
from src.models.cita import Cita

class CitasPanel(ft.Container):
    def __init__(self,medico):
        
       
        # Create a list to store the checkbox references
        self.checkboxes = []
        lista_citas = Cita.obtener_citas_por_medico(medico[0])
        self.estado_cita = None
        self.filtrar = ft.TextField(
                hint_text="Buscar paciente...",
                prefix_icon=ft.icons.SEARCH,
                border_color="#DFDFDF",
                height=40,
                expand=True
            )
        self.color = None
        self.filas = []

        for lista in lista_citas:
            self.estado_cita = lista[4]
            self.color = self.color_cita()
            checkbox = ft.Checkbox(
                value=False,
                scale=0.9,
                fill_color="#4355B9"
            )
            self.checkboxes.append(checkbox)
            
            self.filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(checkbox),
                        ft.DataCell(ft.Text(f"{lista[0]}", size=13, color="#444444")),
                        ft.DataCell(ft.Text(f"{lista[1]}", size=13, color="#444444")),
                        ft.DataCell(ft.Text(f"{lista[2]}", size=13, color="#444444")),
                        ft.DataCell(ft.Text(f"{lista[3]}", size=13, color="#444444")),
                        ft.DataCell(StatusTag(f"{self.estado_cita}", self.color)),
                    ]
                )
            )
          
        self.citas = ft.DataTable(
            expand=True,
            heading_row_height=40,
            data_row_max_height=40,
            data_row_min_height=40,
            border_radius=8,
            divider_thickness=0,
            horizontal_lines=ft.border.BorderSide(1, "#DFDFDF"),
            columns=[
                ft.DataColumn(label=ft.Text(" ")),
                ft.DataColumn(label=ft.Text("ID CITA", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                ft.DataColumn(label=ft.Text("PACIENTE", weight=ft.FontWeight.BOLD, size=14, color="#444444")),                                                    
                ft.DataColumn(label=ft.Text("FECHA", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                ft.DataColumn(label=ft.Text("HORA", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
                ft.DataColumn(label=ft.Text("ESTADO", weight=ft.FontWeight.BOLD, size=14, color="#444444")),
            ],
            rows=self.filas,
        )
        
        # Create action buttons with event handlers
        self.aceptar_button = ActionButton("ACEPTAR", ft.icons.CHECK_CIRCLE_OUTLINE)
        self.cancelar_button = ActionButton("CANCELAR", ft.icons.CANCEL_OUTLINED)
        
        # Assign click event to the aceptar button
        self.aceptar_button.on_click = self.verificar_y_aceptar_citas
        self.cancelar_button.on_click = self.cancelar_citas
        
         # Contenedor para la tabla de citas
        self.container_citas = ft.Container(
            padding=0,
            expand=True,
            content=ft.Column(
                spacing=15,
                controls=[
                    # Encabezado
                    SectionHeader(ft.icons.DATE_RANGE_ROUNDED, "CITAS"),
                    
                    # Controles de filtrado/búsqueda
                    ft.Row([
                        self.filtrar,
                        ft.IconButton(
                            icon=ft.icons.FILTER_ALT,
                            icon_color="#4355B9",
                            tooltip="Filtrar citas"
                        )
                    ]),
                    
                    # Tabla de citas
                    ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.AUTO,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        spacing=0,
                        controls=[
                            self.citas
                        ]
                    )
                ]
            )
        )
            

        super().__init__(
            expand=True,
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Row(
                spacing=20,
                controls=[
                    self.container_citas,
                    ft.VerticalDivider(color="#DFDFDF"),
                    
                    # Contenedor para los botones
                    ft.Container(
                        width=400,
                        padding=20,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20,
                            controls=[
                                # Botones de acción
                                self.aceptar_button,
                                self.cancelar_button
                            ]
                        )
                    )
                ]
            )
        )
    
    def verificar_y_aceptar_citas(self, e):
        citas_seleccionadas = []
        
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.value:
                id_cita = self.filas[i].cells[1].content.value
                paciente = self.filas[i].cells[2].content.value
                citas_seleccionadas.append((id_cita, paciente))
                checkbox.value = False
        
        # Verificar si hay al menos una cita seleccionada
        if citas_seleccionadas:
            Cita.aceptar_cita(id_cita)  
            self.filas[i].cells[5].content = StatusTag("ACEPTADO", ft.colors.GREEN) 
            self.page.open(
                ft.SnackBar(
                    content=ft.Text(f"CITA ACEPTADA: {id_cita}"),
                    action="OK",
                    action_color=ft.colors.GREEN,
                    duration=2000,
                )
            )
        else:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("NO HAY NINGUNA CITA SELECCIONADA."),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=2000,
                )
            )

        
        self.update()
       
    
    def cancelar_citas(self, e):
        
        citas_canceladas = []
        
        # Verificar qué checkboxes están seleccionados
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.value:
                # Obtener la información de la cita seleccionada
                id_cita = self.filas[i].cells[1].content.value
                paciente = self.filas[i].cells[2].content.value
                citas_canceladas.append((id_cita, paciente))
                
                
                             
                # Desmarcar el checkbox después de procesar
                checkbox.value = False
        
        # Verificar si hay al menos una cita seleccionada
        if citas_canceladas:
            Cita.rechazar_cita(id_cita)  
            self.filas[i].cells[5].content = StatusTag("CANCELADO", ft.colors.RED)
            self.page.open(
                ft.SnackBar(
                    content=ft.Text(f"CITA(S) CANCELADA(S): {id_cita}"),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=2000,
                )
            )
            
        else:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("NO HAY NINGUNA CITA SELECCIONADA."),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=2000,
                )
            )
        
        # Actualizar la interfaz para reflejar los cambios
        self.citas.update()
        self.update()
        self.page.update()
        e.page.update()
    
        
    def color_cita(self):
        if self.estado_cita == "ACEPTADO":
            return ft.colors.GREEN
        elif self.estado_cita == "CANCELADO":
            return ft.colors.RED
        else:
            return ft.colors.ORANGE