import flet as ft
from src.pages.Registros.añadir_paciente import  AddPaciente
from src.components.iconLogo import iconLogin
from src.pages.Registros.agendar_cita import AgendarCita
from src.pages.Registros.anadir_medico import AddMedico


class Navegacion(ft.Container):
    def __init__(self,on_menu_click,on_toggle_sidebar):
        self.expanded = True
        self.text_controls = []
        
        self.nav_items = [
            {
                "icon": ft.icons.PERSON_2_OUTLINED,
                "text": "PACIENTE",
                "id": "paciente"
            },
            {
                "icon": ft.icons.MEDICAL_INFORMATION,
                "text": "MEDICOS",
                "id": "medico"
            },
            {
                "icon": ft.icons.DATE_RANGE,
                "text": "CITAS",
                "id": "cita"
            }
        ]
        self.nav_rows = []
        
        for item in self.nav_items:
            text_control = ft.Text(
                item["text"],
                text_align=ft.TextAlign.START,
                weight=ft.FontWeight.W_600,
                color=ft.colors.WHITE,
                visible=self.expanded
            )
            self.text_controls.append(text_control)
            
            nav_row = ft.Container(
                content=ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        ft.Icon(
                            item["icon"],
                            color=ft.colors.WHITE,
                            size=24
                        ),
                        text_control
                    ]
                ),
                margin=0,
                padding=10,
                width=250 if self.expanded else 70,
                height=50,
                ink=True,
                on_click=lambda e, id=item["id"]: on_menu_click(id),
            )
            self.nav_rows.append(nav_row)
        
        # Create the header with logo and title
        self.hospital_text = ft.Text(
            "HOSPITAL",
            size=15,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.WHITE,
            animate_opacity=200,
            opacity=1,
            visible=self.expanded
        )
        
        self.hemodialisis_text = ft.Text(
            'HEMODILISIS',
            size=13,
            weight=ft.FontWeight.W_400,
            color=ft.colors.WHITE54,
            animate_opacity=200,
            opacity=1,
            visible=self.expanded
        )
        
        self.header_column = ft.Column(
            spacing=1,
            controls=[
                self.hospital_text,
                self.hemodialisis_text
            ]
        )
        
        super().__init__(
            expand=True,
            padding=0,
            margin=10,
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT),
            content=ft.Column(
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
                controls=[
                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.Container(
                                margin=0,    
                                alignment=ft.alignment.center,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        iconLogin()       
                                    ]
                                )       
                            ),
                            self.header_column
                        ]
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.IconButton(
                            icon_size=24,
                            icon=ft.icons.MENU,
                            icon_color=ft.colors.WHITE,
                            on_click=lambda e: self.toggle_sidebar(on_toggle_sidebar)
                        ),
                    ),
                    *self.nav_rows
                ],
            )
        )
    
    def toggle_sidebar(self, on_toggle_sidebar):
        self.expanded = not self.expanded
        
        for text in self.text_controls:
            text.visible = self.expanded
        
        self.hospital_text.visible = self.expanded
        self.hemodialisis_text.visible = self.expanded
        
        for row in self.nav_rows:
            row.width = 250 if self.expanded else 70
        
        on_toggle_sidebar(self.expanded)
        
        self.update()

class Seccion(ft.Container):
    def __init__(self, on_menu_click):
        self.expanded = True
        def on_toggle_sidebar(expanded):
            self.expanded = expanded
            self.width = 250 if expanded else 80
            self.update()
        
        self.navegacion = Navegacion(on_menu_click=on_menu_click, on_toggle_sidebar=on_toggle_sidebar)
        
        super().__init__(
            width=250,
            height=1000,
            padding=0, 
            margin=0,
            border_radius=10,
            bgcolor="#111184",
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT),
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color=ft.colors.BLACK26,
                offset=ft.Offset(5, 5)
            ),
            content=self.navegacion,
        )

class containerP(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            width=100,
            height=1000,
            padding=30,
            margin=20,
            bgcolor="#D3D3D3",
            border_radius=50,
            content= AddPaciente()
        )
        

def recepcionista_View(page: ft.Page):
    page.title = "SISTEMA DE CONTROL DEL MEDICO"
    page.bgcolor = "#FAF8F7"
    page.padding = 0
    page.margin = 0
    page.window.maximized = True

    contenedorPrincipal = containerP()

    def on_menu_click(seccion_id: str):
        if seccion_id == "medico":
            contenedorPrincipal.content = AddMedico()
        elif seccion_id == "paciente":
            contenedorPrincipal.content = AddPaciente()
        elif seccion_id == "cita":
            contenedorPrincipal.content =  AgendarCita()
        else:
            contenedorPrincipal.content = ft.Text(f"Sección: {seccion_id}", size=20)
        page.update()

    sidebar = Seccion(on_menu_click=on_menu_click)
    
    row = ft.Row(
        controls=[
            sidebar,
            contenedorPrincipal
        ],
        expand=True
    )
    return row



