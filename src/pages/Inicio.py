import flet as ft
from src.components.TextoIcono import TextoIcono  # Asegúrate de tener este archivo correctamente ubicado
from src.pages.Citas import iuCitas  # Asegúrate de tener este archivo correctamente ubicado

# Clase principal para la UI
class iuInicio(ft.Container):
    def __init__(self):
        super().__init__(
            padding=10,
            expand=True,
            content=ft.Column(
                spacing=20,
                controls=[
                    datosM(),  # Llamar al componente de datos médicos
                    citas()   #LLAMA LOS COMOPONENES DE LAS CITAS
                    
                ]
            )
        )
     # Creamos un contenedor vacío al que vamos a agregar contenido dinámicamente
        self.container_click = containerClick() 
        
    def on_click_icon(self ,seccion):
            if seccion == "cita":
                self.container_click.content = iuCitas()
                pass
            if seccion == "grafica":
                pass
            else:
                pass
            ft.Page.update()  # Actualiza la página para mostrar el contenido nuevo	

# Clase para los datos médicos
class datosM(ft.Card):
    def __init__(self):
        super().__init__(
            expand=True,
            elevation=5,
            color=ft.colors.WHITE,
            content=ft.Container(
                padding=20,
                expand=True,
                content=ft.Row(
                    spacing=20,
                    controls=[
                        ft.Card(
                            elevation=5,
                            height=100,
                            width=100,
                            color=ft.colors.WHITE,
                            content=ft.Container(
                                content=ft.Icon(
                                    ft.icons.PERSON_4_OUTLINED,
                                    size=50,
                                    color=ft.colors.BLUE
                                ),
                                alignment=ft.alignment.center
                            )
                        ),
                        ft.Card(
                            elevation=5,
                            color=ft.colors.WHITE,
                            content=ft.Container(
                                padding=20,
                                content=ft.Column(
                                    spacing=20,
                                    controls=[
                                        TextoIcono(
                                            'NOMBRE: ---',
                                            ft.icons.ABC_ROUNDED,
                                            ft.colors.BLUE
                                        ),
                                        TextoIcono(
                                            'ESPECIALIDAD: ---',
                                            ft.icons.ABC_ROUNDED,
                                            ft.colors.BLUE
                                        )
                                    ]
                                )
                            )
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls= [
                                ft.Card(
                                    expand= True,
                                    width= 200,
                                    elevation= 5,
                                    color= ft.colors.WHITE,
                                    content=ft.Container(
                                        alignment= ft.alignment.center,
                                        expand= True,
                                        padding= 20,
                                        content= ft.Column(
                                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                            spacing= 30,
                                            controls=[
                                                ft.Text(
                                                    "CITAS HOY",
                                                    size= 20,
                                                    weight = ft.FontWeight.BOLD,
                                                    text_align=  ft.TextAlign.CENTER,
                                                    ),TextoIcono(
                                                        "20",
                                                        ft.icons.DATE_RANGE_SHARP,
                                                        ft.colors.BLUE
                                                    )
                                            ]
                                        )
                                    )
                                    ),
                                ft.Divider(),
                                ft.Card(
                                    elevation= 5,
                                    width= 200,
                                    expand= True,
                                    color= ft.colors.WHITE,
                                    content= ft.Container(
                                        expand= True,
                                        padding= 20,
                                        content= ft.Column(
                                            spacing=20,
                                            
                                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                            controls= [
                                               ft.Text(
                                                    "PACIENTES",
                                                    size= 20,
                                                    weight = ft.FontWeight.BOLD,
                                                    text_align=  ft.TextAlign.CENTER,
                                                    ),TextoIcono(
                                                        "3",
                                                        ft.icons.PERSON_3_OUTLINED,
                                                        ft.colors.BLUE
                                                    ) 
                                            ]
                                        )
                                    )
                                )
                            ]
                        ),
                        ft.Card(
                            elevation= 5,
                            color= ft.colors.WHITE,
                            expand= True,
                            height= 400,
                            content= ft.Container(
                                expand= True,
                                padding= 10,
                                content= ft.Column(
                                    
                                    spacing= 10,
                                    controls= [
                                        ft.Row(
                                            vertical_alignment=ft.CrossAxisAlignment.START,  # Alinea los iconos hacia la parte superior
                                            alignment=ft.MainAxisAlignment.CENTER,  # Mantiene los iconos centrados horizontalmente
                                            spacing=20,
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.DATE_RANGE_ROUNDED,
                                                    icon_size=20,
                                                    icon_color=ft.colors.BLUE,
                                                    tooltip='AGENDAR CITAS',
                                                     on_click=lambda e: self.on_click_icon("cita")  # Llama al método on_click_icon con el argumento "cita"
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.DASHBOARD_CUSTOMIZE_ROUNDED,
                                                    icon_size=20,
                                                    icon_color=ft.colors.BLUE,
                                                    tooltip="Grafica"
                                                )
                                            ]
                                        ),ft.Divider()
                                        ,containerClick()
                                        
                                       
                                        
                                        
                                    ]
                                )
                            )
                        )
                    ]
                )
            )
        )
        


        
class containerClick(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
        )
        
        
class citas(ft.Card): #CLASE PARA OBSERVACION DE CITAS 
    def __init__(self):
        super().__init__(
            elevation= 5,
            expand= True,
            color= ft.colors.WHITE,
            content= ft.Container(
                    padding= 10,
                    expand= True,
                    content=  ft.Row(
                    spacing= 20,
                    controls= [
                        ft.Card(
                            elevation= 5,
                            color= ft.colors.WHITE,
                            expand= True,
                            content=ft.Container(
                            padding= 20,
                            expand= True,
                            content= ft.Column(
                                    spacing = 20,
                                    controls= [
                                    TextoIcono(
                                        "CITAS",
                                        ft.Icons.DATE_RANGE_ROUNDED,
                                        ft.Colors.BLUE
                                        ),
                                    ft.Column(
                                                expand= True,
                                                scroll=ft.ScrollMode.AUTO,
                                                horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
                                                spacing=0,
                                                controls=[
                                                    ft.DataTable(
                                                        expand= True,
                                                        columns=[
                                                            ft.DataColumn(label=ft.Text("ID CITA")),
                                                            ft.DataColumn(label=ft.Text("PACIENTE")),                                                    
                                                            ft.DataColumn(label=ft.Text("FECHA")),
                                                            ft.DataColumn(label=ft.Text("HORA")),
                                                            ft.DataColumn(label=ft.Text("ESTADO")),
                                                        ],
                                                        rows=[
                                                            ft.DataRow(
                                                                cells=[
                                                                    ft.DataCell(ft.Text(f" {i}")),
                                                                    ft.DataCell(ft.Text("KARLA JIMENEZ GARCIA")),
                                                                    ft.DataCell(ft.Text("2025-03-10")),
                                                                    ft.DataCell(ft.Text("10:00")),
                                                                    ft.DataCell(ft.Text("Pendiente")),
                                                                ]
                                                            )
                                                            for i in range(20)  
                                                        ],
                                                    )
                                                ]
                                                            
                                            )
                                    ]    
                                )
                                
                            )
                        )
                        ,ft.VerticalDivider()
                        ,ft.Card(
                            elevation= 5,
                            color= ft.colors.WHITE,
                            width= 400,
                            height= 450,
                            content= ft.Container(
                                padding= 60,
                                expand= True,
                                alignment= ft.alignment.center,
                                content= (
                                    ft.Column(
                                        alignment=ft.alignment.center,
                                        horizontal_alignment= ft.MainAxisAlignment.CENTER,
                                        spacing= 20,
                                        controls=[
                                            ft.ElevatedButton(
                                                height= 70,
                                                width= 160,
                                                text= "ACEPTAR",
                                                bgcolor= "#5E8E8D",
                                                color= ft.colors.WHITE
                                                
                                            ),ft.ElevatedButton(
                                                height= 70,
                                                width= 160,
                                                text= "CANCELAR",
                                                bgcolor= "#5E8E8D",
                                                color= ft.colors.WHITE
                                            )
                                        ]
                                    )
                                )
                            )
                        )
                    ]
                    
                )
            
            )
        )


