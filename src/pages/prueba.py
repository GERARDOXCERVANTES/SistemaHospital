import flet as ft
import datetime as dt

class Citas(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Text("Gestión de Citas", size=24, weight=ft.FontWeight.BOLD),
                    # Sección de formulario
                    self.formulario_cita(),
                    # Tabla de citas agendadas
                    self.tabla_citas()
                ]
            )
        )

    def formulario_cita(self):
        """Crea un contenedor con el formulario para agendar una cita."""
        
        # Variables para almacenar la información de la cita
        self.paciente_id = ft.TextField(label="ID Paciente", width=200)
        self.doctor = ft.TextField(label="Médico", width=200)
        self.hora = ft.TextField(label="Hora (HH:MM)", width=150, hint_text="Ej. 10:30")
        
        # Variable para almacenar la fecha seleccionada
        self.fecha_seleccionada = None
        
        # Botón que abre el DatePicker
        boton_fecha = ft.ElevatedButton(
            text="Seleccionar Fecha",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=self.abrir_date_picker
        )
        
        # Botón para Agendar la cita
        boton_agendar = ft.ElevatedButton(
            text="Agendar Cita",
            icon=ft.icons.ADD,
            on_click=self.agregar_cita
        )
        
        # Contenedor con el formulario
        formulario = ft.Row(
            spacing=20,
            controls=[
                self.paciente_id,
                self.doctor,
                self.hora,
                boton_fecha,
                boton_agendar
            ]
        )
        
        return formulario
    
    def tabla_citas(self):
        """
        Crea una DataTable para mostrar las citas.
        Guardaremos las filas en self.lista_citas y actualizaremos la tabla dinámicamente.
        """
        # Almacenaremos las citas en una lista interna
        self.lista_citas = []
        
        # Creamos las columnas de la tabla
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("ID Paciente")),
                ft.DataColumn(label=ft.Text("Médico")),
                ft.DataColumn(label=ft.Text("Fecha")),
                ft.DataColumn(label=ft.Text("Hora")),
            ],
            rows=[],
            expand=True
        )
        
        return self.data_table

    def abrir_date_picker(self, e):
        """Abre un DatePicker en una ventana emergente para seleccionar la fecha."""
        # page.open() abre un DatePicker de manera emergente
        self.page.open(
            ft.DatePicker(
                first_date=dt.datetime.now(),              # Desde hoy
                last_date=dt.datetime.now() + dt.timedelta(days=365),  # Hasta un año después
                on_change=self.on_fecha_cambiada,
                on_dismiss=self.on_datepicker_cerrado,
            )
        )
    
    def on_fecha_cambiada(self, e):
        """Se llama cuando el usuario selecciona una fecha en el DatePicker."""
        fecha = e.control.value  # Esto es un objeto datetime.date
        self.fecha_seleccionada = fecha
        print(f"Fecha seleccionada: {fecha.strftime('%Y-%m-%d')}")
        # Puedes mostrar la fecha seleccionada en un Text o en la consola
    
    def on_datepicker_cerrado(self, e):
        """Se llama cuando se cierra el DatePicker sin seleccionar fecha."""
        print("DatePicker cerrado (sin selección)")
    
    def agregar_cita(self, e):
        """Agrega una cita a la tabla de citas."""
        # Verificamos si tenemos fecha seleccionada
        if not self.fecha_seleccionada:
            self.page.snack_bar = ft.SnackBar(ft.Text("Por favor, selecciona una fecha."))
            self.page.snack_bar.open = True
            self.page.update()
            return
        
        # Obtenemos los valores del formulario
        paciente_id = self.paciente_id.value.strip()
        doctor = self.doctor.value.strip()
        hora = self.hora.value.strip()
        
        if not paciente_id or not doctor or not hora:
            self.page.snack_bar = ft.SnackBar(ft.Text("Por favor, completa todos los campos."))
            self.page.snack_bar.open = True
            self.page.update()
            return
        
        # Convertimos la fecha a string para mostrarla en la tabla
        fecha_str = self.fecha_seleccionada.strftime('%Y-%m-%d')
        
        # Creamos una fila para la tabla
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(paciente_id)),
                ft.DataCell(ft.Text(doctor)),
                ft.DataCell(ft.Text(fecha_str)),
                ft.DataCell(ft.Text(hora)),
            ]
        )
        
        # Agregamos la nueva cita a nuestra lista interna
        self.lista_citas.append(nueva_fila)
        
        # Actualizamos la tabla con la nueva fila
        self.data_table.rows = self.lista_citas
        self.page.update()
        
        # Limpieza de campos
        self.paciente_id.value = ""
        self.doctor.value = ""
        self.hora.value = ""
        self.fecha_seleccionada = None

# Función principal para correr la app
def main(page: ft.Page):
    page.title = "Gestión de Citas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(Citas())

ft.app(target=main)
