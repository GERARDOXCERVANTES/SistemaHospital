import flet as ft
import datetime as dt
from src.components.ActionButton import ActionButton
from src.components.TextfieldsIcons import vitalField
from src.components.DataRow import DataRow
from src.models.medico import Medico
from src.models.cita import Cita

# Clase principal para la interfaz de citas
class iuCitas(ft.Container):
    def __init__(self,medico):  
        super().__init__(
            alignment=ft.alignment.center,
            expand=True,
            padding=0,
            content=date(medico)  
        )

# Función para obtener la fecha actual
def tiempoA():
    hoy = dt.datetime.now()
    return hoy

# Función para obtener el primer día del siguiente mes
def mesS():
    x = tiempoA()
    
    if x.month == 12:
        siguiente = dt.datetime(x.year + 1, 1, 1)
    else:
        siguiente = dt.datetime(x.year, x.month + 1, 1)
    return siguiente


class date(ft.Container):
    def __init__(self,medico):
        self.id_paciente = None
        self.fecha_iso   = None          
        self.hora_iso    = None          

        self.medico_id = medico[0]
        self.paciente_valor = "Paciente: ----"
        self.fecha_valor = "Fecha: ----"
        self.hora_valor = "Hora: ----"
        self.texfiel_id = vitalField("ID Paciente", ft.icons.PERSON_OUTLINE, "", "",self.buscar_pacientes)
        self.detalles_columna = self.construir_detalles_columna()
        
        super().__init__(
            expand=True,
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                spacing=40,
                controls=[
                    ft.Column(
                        spacing=20,
                        controls=[  
                            self.texfiel_id,
                        ]
                    ),
                    ft.VerticalDivider(),
                    ft.Column(
                        spacing=20,
                        controls=[
                            #BOTON PARA ABRIR CALENDARIO
                            ActionButton("FECHA", ft.icons.CALENDAR_MONTH, self.AbrirCalendario),
                            ActionButton("HORA", ft.icons.TIMELAPSE, self.abrirHorario),
                            ActionButton("AGENDAR", ft.icons.ADD,self.limpiar_campos)
                        ]
                    ),
                    ft.Container(
                        padding=15,
                        border_radius=8,
                        border=ft.border.all(1, "#DFDFDF"),
                        content=self.detalles_columna,
                        expand=True
                    ),
                ]
            )
        )
    
    # Método para construir/reconstruir la columna de detalles
    def construir_detalles_columna(self):
        return ft.Column(
            spacing=10,
            controls=[
                ft.Text("DETALLES DE CITA", size=16, weight=ft.FontWeight.BOLD, color="#444444"),
                ft.Divider(height=1, color="#DFDFDF"),
                DataRow(ft.icons.PERSON_OUTLINE, self.paciente_valor, size=13),
                DataRow(ft.icons.CALENDAR_TODAY, self.fecha_valor, size=13),
                DataRow(ft.icons.ACCESS_TIME, self.hora_valor, size=13)
            ]
        )

    def AbrirCalendario(self, e):
        self.page.open(
            ft.DatePicker(
                first_date=tiempoA(),
                last_date=mesS(),
                on_change=self.handle_date_change,
                on_dismiss=self.handle_dismissal,
            )
        )
        
    def abrirHorario(self, e):
        self.page.open(
            ft.TimePicker(
                confirm_text="CONFIRMAR",
                error_invalid_text="TIEMPO INVALIDO",
                help_text="ELIGE TU HORA",
                on_change=self.handle_time_change,
                on_dismiss=self.handle_dismissal,
                on_entry_mode_change=self.handle_entry_mode_change,
            )
        )
        
    def handle_time_change(self, e):
        self.hora_iso = e.control.value.strftime('%H:%M')
        hora = e.control.value.strftime('%H:%M %p')
        self.hora_valor = f"Hora: {hora}"
        nueva_columna = self.construir_detalles_columna()
        self.content.controls[3].content = nueva_columna
        self.update()

    def handle_dismissal(self, e):
        self.page.open(
            ft.SnackBar(
                content=ft.Text("opcion cerrado"),
                action="OK",
                action_color=ft.colors.GREEN,
                duration=1000,
            )
        )

    def handle_entry_mode_change(self, e):
        self.page.open(
            ft.SnackBar(
                content=ft.Text(""),
                action="OK",
                action_color=ft.colors.GREEN,
                duration=1000,
            )
        )
        
    def handle_date_change(self, e):
        # Actualizar el valor para la fecha
        self.fecha_iso = e.control.value.strftime('%Y-%m-%d')
        self.fecha_valor = f"Fecha: {self.fecha_iso}"
        
        nueva_columna = self.construir_detalles_columna()
        
        self.content.controls[3].content = nueva_columna
        
        self.update()
        
    def buscar_pacientes(self, e):
        
        self.id_paciente = self.texfiel_id.value
        
        nom = Medico.buscar_paciente_id(self.id_paciente)
        
        if nom != None:
            self.paciente_valor = f"Paciente: {nom[1]}"     
            nueva_columna = self.construir_detalles_columna() 
            self.content.controls[3].content = nueva_columna
        else:
            
            self.paciente_valor = "Paciente: ----"
            self.fecha_valor = "Fecha: ----"
            self.hora_valor = "Hora: ----"
            
            nueva_columna = self.construir_detalles_columna() 
            self.content.controls[3].content = nueva_columna
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Paciente no encontrado, se restablecen los campos."),
                    action="OK",
                    action_color=ft.colors.RED,
                    duration=1000,
                )
            )

        # Limpiar el campo de ID
        self.texfiel_id.value = ""        
        self.update()

    
    
    def limpiar_campos(self, e):
       # Reset all values to default
       
        Cita.nueva_cita(self.fecha_iso, self.hora_iso,self.id_paciente,self.medico_id)
                   
        self.paciente_valor = "Paciente: ----"
        self.fecha_valor = "Fecha: ----"
        self.hora_valor = "Hora: ----"
        self.texfiel_id.value = ""
        self.fecha_iso = None
        self.hora_iso = None
    # Rebuild the details column with cleared values
        nueva_columna = self.construir_detalles_columna()
        self.content.controls[3].content = nueva_columna
    
        self.update()
    
    
        
        self.page.open(
            ft.SnackBar(
                content=ft.Text("CITA GUARDADA CON EXITO"),
                action="OK",
                action_color=ft.colors.GREEN,
                duration=1000,
            )
        )
        self.page.update()