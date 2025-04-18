import flet as ft
from src.pages.login.loginView import loginView

def main(page: ft.Page):
    page.title = "Sistema de Gestión de Citas Médicas"
    page.window.maximized = True
    page.add(loginView())

ft.app(main)


