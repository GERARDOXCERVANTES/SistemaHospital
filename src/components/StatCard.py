import flet as ft

class StatCard(ft.Container):
    """Componente reutilizable para tarjetas de estadísticas"""
    def __init__(self, icon, title, value, width=200):
        super().__init__(
            expand=True,
            width=width,
            padding=15,
            border_radius=8,
            bgcolor=ft.colors.WHITE,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
                controls=[
                    ft.Row([
                        ft.Icon(icon, size=20, color="#4355B9"),
                        ft.Text(
                            title,
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color="#444444"
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(height=1, color="#DFDFDF"),
                    ft.Text(
                        value,
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="#4355B9"
                    )
                ]
            )
        ) 