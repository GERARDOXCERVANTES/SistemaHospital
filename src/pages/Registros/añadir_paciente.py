import flet as ft
from datetime import datetime
from src.models.paciente import Paciente

# Custom components
class VitalField(ft.Container):
    def __init__(self, label, icon, hint="", expand=True, password=False, width=None):
        self.text_field = ft.TextField(
            label=label,
            hint_text=hint,
            border_color=ft.colors.BLUE_400,
            focused_border_color=ft.colors.BLUE_700,
            prefix_icon=icon,
            expand=expand,
            password=password,
            text_size=14,
            width=width,
            border_radius=8,
        )
        super().__init__(
            content=self.text_field,
            padding=5,
            expand=expand,
        )

    @property
    def value(self):
        return self.text_field.value

    @value.setter
    def value(self, val):
        self.text_field.value = val


class ActionButton(ft.Container):
    def __init__(self, text, icon, bgcolor, on_click=None, width=150):
        self.button = ft.ElevatedButton(
            text=text,
            icon=icon,
            bgcolor=bgcolor,
            color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                elevation=3,
            ),
            height=45,
            width=width,
            on_click=on_click,
        )
        super().__init__(
            content=self.button,
            padding=5,
        )


class TextoIcono(ft.Row):
    def __init__(self, text, icon, color):
        super().__init__(
            controls=[
                ft.Icon(icon, color=color, size=26),
                ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
        )


class DataRow(ft.Row):
    def __init__(self, icon, content, size=14, color="#555555"):
        super().__init__(
            controls=[
                ft.Icon(icon, size=size + 4, color=color),
                ft.Text(content, size=size, color=color),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.START,
        )


class Card(ft.Container):
    def __init__(self, title, icon, content, width=None):
        super().__init__(
            content=ft.Column(
                controls=[
                    TextoIcono(title, icon, ft.colors.BLUE_400),
                    ft.Divider(height=1, color="#DFDFDF"),
                    content
                ],
                spacing=10,
            ),
            width=width,
            padding=20,
            border_radius=12,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.BLUE_100),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.1, ft.colors.BLACK),
            )
        )


class AddPaciente(ft.Container):
    def __init__(self):
        
        
        # Patient basic info fields
        self.nombre = VitalField(label="Nombre completo", icon=ft.icons.PERSON_OUTLINE, hint="Nombre y apellidos")
        self.sexo = VitalField(label="Sexo", icon=ft.icons.WAVING_HAND, hint="M/F", width=100)
        self.fecha_nacimiento = VitalField(label="Fecha de Nacimiento", icon=ft.icons.DATE_RANGE, hint="DD/MM/AAAA")
        
        
        # Contact info fields
        self.telefono = VitalField(label="Teléfono", icon=ft.icons.PHONE, hint="Número de contacto")
        self.direccion = VitalField(label="Dirección", icon=ft.icons.LOCATION_ON, hint="Dirección completa")
        
        # Medical info fields
        self.tipo_sangre = VitalField(label="Tipo de Sangre", icon=ft.icons.BLOODTYPE, hint="Ej: O+", width=100)
        self.alergias = VitalField(label="Alergias", icon=ft.icons.HEALTH_AND_SAFETY, hint="Medicamentos, alimentos, etc.")
        self.condiciones = VitalField(label="Condiciones médicas", icon=ft.icons.MEDICAL_INFORMATION, hint="Diabetes, hipertensión, etc.")        
        
        self.alergia = ActionButton(
            text=" ALERGIAS",
            icon=ft.icons.ADD,
            bgcolor=ft.colors.INDIGO_800,
            on_click=self.add_alergia
        )
        self.condicione = ActionButton(
            text="CONDICIONES",
            icon=ft.icons.ADD,
            bgcolor=ft.colors.INDIGO_800,
            on_click=self.add_condicion
        )        

        
        # Action buttons
        self.registrar = ActionButton(
            text="Registro de Pacientes",
            icon=ft.icons.PERSON_ADD,
            bgcolor=ft.colors.GREEN_600,
            on_click=self.registrar_paciente,
        )
        
        self.limpiar = ActionButton(
            text="Limpiar Campos",
            icon=ft.icons.CLEAR_ALL,
            bgcolor=ft.colors.BLUE_GREY_400,
            on_click=self.limpiar_campos,
        )
        self.eliminar = ActionButton(
            text="eliminar paciente",
            icon=ft.icons.DELETE_FOREVER,
            bgcolor=ft.colors.RED_400,
            on_click=self.eliminar_paciente
        )
        # Crear estructura del formulario
        super().__init__(
            expand=True,
            border_radius= 30,
            padding=30,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=TextoIcono("REGISTRO DE PACIENTES O ELIMINACION DE PACIENTES", ft.icons.PERSON_ADD_ALT_1, ft.colors.BLUE_700),
                        padding=10,
                    ),
                    ft.Text(
                        f"Fecha de registro: {datetime.now().strftime('%d/%m/%Y')}",
                        size=12,
                        color=ft.colors.GREY_700,
                    ),
                    ft.Divider(height=1, color=ft.colors.BLUE_200),
                    
                    # Contenido principal en dos columnas
                    ft.Row(
                        controls=[
                            # Columna izquierda - Datos del paciente
                            ft.Column(
                                controls=[
                                    Card(
                                        "INFORMACIÓN PERSONAL",
                                        ft.icons.PERSON,
                                        ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[self.nombre],
                                                    spacing=10,
                                                ),
                                                ft.Row(
                                                    controls=[self.fecha_nacimiento, self.sexo],
                                                    spacing=10,
                                                ),
                                            ],
                                            spacing=10,
                                        ),
                                    ),
                                    
                                    Card(
                                        "INFORMACIÓN DE CONTACTO",
                                        ft.icons.CONTACT_MAIL,
                                        ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[self.telefono],
                                                    spacing=10,
                                                ),
                                                
                                                ft.Row(
                                                    controls=[self.direccion],
                                                    spacing=10,
                                                ),
                                            ],
                                            spacing=10,
                                        ),
                                    ),
                                    
                                    Card(
                                        "INFORMACIÓN MÉDICA",
                                        ft.icons.MEDICAL_SERVICES,
                                        ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[self.tipo_sangre],
                                                    spacing=10,
                                                ),
                                                ft.Row(
                                                    controls=[self.alergias],
                                                    spacing=10,
                                                ),
                                                ft.Row(
                                                    controls=[self.condiciones],
                                                    spacing=10,
                                                ),
                                            ],
                                            spacing=10,
                                        ),
                                    ),
                                ],
                                spacing=15,
                                expand=3,
                            ),
                            
                            # Columna derecha - Detalles de cita
                            ft.Column(
                                controls=[
                                    self.limpiar,
                                    self.registrar,
                                    self.eliminar,
                                    self.alergia,
                                    self.condicione
                                    # Botones de acción
                                    
                                ],
                                alignment= ft.alignment.center,
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                spacing=15,
                                expand=2,
                            ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                spacing=15,
            ),
            bgcolor=ft.colors.GREY_50,
        )
        
    
    def registrar_paciente(self, e):
        
        campos = [
            ("Nombre", self.nombre.value),
            ("Sexo", self.sexo.value),
            ("Fecha de Nacimiento", self.fecha_nacimiento.value),
            ("Teléfono", self.telefono.value),
            ("Dirección", self.direccion.value),
            ("Tipo de Sangre", self.tipo_sangre.value),
            ("Alergias", self.alergias.value),
            ("Condiciones Médicas", self.condiciones.value),
            
        ]

        
        for label, value in campos:
            if not value:  
                self.page.open(
                    ft.SnackBar(
                        content=ft.Text(f"El campo '{label}' no puede estar vacío."),
                        bgcolor=ft.colors.RED_500,
                        action="OK",
                    )
                )
                return
            
        Paciente.new_paciente(self.nombre.value,self.sexo.value,self.fecha_nacimiento.value,self.tipo_sangre.value,self.telefono.value,self.direccion.value)
        self.limpiar_campos(e)
        self.page.open(
            ft.SnackBar(
                content=ft.Text("Paciente registrado correctamente"),
                bgcolor=ft.colors.GREEN_500,
                action="OK",
            )
        )
        
        
    def limpiar_campos(self, e):
        # Limpiar todos los campos del formulario uno por uno
        self.nombre.value = ""
        self.sexo.value = ""
        self.fecha_nacimiento.value = ""
        self.telefono.value = ""
        self.direccion.value = ""
        self.tipo_sangre.value = ""
        self.alergias.value = ""
        self.condiciones.value = ""
        

        # Actualizar la interfaz para reflejar los cambios
        self.update()

        # Mostrar mensaje de confirmación
        self.page.open(
            ft.SnackBar(
                content=ft.Text("Campos limpiados"),
                bgcolor=ft.colors.BLUE_500,
                action="OK",
            )
        )

    def eliminar_paciente(self, e):
        # Crear campo para el diálogo
        id_eliminar = ft.TextField(
            label="ID del Paciente",
            hint_text="Ingrese el ID del Paciente a eliminar",
            prefix_icon=ft.icons.PERSON_REMOVE,
            border_radius=8,
        )
        
        # Crear diálogo
        dialog = ft.AlertDialog(
            title=ft.Text("Eliminar Paciente", weight=ft.FontWeight.BOLD, color=ft.colors.RED),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Esta acción eliminará permanentemente al Paciente del sistema.",
                        color=ft.colors.RED_700
                    ),
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    id_eliminar,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    ft.Text(
                        "Para confirmar, ingrese el ID del Paciente y presione 'Eliminar'.",
                        size=12,
                        italic=True,
                        color=ft.colors.GREY_700
                    ),
                ],
                spacing=5,
                width=400,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    style=ft.ButtonStyle(color=ft.colors.GREY_700),
                    on_click=lambda e: self.cerrar_dialogo_eliminar(e, dialog),
                ),
                ft.ElevatedButton(
                    "Eliminar",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.RED_600,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=lambda e: self.confirmar_eliminacion(e, dialog, id_eliminar.value),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.open(dialog)
        self.page.update()
    
    def cerrar_dialogo_eliminar(self, e, dialog):
        dialog.open = False
        self.page.update()
    
    def confirmar_eliminacion(self, e, dialog, id_paciente):
        if not id_paciente:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Por favor ingrese un ID válido"),
                    bgcolor=ft.colors.RED_500,
                    action="OK",
                )
            )
            return
        
        
        Paciente.eliminar_paciente(id_paciente)
        
        # Cerrar el diálogo
        dialog.open = False
        self.page.update()
        
        
    def add_alergia(self, e):
        # Crear campo para el diálogo
        id_paciente = ft.TextField(
            label="ID del Paciente",
            hint_text="Ingrese el ID del Paciente a agregar alergia",
            prefix_icon=ft.icons.PERSON_REMOVE,
            border_radius=8,
        )
        
        alergia = ft.TextField(
            label="alergia",
            hint_text="Ingrese la alergia agregar",
            prefix_icon=ft.icons.PERSON_REMOVE,
            border_radius=8,
        )
        
        # Crear diálogo
        dialog = ft.AlertDialog(
            title=ft.Text("agregar alergia", weight=ft.FontWeight.BOLD, color=ft.colors.INDIGO_800),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Esta agregara una alergia al paciente dado por su id.",
                        color=ft.colors.INDIGO_700
                    ),
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    id_paciente,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    alergia,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    ft.Text(
                        "Para confirmar, ingrese el ID del Paciente y presione 'aceptar'",
                        size=12,
                        italic=True,
                        color=ft.colors.GREY_700
                    ),
                ],
                spacing=5,
                width=400,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    style=ft.ButtonStyle(color=ft.colors.GREY_700),
                    on_click=lambda e: self.cerrar_dialogo_eliminar(e, dialog),
                ),
                ft.ElevatedButton(
                    "ACEPTAR",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.INDIGO_700,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=lambda e: self.confirmar_alergia(e, dialog, id_paciente.value,alergia.value),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.open(dialog)
        self.page.update()
    
    
    def confirmar_alergia(self, e, dialog, id_paciente,alergia):
        if not id_paciente:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Por favor ingrese un ID válido"),
                    bgcolor=ft.colors.GREEN_400,
                    action="OK",
                )
            )
            return
        
        Paciente.add_alergias(id_paciente,alergia)
        
        
        # Cerrar el diálogo
        dialog.open = False
        self.page.update()
    
    def add_condicion(self, e):
        # Crear campo para el diálogo
        id_paciente = ft.TextField(
            label="ID del Paciente",
            hint_text="Ingrese el ID del Paciente a agregar condicion",
            prefix_icon=ft.icons.PERSON_REMOVE,
            border_radius=8,
        )
        
        alergia = ft.TextField(
            label="condicion",
            hint_text="Ingrese la condicion a agregar",
            prefix_icon=ft.icons.PERSON_REMOVE,
            border_radius=8,
        )
        
        # Crear diálogo
        dialog = ft.AlertDialog(
            title=ft.Text("agregar condicion", weight=ft.FontWeight.BOLD, color=ft.colors.INDIGO_800),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Esta agregara una condicion al paciente dado por su id.",
                        color=ft.colors.INDIGO_700
                    ),
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    id_paciente,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    alergia,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    ft.Text(
                        "Para confirmar, ingrese el ID del Paciente y presione 'aceptar'",
                        size=12,
                        italic=True,
                        color=ft.colors.GREY_700
                    ),
                ],
                spacing=5,
                width=400,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    style=ft.ButtonStyle(color=ft.colors.GREY_700),
                    on_click=lambda e: self.cerrar_dialogo_eliminar(e, dialog),
                ),
                ft.ElevatedButton(
                    "AÑADIR",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.INDIGO_700,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=lambda e: self.confirmar_condicion(e, dialog, id_paciente.value,alergia.value),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.open(dialog)
        self.page.update()
    
    
    def confirmar_condicion(self, e, dialog, id_paciente,alergia):
        if not id_paciente:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Por favor ingrese un ID válido"),
                    bgcolor=ft.colors.GREEN_400,
                    action="OK",
                )
            )
            return
        
        Paciente.add_condicones(id_paciente,alergia)
        
        
        # Cerrar el diálogo
        dialog.open = False
        self.page.update()
        
        
        
        



    
