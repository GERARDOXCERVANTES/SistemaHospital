import flet as ft

class UiPaciente(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            content=ft.Row(
                controls=[
                    ft.Card(
                        expand=True,
                        height=1000,
                        color=ft.colors.WHITE,
                        elevation=5,
                        content=ft.Container(
                            padding=20,
                            content=ft.Column(
                                spacing=20,
                                controls=[
                                    ft.Row(
                                        spacing=20,
                                        controls=[
                                            ft.Card(
                                                height=100,
                                                width=100,
                                                color=ft.colors.WHITE,
                                                elevation=5,
                                                content=ft.Container(
                                                    content=ft.Icon(ft.icons.PERSON_4_OUTLINED, size=50, color=ft.colors.BLUE),
                                                    alignment=ft.alignment.center
                                                )
                                            ),ft.Card(
                                                expand= True,
                                                height= 150,
                                                color= ft.colors.WHITE,
                                                elevation= 5,
                                                content=ft.Container(
                                                    padding= 30,
                                                    content=ft.Row(
                                                    vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                                    alignment= ft.MainAxisAlignment.START,
                                                    spacing= 60,
                                                    controls=[
                                                        ft.Row(
                                                            spacing= 10,
                                                            controls= [
                                                                ft.Icon(
                                                                    ft.icons.BADGE_ROUNDED,
                                                                    size= 16
                                                                ),
                                                                ft.Text(
                                                                    'ID: ---',
                                                                    size= 14,
                                                                    color= ft.Colors.BLACK,
                                                                    weight= ft.FontWeight.W_600
                                                                )
                                                            ]
                                                            ),                                 
                                                            ft.Column(
                                                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                            alignment= ft.MainAxisAlignment.CENTER,
                                                            spacing= 24,
                                                            controls= [
                                                                ft.Row(
                                                                    spacing= 10,
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.PERSON_3_SHARP,
                                                                            size= 16
                                                                            
                                                                        ), ft.Text(
                                                                            'NOMBRE: --',
                                                                            size= 14,
                                                                            color= ft.Colors.BLACK,
                                                                            weight= ft.FontWeight.W_600
                                                                            ),
                                                                    ]
                                                                    ),ft.Row(
                                                                        spacing= 10,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.Icons.CAKE_OUTLINED,
                                                                                size= 16
                                                                                
                                                                            ),
                                                                            ft.Text(
                                                                                'EDAD: ---',
                                                                                size= 14,
                                                                                color= ft.Colors.BLACK,
                                                                                weight= ft.FontWeight.W_600
                                                                            ),
                                                                        ]
                                                                    )    
                                                                
                                                            ]
                                                        ),ft.Column(
                                                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                            alignment= ft.MainAxisAlignment.CENTER,
                                                            spacing= 20,
                                                            controls= [
                                                                ft.Row(
                                                                        spacing= 10,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.Icons.WC_OUTLINED,
                                                                                size= 16
                                                                                
                                                                            ),
                                                                            ft.Text(
                                                                                'SEXO: ---',
                                                                                size= 14,
                                                                                color= ft.Colors.BLACK,
                                                                                weight= ft.FontWeight.W_600
                                                                            ),
                                                                        ]
                                                                    ),    
                                                                 ft.Row(
                                                                        spacing= 10,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.Icons.BLOODTYPE_OUTLINED,
                                                                                size= 16
                                                                                
                                                                            ),
                                                                            ft.Text(
                                                                                'TIPO DE SANGRE: ---',
                                                                                size= 14,
                                                                                color= ft.Colors.BLACK,
                                                                                weight= ft.FontWeight.W_600
                                                                            ),
                                                                        ]
                                                                    ),    
                                                            ]
                                                        )

                                                    ]                                                    
                                                )
                                                )

                                            )
                                        ]
                                    ),
                                    #carta para alergias y condiciones medicas
                                    ft.Card(
                                        elevation= 5,
                                        color= ft.colors.WHITE,
                                        height= 200,
                                        width= 800,
                                        content= ft.Container(
                                            padding= 20,
                                            content=ft.Row(
                                                spacing= 20,
                                                controls=[
                                                   ft.Column(
                                                       expand= True,
                                                       spacing= 20,
                                                       controls=[
                                                           ft.Row(
                                                               spacing= 20,
                                                               controls=[
                                                                   ft.Icon(
                                                                       ft.icons.MEDICAL_INFORMATION_OUTLINED,
                                                                       size= 24,

                                                                   ),
                                                                   ft.Text(
                                                                       'ALERGIAS',
                                                                       color= "#111184",
                                                                       size= 18,
                                                                       weight= ft.FontWeight.BOLD

                                                                   )
                                                                   
                                                                   
                                                                   
                                                               ]
                                                           ),
                                                           ft.ListView(
                                                                expand= True,
                                                                spacing= 20,
                                                                controls=[
                                                                    ft.Text(f'ALERGIA {i}')for  i in range (1,11)
                                                                ]
                                                           )
                                                       ]
                                                   ),
                
                                                    ft.Column(
                                                        expand= True,
                                                        spacing= 20,
                                                        controls= [
                                                            ft.Row(
                                                                spacing= 20,
                                                                controls= [
                                                                    ft.Icon(
                                                                        ft.icons.MEDICATION_SHARP,
                                                                        size= 24
                                                                    ),ft.Text(
                                                                        'CONDICIONES PREVIA',
                                                                        color= "#111184",
                                                                        size= 18,
                                                                        weight= ft.FontWeight.BOLD
                                                                    )
                                                                    ]
                                                                ),
                                                            ft.ListView( 
                                                                expand= True,
                                                                spacing= 20,
                                                                controls=[
                                                                    ft.Text(f'CONDICION  {i}')for  i in range (1,11)
                                                                ]
                                                            )
                                                        ]
                                                                    
                                                    ) 
                                                   
                                                ]
                                            )
                                        )
                                        
                                        
                                    ),
                                    #TERCERA TARJETA  DE LA COLUMNA PARA IDENTIFICAR DATOS DE SESIONES ANTERIORES
                                    ft.Card(
                                        expand=True,
                                        width= 800,
                                        elevation= 5,
                                        color= ft.colors.WHITE,
                                        content= ft.Container(
                                            padding= 20,
                                            content= ft.Column(
                                                spacing= 10,
                                                controls=[
                                                    ft.Row(
                                                        spacing= 20,
                                                        controls= [
                                                            ft.Icon(
                                                                ft.icons.LIST_ALT,
                                                                size= 16
                                                            ),ft.Text(
                                                                'SESIONES DE HEMODIALIS',
                                                                size= 16,
                                                                color= '#111184',
                                                                weight= ft.FontWeight.BOLD
                                                            )
                                                        ]
                                                    ),ft.Column(
                                                        expand= True,
                                                        scroll=ft.ScrollMode.AUTO,
                                                        horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
                                                        spacing=0,
                                                        controls=[
                                                            ft.DataTable(
                                                                column_spacing= 20,
                                                                expand= True,
                                                                columns= [
                                                                    ft.DataColumn(label= ft.Text('FECHA',text_align= ft.TextAlign.CENTER)),
                                                                    ft.DataColumn(label= ft.Text('DURACION',text_align= ft.TextAlign.CENTER)),
                                                                    ft.DataColumn(label= ft.Text('PESO PRE',text_align= ft.TextAlign.CENTER)),
                                                                    ft.DataColumn(label= ft.Text('PESO POST',text_align= ft.TextAlign.CENTER)),
                                                                    ft.DataColumn(label= ft.Text('ULT TOTAL',text_align= ft.TextAlign.CENTER)),
                                                                ],
                                                                rows=[
                                                                    ft.DataRow(
                                                                        cells=[
                                                                            ft.DataCell(ft.Text("2025-03-10",text_align= ft.TextAlign.CENTER)),
                                                                            ft.DataCell(ft.Text("5 MINUTOS",text_align= ft.TextAlign.CENTER)),
                                                                            ft.DataCell(ft.Text("72.00 KG",text_align= ft.TextAlign.CENTER)),
                                                                            ft.DataCell(ft.Text("70.00 KG",text_align= ft.TextAlign.CENTER)),
                                                                            ft.DataCell(ft.Text("2.0 L",text_align= ft.TextAlign.CENTER)),
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
                                ]
                            )
                        )
                    ),
                    # Segunda tarjeta del segundo row: buscador o campos adicionales
                    ft.Card(
                        expand=True,
                        height=1000,
                        color=ft.colors.WHITE,
                        elevation=5,
                        content= ft.Container(
                            padding= 20,
                            content= ft.Column(
                                spacing= 20,
                                controls= [
                                    ft.Card(
                                        elevation= 5,
                                        height= 150,
                                        width= 800,
                                        color= ft.colors.WHITE,
                                        content= ft.Container(
                                            padding= 40,
                                            expand= True,
                                            content= ft.Row(
                                                expand= True,
                                                spacing= 30,
                                                controls=[
                                                    ft.TextField(
                                                        hint_text= 'ID USUARIO',
                                                        icon= ft.icons.SEARCH,
                                                        height= 100,
                                                        width= 200,
                                                        text_size= 16,
                                                        border = 'underline'
                                                    ),ft.ElevatedButton(
                                                        width=  170,
                                                        height= 80,
                                                        text= 'BUSCAR',
                                                        color= ft.colors.WHITE,
                                                        bgcolor='#3A6766'
                                                    ),ft.Icon(
                                                        ft.icons.HEALTH_AND_SAFETY_OUTLINED,
                                                        expand= True,
                                                        size= 50
                                                    )
                                                    
                                                ]
                                            )
                                        )

                                    ),ft.Card(
                                        expand= True,
                                        width= 800,
                                        color= ft.colors.WHITE,
                                        elevation= 5,
                                        content= ft.Container(
                                            padding= 0,
                                            expand= True,
                                            content=ft.Column(
                                                spacing= 10,
                                                controls= [
                                                    ft.Container(
                                                        padding=20,
                                                        expand=True,
                                                        content=ft.Column(
                                                            spacing=20,
                                                            controls=[
                                                                ft.Row(
                                                                    spacing=20,
                                                                    controls=[
                                                                        ft.Icon(ft.icons.DATE_RANGE_SHARP, size=20),
                                                                        ft.Text('CITAS ', color='#111184', size=16, weight=ft.FontWeight.BOLD)
                                                                    ]
                                                                ),
                                                                ft.Column(
                                                                    expand=True,
                                                                    scroll=ft.ScrollMode.AUTO,
                                                                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                                                    spacing=0,
                                                                    controls=[
                                                                        ft.DataTable(
                                                                            column_spacing=20,
                                                                            expand=True,
                                                                            columns=[
                                                                                ft.DataColumn(label=ft.Text('FECHA', text_align=ft.TextAlign.CENTER)),
                                                                                ft.DataColumn(label=ft.Text('HORA', text_align=ft.TextAlign.CENTER)),
                                                                                ft.DataColumn(label=ft.Text('MEDICO', text_align=ft.TextAlign.CENTER))
                                                                            ],
                                                                            rows=[
                                                                                ft.DataRow(
                                                                                    cells=[
                                                                                        ft.DataCell(ft.Text("2025-03-10", text_align=ft.TextAlign.CENTER)),
                                                                                        ft.DataCell(ft.Text("10:00", text_align=ft.TextAlign.CENTER)),
                                                                                        ft.DataCell(ft.Text("FERNANDO OLIVARES GOMEZ", text_align=ft.TextAlign.CENTER))
                                                                                    ]
                                                                                ) for i in range(20)
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    )

                                                    
                                                ]
                                            )
                                            
                                        
                                        )
                                    )
                                ]
                            )
                        )
                    )
                ]
            )
        )
