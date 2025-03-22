import flet as ft
import datetime as dt

# Clase principal para la interfaz de citas
class iuCitas(ft.Container):
    def __init__(self):  
        super().__init__(
            alignment= ft.alignment.center,
            expand=True,
            padding= 20,
            content=date()  # Llamar al componente de DatePicker
                
             
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
                        ft.TextField(
                            label= "HORA",
                            hint_text= "ej 10:20 AM"
                            ),
                        ft.TextField(
                            label="ID Paciente",
                            width=200
                            
                            ),
                        
                          ]
                      ),ft.VerticalDivider(),
                      ft.Column(
                          spacing= 20,
                          controls= [
                              #BOTON PARA ABRIR CALENDARIO
                        ft.ElevatedButton(
                            "SELECCIONAR FECHA",
                            icon=ft.Icons.CALENDAR_MONTH,
                            on_click=self.AbrirCalendario,
                            color= ft.colors.WHITE,
                            bgcolor= "#5E8E8D",
                            height= 70,
                            width= 180,
                        ),
                        ft.ElevatedButton(
                            "AGENDAR CITA",
                            icon= ft.Icons.ADD,
                            width= 180,
                            height= 70,
                            bgcolor= "#5E8E8D",
                            color= ft.Colors.WHITE
                        )
                        
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

    # Método para manejar el cambio de fecha
    def handle_date_change(self, e):
        # Mostrar la fecha seleccionada en un mensaje
        X = e.control.value.strftime('%Y-%m-%d')
        return X
        
        
    def handle_dismissal(self, e):
        print("DatePicker dismissed")



