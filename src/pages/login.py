import flet as ft
from src.components.button import buttonP

class uiLogin(ft.Container):
    def __init__(self):
        super().__init__(
            border_radius=30,
            width=400,
            height=500,
            padding= 20,
            bgcolor=ft.Colors.WHITE70,  # Color de fondo
            alignment=ft.alignment.center,
            expand=True,
            shadow=ft.BoxShadow(
                spread_radius=5,  # Difusión
                blur_radius=15,  # Desenfoque
                color=ft.colors.BLACK26,  # Color de la sombra
                offset=ft.Offset(5, 5),  # Posición de la sombra
                
            ),
            
            
            
            content=ft.Column(
                controls=[# Lista de elementos
                    ft.Container(
                        content = iconLogin(),
                        alignment=ft.alignment.center
                        ), 
                    ft.Container(
                        content=ft.Text(
                            "LOGIN",
                            size=20,
                            color= '#000080',  # Un color que combine con el fondo
                            weight=ft.FontWeight.BOLD,
                        ),
                        alignment=ft.alignment.center
                    ),ft.Container(
                        content=ft.Text(
                            "inicia sesion para continuar",
                            size=20,
                            weight=ft.FontWeight.W_100,
                            
                            
                        ),
                        alignment=ft.alignment.center
                    ),
                    
                    ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                    
                    ft.Container(
                        content=ft.TextField(
                            hint_text ="Usuario",
                            width=300,
                            height =50,
                            border = 'underline',
                            border_radius= 20,
                            prefix_icon= ft.Icon(ft.icons.PERSON,ft.colors.BLUE),
                            bgcolor=ft.colors.GREY_300,
                            
                        ),

                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        content=ft.TextField(
                            hint_text ="Contraseña",
                            width=300,
                            height =100,
                            border = 'underline',
                            border_radius=20,
                            password= True,
                            prefix_icon= ft.Icon(ft.icons.LOCK ,ft.colors.BLUE),
                            bgcolor= ft.colors.GREY_300
                        ),
                        alignment=ft.alignment.center
                    ),
                    ft.Container(
                        buttonP(
                            'INGRESAR'
                            ),
                        alignment=ft.alignment.center
                    )
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        )
class background(ft.Image):
    def __init__(self):
        super().__init__(
            expand=True,
            src="src/assets/fondo.jpg",
            fit=ft.ImageFit.COVER,  # Ajusta la imagen al tamaño de la pantalla

                
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

       

def Main(page: ft.Page):#metodo principal 
    page.window_full_screen = True
    page.padding = 0
    page.margin = 0
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    sr = ft.Stack(
        controls=[
            ft.Container(
                content=background(),
                width=page.width,
                height=page.height
                ),  # Fondo ocupa toda la pantalla
            ft.Container(
                content=uiLogin(),
                alignment=ft.alignment.center
                ) 
        ],
        width=page.width,
        height=page.height
    )
    page.add(sr)
    page.title = 'LOGIN'

ft.app(target=Main)
