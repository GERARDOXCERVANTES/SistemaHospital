import flet as ft
from src.components.iconLogo import iconLogin 
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
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing= 20,
                controls=[# Lista de elementos
                    iconLogin(),
                        ft.Text(
                            'LOGIN',
                            color= "#111184",
                            size= 18,
                            weight= ft.FontWeight.BOLD 
                        ),
                        ft.Text(
                            "inicia sesion para continuar",
                            size=20,
                            weight=ft.FontWeight.W_400,
                        ),
                    ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                    
                    ft.TextField(
                        hint_text ="Usuario",
                        width=300,
                        height =50,
                        border = 'underline',
                        border_radius= 20,
                            prefix_icon= ft.Icon(ft.icons.PERSON,ft.colors.BLUE),
                            bgcolor=ft.colors.GREY_300,
                            
                        ),


                    
                    ft.TextField(
                            hint_text ="Contraseña",
                            width=300,
                            height =100,
                            border = 'underline',
                            border_radius=20,
                            password= True,
                            prefix_icon= ft.Icon(ft.icons.LOCK ,ft.colors.BLUE),
                            bgcolor= ft.colors.GREY_300
                        ),
                    botonPersonalizado(
                        'INGRESAR',
                        ft.icons.TRANSIT_ENTEREXIT_SHARP,
                        ft.colors.WHITE,
                        "#111184",
                        ft.colors.WHITE
                    )
                    
                ],
            ),
        )
        
def botonPersonalizado(text,icon,color,bgcolor,iconC):
    return ft.ElevatedButton(
        height= 50,
        elevation= 5,
        text= text,
        icon= icon,
        icon_color= iconC,
        style= ft.ButtonStyle(
            color= color,
            bgcolor= bgcolor,
            shape=ft.RoundedRectangleBorder(radius=8),

            
        )
        
    )
    
        
        

