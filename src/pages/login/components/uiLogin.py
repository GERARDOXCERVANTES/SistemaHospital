import flet as ft
from src.components.iconLogo import iconLogin
from src.models.user import User
from src.models.Indentificador import Identificador

class uiLogin(ft.Container):
    def __init__(self):
        self.usuario = ft.TextField(
            hint_text="Usuario",
            width=300,
            height=50,
            border='underline',
            border_radius=20,
            prefix_icon=ft.Icon(ft.icons.PERSON, ft.colors.BLUE),
            bgcolor=ft.colors.GREY_300,
        )
        self.contrasena = ft.TextField(
            hint_text="Contraseña",
            width=300,
            height=100,
            border='underline',
            border_radius=20,
            password=True,
            prefix_icon=ft.Icon(ft.icons.LOCK, ft.colors.BLUE),
            bgcolor=ft.colors.GREY_300,
        )

        super().__init__(
            border_radius=30,
            width=400,
            height=500,
            padding=20,
            bgcolor=ft.Colors.WHITE70,
            alignment=ft.alignment.center,
            expand=True,
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=ft.colors.BLACK26,
                offset=ft.Offset(5, 5),
            ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    iconLogin(),
                    ft.Text(
                        'LOGIN',
                        color="#111184",
                        size=18,
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        "Inicia sesión para continuar",
                        size=20,
                        weight=ft.FontWeight.W_400,
                    ),
                    ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                    self.usuario,
                    self.contrasena,
                    botonPersonalizado(
                        'INGRESAR',
                        ft.icons.TRANSIT_ENTEREXIT_SHARP,
                        ft.colors.WHITE,
                        "#111184",
                        ft.colors.WHITE,
                        on_click=self.on_click
                    )
                ],
            ),
        )

    def on_click(self, e):
        try:
            usuario = self.usuario.value.strip()
            contrasena = self.contrasena.value.strip()
            if User.get_user(usuario, contrasena) != None:#verifica si el usuario existe
                autentificacion, rol  = User.get_user(usuario, contrasena)
                Identificador.identificar_rol(autentificacion, rol,usuario,e.page)        
                e.page.update()
            else:
                return
        except Exception as e:
            print(f"Error en la autenticación: {e}")
        finally:
            self.usuario.value = ""
            self.contrasena.value = ""
                      
            
    
def botonPersonalizado(text, icon, color, bgcolor, iconC, on_click=None):
    return ft.ElevatedButton(
        on_click=on_click,
        height=50,
        elevation=5,
        text=text,
        icon=icon,
        icon_color=iconC,
        style=ft.ButtonStyle(
            color=color,
            bgcolor=bgcolor,
            shape=ft.RoundedRectangleBorder(radius=8),
        )
    )
