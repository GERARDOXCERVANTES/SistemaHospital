import flet as ft

class SectionHeader(ft.Column):
    """Componente reutilizable para encabezados de sección"""
    def __init__(self, icon, title, size=18):
        super().__init__(
            controls=[
                ft.Row([
                    ft.Icon(icon, size=24, color="#4355B9"),
                    ft.Text(
                        title,
                        weight=ft.FontWeight.BOLD,
                        size=size,
                        color="#444444"
                    )
                ]),
                ft.Divider(height=1, color="#DFDFDF")
            ],
            spacing=5
        ) 