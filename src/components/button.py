import flet as ft
class buttonP(ft.ElevatedButton):
    def __init__(self,text):
        
        super().__init__(
            width= 200,
            height= 40, 
            bgcolor = '#000080',
            color= ft.colors.WHITE
           
        )
        
        self.text = text

    