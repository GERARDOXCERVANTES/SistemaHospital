import flet as ft
import datetime as dt
from src.components.ActionButton import ActionButton
from src.components.TextfieldsIcons import vitalField

# Clase principal para la interfaz de citas
class iuCitas(ft.Container):
    def __init__(self):  
        super().__init__(
            alignment= ft.alignment.center,
            expand=True,
            padding= 20,
            content=date()  
                
             
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


# Clase para el DatePicker dentro de un Card
class date(ft.Container):
    def __init__(self):  
        super().__init__(
            expand=True,
            padding= 20,
            content= ft.Row(
                   alignment=ft.MainAxisAlignment.START,  # Mantiene los iconos centrados horizontalmente
                    spacing=40,
                    controls=[
                      ft.Column(
                          spacing= 20,
                          controls= [  

                            vitalField("ID Paciente",ft.icons.PERSON_OUTLINE,"",""),
                        
                          ]
                      ),ft.VerticalDivider(),
                      ft.Column(
                          spacing= 20,
                          controls= [
                              #BOTON PARA ABRIR CALENDARIO
                        ActionButton("FECHA", ft.icons.CALENDAR_MONTH,self.AbrirCalendario),
                        ActionButton("HORA", ft.icons.TIMELAPSE,self.abrirHorario),
                        ActionButton("AGENDAR", ft.icons.ADD),


                        
                          ]
                      )
                    ]
                )
            )
        

    def AbrirCalendario(self, e):
        
        self.page.open(
            ft.DatePicker(
                first_date=tiempoA(),  # Llamamos a la función y pasamos el valor de la fecha
                last_date=mesS(),  # Llamamos a la función y pasamos el valor de la fecha
                on_change=self.handle_date_change,
                on_dismiss=self.handle_dismissal,
            )
        )
        
        
        
    def abrirHorario(self,e):
     self.page.open(
            ft.TimePicker(
                confirm_text="Confirm",
                error_invalid_text="Time out of range",
                help_text="Pick your time slot",
                on_change=self.handle_change,
                on_dismiss=self.handle_dismissal,
                on_entry_mode_change=self.handle_entry_mode_change,
            )
        )
        
        
    def handle_change(self,e):
        print(f"TimePicker change: ")

    def handle_dismissal(self,e):
        print(f"TimePicker dismissed: ")

    def handle_entry_mode_change(self,e):
        print(f"TimePicker Entry mode changed t")
        
        
        
        
    # Método para manejar el cambio de fecha
    def handle_date_change(self, e):
        # Mostrar la fecha seleccionada en un mensaje
        X = e.control.value.strftime('%Y-%m-%d')
        return X
        
        
    def handle_dismissal(self, e):
        print("DatePicker dismissed")



