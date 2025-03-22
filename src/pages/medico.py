import flet as ft
from src.pages.Paciente import UiPaciente
from src.pages.Inicio import iuInicio
class Navegacion(ft.Container):
    def __init__(self, on_menu_click):
        super().__init__(
            expand=True,
            padding= 0,
            margin=10,
            content=ft.Column(
                expand= True,
                horizontal_alignment= ft.CrossAxisAlignment.START,
                alignment= ft.MainAxisAlignment.START,
                spacing=10,
                controls=[
                     ft.Container(
                        margin=0,    
                        content = (
                              ft.Container(
                                alignment= ft.alignment.center,
                                content= ft.Column(
                                alignment= ft.MainAxisAlignment.CENTER,
                                controls= [
                                iconLogin()       
                            ]
                                )
                              )
                        )
                    ),
                    ft.Container(
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        content = (
                            ft.Row(
                                vertical_alignment  =ft.CrossAxisAlignment.CENTER,
                                spacing= 20,
                                controls= [
                                    ft.Icon(
                                        ft.icons.MENU,
                                        color= ft.colors.WHITE,
                                        size= 16
                                    ),
                                    ft.Text(
                                    "MENU", 
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.BOLD,
                                    size= 16,
                                    color=ft.colors.WHITE
                                    
                                ),
                                ]
                                
                            )
                        )   
                    ),
                    
                    ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.HOME,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "INICIO",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("dashboard"),
                    ),
                   ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.PERSON_2,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "PACIENTES",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("pacientes"),
                    ),
                     ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.CALENDAR_MONTH_OUTLINED,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "AGENDA / CITAS",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("agenda"),
                    ),
                    ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.MEDICAL_INFORMATION_ROUNDED,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "SESIONES",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                    
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("sesiones"),
                    ),
                    ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.PAGEVIEW,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "HISTORIALES CLINICO",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                    
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("historial"),
                    )
                  
                  
                ],
            )
        )
class iconLogin(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            width=100,
            height=100,
            border_radius=100,                    # Radio de la esquina
            clip_behavior=ft.ClipBehavior.HARD_EDGE,  # Recorta según el radio
            content=ft.Image(
                src="src/assets/logo.jpg",
                fit=ft.ImageFit.COVER              # Aseguras que ocupe todo el contenedor
            ),
             shadow=ft.BoxShadow(
                spread_radius=5,  # Difusión
                blur_radius=15,  # Desenfoque
                color=ft.colors.BLACK26,  # Color de la sombra
                offset=ft.Offset(5, 5),  # Posición de la sombra
            ),
            
            
        )
        

class Seccion(ft.Container):
    def __init__(self, on_menu_click):
        super().__init__(
            width=250,
            height=1000,
            padding=0, 
            margin=0,
            bgcolor="#111184",
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=ft.colors.BLACK26,
                offset=ft.Offset(5, 5)
            ),
            content=Navegacion(on_menu_click=on_menu_click),
            
        )
        
class Citas(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
            bgcolor= ft.colors.WHITE,

            border_radius=20,
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=ft.colors.BLACK26,
                offset=ft.Offset(5, 5)
            ),
            
            content=ft.Column(
                expand= True,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
                spacing=0,
                controls=[
                    ft.DataTable(
                        expand= True,
                        columns=[
                            ft.DataColumn(label=ft.Text("ID CITA")),
                            ft.DataColumn(label=ft.Text("FECHA")),
                            ft.DataColumn(label=ft.Text("HORA")),
                            ft.DataColumn(label=ft.Text("ESTADO")),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(f" {i}")),
                                    ft.DataCell(ft.Text("2025-03-10")),
                                    ft.DataCell(ft.Text("10:00")),
                                    ft.DataCell(ft.Text("Pendiente")),
                                ]
                            )
                            for i in range(20)  
                        ],
                    )
                ]
            )
        )
        
        
        
        

class OpcionesC(ft.Container):
    def __init__(self):
        super().__init__(
            width=300,
            padding= 40,
            height=500,
            border_radius=20,
            bgcolor= "#3A6766",
            alignment= ft.alignment.center,
            content=ft.Column(
                alignment= ft.alignment.center,
                spacing= 30,
                controls = [
                    ft.ElevatedButton(
                        text="ACEPTAR",
                        width= 150,
                        height=45,
                        bgcolor= "#5E8E8D",
                        color= ft.colors.WHITE
                    ),
                    ft.ElevatedButton(
                        text= 'CANCELAR',
                        width= 150,
                        height= 45,
                        bgcolor= "#5E8E8D",
                        color= ft.colors.WHITE
                    )
                ]
            )
        )
        
class containerP(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
            width= 100,
            height= 1000,
            padding= 30,
            margin= 20,
            bgcolor= "#D3D3D3",
            border_radius= 50,
            content = iuInicio()
            
        )
    
    










def Main(page: ft.Page):
    page.title = "SISTEMA DE CONTROL DEL MEDICO"
    page.bgcolor = "#FAF8F7"
    page.padding = 0
    page.margin = 0

    # Contenedor para mostrar el contenido principal al lado de la barra
    contenedorPrincipal = containerP()
    
  
    # Función que manejará los clics de los botones del menú
    def on_menu_click(seccion_id : str ):

        if seccion_id == "dashboard":
            contenedorPrincipal.content = iuInicio()
        elif seccion_id == "pacientes":
            contenedorPrincipal.content = UiPaciente()
            ##ft.Column(control = [])
        elif seccion_id == "agenda":
            contenedorPrincipal.content = ft.Row(
                controls=[
                    Citas(),
                    OpcionesC()
                    ]
                )
                
                       
        elif seccion_id == "sesiones":
            contenedorPrincipal.content = ft.Text("Sesiones de Diálisis", size=20)
        elif seccion_id == "historial":
            contenedorPrincipal.content = ft.Text("historial clinico", size=20)
        else:
            contenedorPrincipal.content = ft.Text(f"Sección: {seccion_id}", size=20)
        page.update()

    
    

    row = ft.Row(
        controls=[
            Seccion(on_menu_click=on_menu_click),
            contenedorPrincipal
        ],
        expand=True
    )
    page.add(row)
    page.update()




ft.app(target=Main)
