import flet as ft

class DataRow(ft.Row):
    """Componente reutilizable para filas de datos con icono + texto"""
    def __init__(self, icon, text, size=14, icon_color="#4355B9"):
        super().__init__(
            controls=[
                ft.Icon(icon, size=20, color=icon_color),
                ft.Text(text, size=size, weight=ft.FontWeight.BOLD, color="#444444")
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ) 