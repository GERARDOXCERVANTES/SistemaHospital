import flet as ft


accent_color = "#3f51b5"  # Azul claro para acentos

class botonesIU(ft.Container):
    def __init__(self):
        super().__init__(
            expand= True,
            padding= 20,
            content= ft.Row(
                vertical_alignment= ft.CrossAxisAlignment.END,
                alignment= ft.MainAxisAlignment.END,
                spacing= 30,
                controls= [
                    botonPersonalizado(
                    'INICIAR SESION',
                    ft.Icons.PLAY_ARROW,
                    ft.colors.WHITE,
                    accent_color,
                    ft.Colors.WHITE
                ),botonPersonalizado(
                    'PAUSAR',
                    ft.Icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    ft.colors.WHITE,
                    ft.colors.RED,
                    ft.Colors.WHITE
                ),ft.FilledButton(
                    "GUARDAR",
                    icon=ft.icons.SAVE,
                    elevation= 5,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    height=50,
                ),botonPersonalizado(
                    'FINALIZAR',
                    ft.Icons.STOP_CIRCLE_ROUNDED,
                    ft.colors.WHITE,
                    accent_color,
                    ft.Colors.WHITE
                    
                )
                    
                ]
            )            
        )
def botonPersonalizado(text,icon,color,bgcolor,iconC):
    return ft.ElevatedButton(
        height= 50,
        elevation= 5,
        text= text,
        icon= icon,
        icon_color= iconC,
        style= ft.ButtonStyle(
            color= color,
            bgcolor= bgcolor,
            shape=ft.RoundedRectangleBorder(radius=8),

            
        )
        
    )
    

    
