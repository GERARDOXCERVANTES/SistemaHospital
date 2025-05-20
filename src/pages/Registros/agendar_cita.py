import flet as ft
import datetime as dt
from src.components.SectionHeader import SectionHeader
from src.components.StatusTag import StatusTag
from src.components.TextfieldsIcons import vitalField
from src.components.ActionButton import ActionButton
from src.components.DataRow import DataRow
from src.models.medico import Medico
from src.models.cita import Cita

def tiempoA():
    """Obtener la fecha actual"""
    return dt.datetime.now()

def mesS():
    """Obtener el primer día del siguiente mes"""
    x = tiempoA()
    
    if x.month == 12:
        siguiente = dt.datetime(x.year + 1, 1, 1)
    else:
        siguiente = dt.datetime(x.year, x.month + 1, 1)
    return siguiente

class AgendarCita(ft.Container):
    def __init__(self):
        # Inicializar valores
        self.id_paciente = None
        self.fecha_iso = None
        self.hora_iso = None
        self.medico_id = None
        
        # Crear campos de entrada
        self.paciente_field = vitalField(label="Paciente", icon=ft.icons.PERSON_OUTLINE, on_submit=self.buscar_paciente)
        self.medico_field = vitalField(label="Médico", icon=ft.icons.MEDICAL_SERVICES)
        
        # Valores para mostrar
        self.paciente_valor = "Paciente: No seleccionado"
        self.fecha_valor = "Fecha: No seleccionada"
        self.hora_valor = "Hora: No seleccionada"
        
        # Crear botones de acción
        self.btn_fecha = ActionButton("FECHA", ft.icons.CALENDAR_MONTH, self.abrir_calendario)
        self.btn_hora = ActionButton("HORA", ft.icons.ACCESS_TIME, self.abrir_horario)
        self.btn_agendar = ActionButton("AGENDAR", ft.icons.ADD, self.guardar_cita)
        
        # Panel de detalles
        self.detalles_columna = self.construir_detalles_columna()
        
        # Tabla de citas
        self.checkboxes = []
        lista_citas = Cita.obtener_all_citas()
        self.estado_cita = None
        self.filtrar = ft.TextField(
            hint_text="Buscar paciente...",
            prefix_icon=ft.icons.SEARCH,
            border_color="#DFDFDF",
            height=40,
            expand=True,
            on_change=self.filtrar_citas
        )
        self.color = None
        self.filas = []
        self.todas_filas = []  # Para mantener todas las filas para el filtrado

        for lista in lista_citas:
            self.estado_cita = lista[4]
            self.color = self.color_cita()
            checkbox = ft.Checkbox(
                value=False,
                scale=0.9,
                fill_color="#4355B9"
            )
            self.checkboxes.append(checkbox)
            
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(checkbox),
                    ft.DataCell(ft.Text(f"{lista[0]}", size=13, color="#444444")),
                    ft.DataCell(ft.Text(f"{lista[1]}", size=13, color="#444444")),
                    ft.DataCell(ft.Text(f"{lista[2]}", size=13, color="#444444")),
                    ft.DataCell(ft.Text(f"{lista[3]}", size=13, color="#444444")),
                    ft.DataCell(StatusTag(f"{self.estado_cita}", self.color)),
                ]
            )
            self.filas.append(fila)
            self.todas_filas.append(fila)
          
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
        self.actualizar_button = ActionButton("ACTUALIZAR", ft.icons.REFRESH)
        
        self.aceptar_button.on_click = self.verificar_y_aceptar_citas
        self.cancelar_button.on_click = self.cancelar_citas
        self.actualizar_button.on_click = self.actualizar_citas
        
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
                            tooltip="Filtrar citas",
                            on_click=self.mostrar_filtros
                        )
                    ]),
                    
                    # Tabla de citas
                    ft.Container(
                        expand=True,
                        border_radius=8,
                        border=ft.border.all(1, "#DFDFDF"),
                        padding=10,
                        content=ft.Column(
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                            spacing=0,
                            controls=[
                                self.citas
                            ]
                        )
                    ),
                    
                    # Botones de acción
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                        controls=[
                            self.actualizar_button,
                            self.aceptar_button,
                            self.cancelar_button
                        ]
                    )
                ]
            )
        )

        super().__init__(
            expand=True,
            bgcolor=ft.colors.WHITE,
            padding=20,
            border_radius=30,
            content=ft.Column(
                spacing=20,
                controls=[
                    # Título principal
                    ft.Container(
                        content=ft.Text("GESTIÓN DE CITAS", size=24, weight=ft.FontWeight.BOLD),
                        padding=10,
                        alignment=ft.alignment.center
                    ),
                    
                    # Panel principal
                    ft.Row(
                        spacing=20,
                        expand=True,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            # Panel izquierdo - Formulario
                            ft.Card(
                                elevation=2,
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Column(
                                        spacing=15,
                                        controls=[
                                            ft.Text("Nueva Cita", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Divider(height=1),
                                            
                                            ft.Row(
                                                spacing=20,
                                                controls=[
                                                    ft.Column(
                                                        spacing=20,
                                                        controls=[
                                                            self.paciente_field,
                                                            self.medico_field,
                                                        ],
                                                        expand=True
                                                    ),
                                                    ft.Column(
                                                        spacing=20,
                                                        controls=[
                                                            self.btn_fecha,
                                                            self.btn_hora,
                                                            self.btn_agendar
                                                        ],
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                                    )
                                                ]
                                            ),
                                            
                                            ft.Container(
                                                padding=15,
                                                border_radius=8,
                                                bgcolor=ft.colors.SURFACE_VARIANT,
                                                content=self.detalles_columna
                                            )
                                        ]
                                    )
                                ),
                                width=400
                            ),
                            
                            # Panel derecho - Tabla de citas
                            ft.Card(
                                elevation=2,
                                expand=True,
                                content=ft.Container(
                                    padding=20,
                                    content=ft.Column(
                                        spacing=15,
                                        controls=[
                                            ft.Text("Citas Programadas", size=18, weight=ft.FontWeight.BOLD),
                                            ft.Divider(height=1),
                                            ft.Container(
                                                content=self.container_citas,
                                                height=500,
                                                expand=True
                                            )
                                        ]
                                    )
                                )
                            )
                        ]
                    )
                ]
            )
        )
    
    def construir_detalles_columna(self):
        """Construir la columna de detalles de la cita"""
        return ft.Column(
            spacing=10,
            controls=[
                ft.Text("DETALLES DE LA CITA", size=16, weight=ft.FontWeight.BOLD),
                ft.Divider(height=1),
                DataRow(ft.icons.PERSON_OUTLINE, self.paciente_valor, size=14),
                DataRow(ft.icons.CALENDAR_TODAY, self.fecha_valor, size=14),
                DataRow(ft.icons.ACCESS_TIME, self.hora_valor, size=14)
            ]
        )
    
    def abrir_calendario(self, e):
        """Abrir el selector de fecha"""
        self.page.open(
            ft.DatePicker(
                first_date=tiempoA(),
                last_date=mesS(),
                on_change=self.handle_date_change,
                on_dismiss=self.handle_dismissal,
            )
        )
    
    def abrir_horario(self, e):
        """Abrir el selector de hora"""
        self.page.open(
            ft.TimePicker(
                confirm_text="CONFIRMAR",
                error_invalid_text="TIEMPO INVÁLIDO",
                help_text="ELIGE LA HORA",
                on_change=self.handle_time_change,
                on_dismiss=self.handle_dismissal,
            )
        )
    
    def handle_time_change(self, e):
        """Manejar el cambio de hora seleccionada"""
        self.hora_iso = e.control.value.strftime('%H:%M')
        hora = e.control.value.strftime('%H:%M %p')
        self.hora_valor = f"Hora: {hora}"
        
        # Actualizar la columna de detalles
        self.detalles_columna = self.construir_detalles_columna()
        # Acceder correctamente al contenedor de detalles
        self.content.controls[1].controls[0].content.content.controls[3].content = self.detalles_columna
        self.update()
    
    def handle_date_change(self, e):
        """Manejar el cambio de fecha seleccionada"""
        self.fecha_iso = e.control.value.strftime('%Y-%m-%d')
        self.fecha_valor = f"Fecha: {self.fecha_iso}"
        
        # Actualizar la columna de detalles
        self.detalles_columna = self.construir_detalles_columna()
        # Acceder correctamente al contenedor de detalles
        self.content.controls[1].controls[0].content.content.controls[3].content = self.detalles_columna
        self.update()
    
    def handle_dismissal(self, e):
        self.page.open(
            ft.SnackBar(
                content=ft.Text("Selección cerrada"),
                action="OK",
                action_color=ft.colors.GREEN,
                duration=1000,
            )
        )
    
    def buscar_paciente(self, e):
        """Buscar paciente por ID"""
        paciente_id = self.paciente_field.value
        if not paciente_id:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Ingrese un ID de paciente"),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=2000,
                )
            )
            return
            
        x = Medico.buscar_paciente_id(paciente_id)
        
        # Verificar que se encontró el paciente
        if x and len(x) > 1:
            nom = x[1]
            self.id_paciente = paciente_id
            self.paciente_valor = f"Paciente: {paciente_id} - {nom}"
            
            # Actualizar la columna de detalles
            self.detalles_columna = self.construir_detalles_columna()
            # Acceder correctamente al contenedor de detalles
            self.content.controls[1].controls[0].content.content.controls[3].content = self.detalles_columna
        else:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Paciente no encontrado"),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=2000,
                )
            )
            return
        
        self.update()
    
    def guardar_cita(self, e):
        """Guardar la cita en la base de datos"""
        if not self.id_paciente or not self.fecha_iso or not self.hora_iso or not self.medico_field.value:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Complete todos los campos para agendar la cita"),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=2000,
                )
            )
            return
        
        # Guardar cita en la base de datos
        id_cita = Cita.nueva_cita(self.fecha_iso, self.hora_iso, self.medico_field.value, self.id_paciente)
        
        # Actualizar la tabla
        self.actualizar_citas(None)
        
        # Limpiar los campos
        self.paciente_field.value = ""
        self.medico_field.value = ""
        self.paciente_valor = "Paciente: No seleccionado"
        self.fecha_valor = "Fecha: No seleccionada"
        self.hora_valor = "Hora: No seleccionada"
        self.id_paciente = None
        self.fecha_iso = None
        self.hora_iso = None
        
        # Actualizar la columna de detalles
        self.detalles_columna = self.construir_detalles_columna()
        # Acceder correctamente al contenedor de detalles
        self.content.controls[1].controls[0].content.content.controls[3].content = self.detalles_columna
        
        self.page.open(
            ft.SnackBar(
                content=ft.Text("¡CITA GUARDADA CON ÉXITO!"),
                action="OK",
                action_color=ft.colors.GREEN,
                duration=2000,
            )
        )
        
        self.update()
    
    def color_cita(self):
        """Determinar el color según el estado de la cita"""
        if self.estado_cita == "ACEPTADO":
            return ft.colors.GREEN
        elif self.estado_cita == "CANCELADO":
            return ft.colors.RED
        else:
            return ft.colors.ORANGE
    
    def filtrar_citas(self, e):
        """Filtrar citas por texto de búsqueda"""
        texto = self.filtrar.value.lower()
        if not texto:
            self.filas = self.todas_filas.copy()
        else:
            self.filas = []
            for fila in self.todas_filas:
                # Buscar en ID de cita y nombre de paciente (columnas 1 y 2)
                id_cita = fila.cells[1].content.value.lower()
                paciente = fila.cells[2].content.value.lower()
                if texto in id_cita or texto in paciente:
                    self.filas.append(fila)
        
        self.citas.rows = self.filas
        self.update()
    
    def mostrar_filtros(self, e):
        
        self.page.open(
            ft.SnackBar(
                content=ft.Text("Filtros avanzados disponibles próximamente"),
                action="OK",
                action_color=ft.colors.BLUE,
                duration=2000,
            )
        )
    
    def actualizar_citas(self, e):
        """Actualizar la lista de citas desde la base de datos"""
        # Limpiar listas existentes
        self.checkboxes = []
        self.filas = []
        self.todas_filas = []
        
        # Obtener citas actualizadas
        lista_citas = Cita.obtener_all_citas()
        
        for lista in lista_citas:
            self.estado_cita = lista[4]
            self.color = self.color_cita()
            checkbox = ft.Checkbox(
                value=False,
                scale=0.9,
                fill_color="#4355B9"
            )
            self.checkboxes.append(checkbox)
            
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(checkbox),
                    ft.DataCell(ft.Text(f"{lista[0]}", size=13, color="#444444")),
                    ft.DataCell(ft.Text(f"{lista[1]}", size=13, color="#444444")),
                    ft.DataCell(ft.Text(f"{lista[2]}", size=13, color="#444444")),
                    ft.DataCell(ft.Text(f"{lista[3]}", size=13, color="#444444")),
                    ft.DataCell(StatusTag(f"{self.estado_cita}", self.color)),
                ]
            )
            self.filas.append(fila)
            self.todas_filas.append(fila)
        
        # Actualizar la tabla
        self.citas.rows = self.filas
        
        self.page.open(
            ft.SnackBar(
                content=ft.Text("Lista de citas actualizada"),
                action="OK",
                action_color=ft.colors.GREEN,
                duration=1000,
            )
        )
        
        self.update()
        
    def verificar_y_aceptar_citas(self, e):
        """Aceptar las citas seleccionadas"""
        citas_seleccionadas = []
        
        # Verificar qué checkboxes están seleccionados
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.value:
                # Obtener la información de la cita seleccionada
                id_cita = self.filas[i].cells[1].content.value
                citas_seleccionadas.append(id_cita)
                
                # Actualizar estado en la UI
                self.filas[i].cells[5].content = StatusTag("ACEPTADO", ft.colors.GREEN)
                
                # Actualizar en la base de datos
                Cita.aceptar_cita(id_cita)
                
                # Desmarcar el checkbox después de procesar
                checkbox.value = False
        
        # Verificar si hay al menos una cita seleccionada
        if citas_seleccionadas:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text(f"CITAS ACEPTADAS: {', '.join(citas_seleccionadas)}"),
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

        # Actualizar la interfaz
        self.update()

    def cancelar_citas(self, e):
        """Cancelar las citas seleccionadas"""
        citas_canceladas = []
        
        # Verificar qué checkboxes están seleccionados
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.value:
                # Obtener la información de la cita seleccionada
                id_cita = self.filas[i].cells[1].content.value
                citas_canceladas.append(id_cita)
                
                # Actualizar estado en la UI
                self.filas[i].cells[5].content = StatusTag("CANCELADO", ft.colors.RED)
                
                # Actualizar en la base de datos
                Cita.rechazar_cita(id_cita)
                
                # Desmarcar el checkbox después de procesar
                checkbox.value = False

        # Verificar si hay al menos una cita seleccionada
        if citas_canceladas:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text(f"CITAS CANCELADAS: {', '.join(citas_canceladas)}"),
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
        
        # Actualizar la interfaz
        self.update()