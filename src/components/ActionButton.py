import flet as ft

class ActionButton(ft.ElevatedButton):
    """Componente reutilizable para botones de acción"""
    def __init__(self, text, icon, on_click=None, bgcolor="#4355B9"):
        super().__init__(
            content=ft.Row([
                ft.Icon(icon, color=ft.colors.WHITE),
                ft.Text(text, size=14, weight=ft.FontWeight.BOLD)
            ]),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                bgcolor=bgcolor,
                color=ft.colors.WHITE
            ),
            height=50,
            width=160,
            on_click=on_click
        ) 