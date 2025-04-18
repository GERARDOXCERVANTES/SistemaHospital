import flet as ft

class vitalField(ft.Column):
    def __init__(self, label, icon, unit="", hint_text="", on_submit=None):
        # 1) Guardar la referencia a tu TextField
        self.text_field = ft.TextField(
            on_submit=on_submit,
            hint_text=hint_text,
            suffix_text=unit,
            border_radius=ft.border_radius.all(8),
            height=40,
            width=200,
            content_padding=ft.padding.only(left=10, right=10),
            text_size=14,
            focused_border_color="#3f51b5",
            focused_color="#3f51b5",
        )
        
        super().__init__(
            spacing=10,
            controls=[
                ft.Row(
                    [
                        ft.Icon(icon, color="#3f51b5", size=18),
                        ft.Text(label, weight=ft.FontWeight.W_500, size=14),
                    ],
                    spacing=5
                ),
                
                self.text_field
            ]
        )

    @property
    def value(self):
        return self.text_field.value
    @value.setter
    def value(self,label):
        self.text_field.value = label
        self.text_field.update()