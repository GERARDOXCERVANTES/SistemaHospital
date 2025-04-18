import flet as ft
from src.pages.login.components.fondo import fondo
from src.pages.login.components.uiLogin import uiLogin

        
        
            
def loginView():# Here build the login page view with a stack
    return ft.Container(
        alignment=ft.alignment.center,
        content= ft.Stack(
            alignment=ft.alignment.center,
            controls=[
                fondo(),
                uiLogin()
            ]
        )
    )
                                
