import flet as ft

class StatusTag(ft.Container):
    """Componente reutilizable para etiquetas de estado"""
    def __init__(self, text, color):
        super().__init__(
            content=ft.Text(text, size=12, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            bgcolor=color,
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            border_radius=4
        ) 