import flet as ft


class UiBarraNavegacion(ft.Container):
    def __init__(self,on_menu_click):
        super().__init__(
            
        )
        
        
        
class Navegacion(ft.Container):
    def __init__(self, on_menu_click):
        super().__init__(
            expand=True,
            padding= 0,
            margin=10,
            content=ft.Column(
                expand= True,
                horizontal_alignment= ft.CrossAxisAlignment.START,
                alignment= ft.MainAxisAlignment.START,
                spacing=10,
                controls=[
                    ft.Container(
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        content = (
                            ft.Row(
                                vertical_alignment  =ft.CrossAxisAlignment.CENTER,
                                spacing= 20,
                                controls= [
                                    ft.Icon(
                                        ft.icons.MENU,
                                        color= ft.colors.WHITE,
                                        size= 16
                                    ),
                                    ft.Text(
                                    "MENU", 
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.BOLD,
                                    size= 16,
                                    color=ft.colors.WHITE
                                    
                                ),
                                ]
                                
                            )
                        )   
                    ),
                    
                    ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.HOME,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "INICIO",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("dashboard"),
                    ),
                   ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.PERSON_2,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "PACIENTES",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("pacientes"),
                    ),
                     ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.CALENDAR_MONTH_OUTLINED,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "AGENDA / CITAS",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("agenda"),
                    ),
                    ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.MEDICAL_INFORMATION_ROUNDED,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "SESIONES",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                    
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("sesiones"),
                    ),
                    ft.Container(
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Icon(
                                    ft.icons.PAGEVIEW,
                                    color=ft.colors.WHITE,
                                    size=24
                                ),
                                ft.Text(
                                    "HISTORIALES CLINICO",
                                    text_align=ft.TextAlign.START,
                                    weight=ft.FontWeight.W_600,
                                    color=ft.colors.WHITE
                                    
                                )
                            ]
                        ),
                        margin=0,
                        padding=10,
                        width=250,
                        height=50,
                        ink=True,
                        on_click=lambda e: on_menu_click("historial"),
                    )
                  
                  
                ],
            )
        )


class Seccion(ft.Container):
    def __init__(self, on_menu_click):
        super().__init__(
            width=250,
            height=1000,
            padding=0, 
            margin=0,
            bgcolor="#111184",
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=ft.colors.BLACK26,
                offset=ft.Offset(5, 5)
            ),
            content=Navegacion(on_menu_click=on_menu_click),
    )