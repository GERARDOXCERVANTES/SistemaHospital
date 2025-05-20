import flet as ft
from datetime import datetime
from src.models.user import User
from src.models.medico import Medico
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
                    TextoIcono(title, icon, ft.colors.TEAL_400),
                    ft.Divider(height=1, color="#DFDFDF"),
                    content
                ],
                spacing=10,
            ),
            width=width,
            padding=20,
            border_radius=12,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.TEAL_100),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.1, ft.colors.BLACK),
            )
        )


class AddMedico(ft.Container):
    def __init__(self):
        
        
        
        self.nombre = VitalField(label="Nombre completo", icon=ft.icons.PERSON_OUTLINE, hint="Nombre y apellidos")
        
        
        
        # Professional info fields
        self.especialidad = VitalField(label="Especialidad", icon=ft.icons.MEDICAL_SERVICES, hint="Área de especialización")
        
        # Contact info fields
        self.telefono = VitalField(label="Teléfono", icon=ft.icons.PHONE, hint="Número de contacto")
        
        self.correo = VitalField(label="Correo electrónico", icon=ft.icons.EMAIL, hint="ejemplo@correo.com")
       
       
        
        # Action buttons
        self.registrar = ActionButton(
            text="Registrar Médico",
            icon=ft.icons.PERSON_ADD,
            bgcolor=ft.colors.TEAL_600,
            on_click=self.abrir_dialogo_usuario,
        )
        
        self.limpiar = ActionButton(
            text="Limpiar Campos",
            icon=ft.icons.CLEAR_ALL,
            bgcolor=ft.colors.BLUE_GREY_400,
            on_click=self.limpiar_campos,
        )
        
        self.eliminar = ActionButton(
            text="Eliminar Médico",
            icon=ft.icons.DELETE_FOREVER,
            bgcolor=ft.colors.RED_400,
            on_click=self.eliminar_medico
        )
        
        
        # Campos para resumen
        self.resumen_nombre = DataRow(ft.icons.PERSON_OUTLINE, "Dr(a): Pendiente", size=14)
        self.resumen_especialidad = DataRow(ft.icons.MEDICAL_SERVICES, "Especialidad: Pendiente", size=14)
        self.resumen_contacto = DataRow(ft.icons.CONTACT_PHONE, "Contacto: Pendiente", size=14)
        self.resumen_mensaje = ft.Text(
            "Esta información se actualizará al registrar el médico",
            size=12,
            italic=True,
            color=ft.colors.GREY_700,
        )
        
        # Crear estructura del formulario
        super().__init__(
            expand=True,
            border_radius= 30,
            padding=30,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=TextoIcono("REGISTRO DE MÉDICO", ft.icons.MEDICAL_SERVICES, ft.colors.TEAL_700),
                        padding=10,
                    ),
                    ft.Text(
                        f"Fecha de registro: {datetime.now().strftime('%d/%m/%Y')}",
                        size=12,
                        color=ft.colors.GREY_700,
                    ),
                    ft.Divider(height=1, color=ft.colors.TEAL_200),
                    
                    # Contenido principal en dos columnas
                    ft.Row(
                        controls=[
                            # Columna izquierda - Datos personales y profesionales
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
                                            ],
                                            spacing=10,
                                        ),
                                    ),
                                    
                                    Card(
                                        "INFORMACIÓN PROFESIONAL",
                                        ft.icons.SCHOOL,
                                        ft.Column(
                                            controls=[
                                                ft.Row(
                                                    controls=[self.especialidad],
                                                    spacing=10,
                                                )
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
                                                    controls=[self.correo],
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
                            
                            # Columna derecha - Detalles laborales y resumen
                            ft.Column(
                                controls=[
                                    
                                    # Vista previa de doctor
                                    Card(
                                        "RESUMEN DEL MÉDICO",
                                        ft.icons.PREVIEW,
                                        ft.Column(
                                            controls=[
                                                self.resumen_nombre,
                                                self.resumen_especialidad,
                                                self.resumen_contacto,
                                                ft.Row(
                                                    controls=[
                                                        ft.Container(
                                                            content=self.resumen_mensaje,
                                                            padding=5,
                                                        )
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                            ],
                                            spacing=10,
                                        ),
                                    ),
                                    
                                    # Botones de acción
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[self.limpiar, self.registrar, self.eliminar],
                                            alignment=ft.MainAxisAlignment.END,
                                            spacing=10,
                                        ),
                                        padding=ft.padding.only(top=20),
                                    ),
                                ],
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
    
    def abrir_dialogo_usuario(self, e):
        
        if not self.nombre.value or not self.especialidad.value or not self.telefono.value:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Por favor complete los campos obligatorios"),
                    bgcolor=ft.colors.RED_500,
                    action="OK",
                )
            )
            return
        
        # Crear campos para el diálogo
        nombre_usuario = ft.TextField(
            label="Nombre de usuario",
            hint_text="Ingrese un nombre de usuario",
            prefix_icon=ft.icons.ACCOUNT_CIRCLE,
            border_radius=8,
        )
        
        contrasena = ft.TextField(
            label="Contraseña",
            hint_text="Ingrese una contraseña",
            prefix_icon=ft.icons.LOCK,
            password=True,
            border_radius=8,
        )
        
        confirmar_contrasena = ft.TextField(
            label="Confirmar contraseña",
            hint_text="Confirme la contraseña",
            prefix_icon=ft.icons.LOCK_OUTLINE,
            password=True,
            border_radius=8,
        )
        
        
        if self.nombre.value:
            nombre_partes = self.nombre.value.split()
            if len(nombre_partes[0]) >= 2:
                primeras_dos_letras = nombre_partes[0][:2].upper()  # Extrae las dos primeras letras y las pone en mayúsculas
                nombre_usuario.value = f'ME{primeras_dos_letras}'
            else:
                # Si el primer nombre tiene solo una letra, usar solo esa
                primeras_letras = nombre_partes[0][0].upper()
                nombre_usuario.value = f'ME{primeras_letras}'

        # Crear diálogo
        dialog = ft.AlertDialog(
            title=ft.Text("Crear Usuario para Médico", weight=ft.FontWeight.BOLD),
            content=ft.Column(
                controls=[
                    ft.Text(
                        f"Crear credenciales para: {self.nombre.value}",
                        color=ft.colors.BLUE_GREY_700
                    ),
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    nombre_usuario,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    contrasena,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    confirmar_contrasena,
                ],
                spacing=5,
                width=400,
                height=230,
                scroll=ft.ScrollMode.AUTO,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    style=ft.ButtonStyle(color=ft.colors.GREY_700),
                    on_click=lambda e: self.cerrar_dialogo_usuario(e, dialog),
                ),
                ft.ElevatedButton(
                    "Crear Usuario",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.TEAL_600,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=lambda e: self.registrar_medico(
                        e, 
                        dialog, 
                        nombre_usuario.value, 
                        contrasena.value, 
                        confirmar_contrasena.value
                    ),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.open(dialog)
        self.page.update()
    
    def cerrar_dialogo_usuario(self, e, dialog):
        dialog.open = False
        self.page.update()
    
    def registrar_medico(self, e, dialog=None, nombre_usuario=None, contrasena=None, confirmar_contrasena=None):
        # Si viene del diálogo, validar las credenciales
        if dialog:
            
            if contrasena != confirmar_contrasena:
                self.page.open(
                    ft.SnackBar(
                        content=ft.Text("Las contraseñas no coinciden"),
                        bgcolor=ft.colors.RED_500,
                        action="OK",
                    )
                )
                return
            User.addUser(nombre_usuario, contrasena, "medico")
            id_medic = Medico.add_medico(self.nombre.value, self.especialidad.value,self.correo.value, self.telefono.value, nombre_usuario)
            # Cerrar el diálogo
            dialog.open = False
            self.page.update()
            

            # Mostrar diálogo de confirmación de creación
            self.mostrar_confirmacion(nombre_usuario,id_medic)
            
            
        else:
            # Validación normal sin diálogo (no debería ejecutarse con el nuevo flujo)
            if not self.nombre.value or not self.especialidad.value or not self.telefono.value:
                self.page.open(
                    ft.SnackBar(
                        content=ft.Text("Por favor complete los campos obligatorios"),
                        bgcolor=ft.colors.RED_500,
                        action="OK",
                    )
                )
                return
            
            # Mostrar un mensaje de éxito
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Médico registrado correctamente"),
                    bgcolor=ft.colors.GREEN_500,
                    action="OK",
                )
            )
            
            self.actualizar_resumen()
    
    def mostrar_confirmacion(self, nombre_usuario,ID_medico):
        dialog_confirmacion = ft.AlertDialog(
            title=ft.Text("Registro Exitoso", weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
            content=ft.Column(
                controls=[
                    ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=50),
                    ft.Text(
                        f"Médico registrado correctamente con usuario: {nombre_usuario} y con ID: {ID_medico}",
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Se ha creado con éxito la cuenta de usuario para el médico.",
                        size=14,
                        color=ft.colors.BLUE_GREY_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                width=400,
            ),
            actions=[
                ft.ElevatedButton(
                    "Aceptar",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREEN,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=lambda e: self.cerrar_dialogo_confirmacion(e, dialog_confirmacion),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        
        self.page.open(dialog_confirmacion)
        self.limpiar_campos(None)
        self.page.update()
        	
    def cerrar_dialogo_confirmacion(self, e, dialog):
        dialog.open = False
        self.page.update()
    
    def actualizar_resumen(self):
        
        self.resumen_nombre.controls[1].value = f"Dr(a):{self.nombre.value}"
        self.resumen_especialidad.controls[1].value = f"Especialidad: {self.especialidad.value}"

        
        if self.telefono.value:
            self.resumen_contacto.controls[1].value = f"Contacto: {self.telefono.value}"
        
        self.resumen_mensaje.value = f"Registrado el {datetime.now().strftime('%d/%m/%Y')}"
        self.resumen_mensaje.color = ft.colors.GREEN
        
        self.page.update()
    
    def eliminar_medico(self, e):
        # Crear campo para el diálogo
        id_eliminar = ft.TextField(
            label="ID del Médico",
            hint_text="Ingrese el ID del médico a eliminar",
            prefix_icon=ft.icons.PERSON_REMOVE,
            border_radius=8,
        )
        
        # Crear diálogo
        dialog = ft.AlertDialog(
            title=ft.Text("Eliminar Médico", weight=ft.FontWeight.BOLD, color=ft.colors.RED),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Esta acción eliminará permanentemente al médico del sistema.",
                        color=ft.colors.RED_700
                    ),
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    id_eliminar,
                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                    ft.Text(
                        "Para confirmar, ingrese el ID del médico y presione 'Eliminar'.",
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
    
    def confirmar_eliminacion(self, e, dialog, id_medico):
        if not id_medico:
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Por favor ingrese un ID válido"),
                    bgcolor=ft.colors.RED_500,
                    action="OK",
                )
            )
            
        
        
        
        Medico.dell_medico(id_medico)
        # Cerrar el diálogo
        dialog.open = False
        self.page.update()
        
        # Mostrar mensaje de confirmación
        self.page.open(
            ft.SnackBar(
                content=ft.Text(f"Médico con ID {id_medico} eliminado correctamente"),
                bgcolor=ft.colors.RED_400,
                action="OK",
            )
        )
        
        # Opcional: Limpiar los campos después de eliminar
        self.limpiar_campos(e)
    
    def limpiar_campos(self, e):
        # Limpiar todos los campos del formulario
        for field in [
            self.nombre,
            self.especialidad,
            self.telefono,  self.correo, 
        ]:
            
            field.text_field.value = ""
        
        # Restablecer el resumen
        self.resumen_nombre.controls[1].value = "Dr(a): Pendiente"
        self.resumen_especialidad.controls[1].value = "Especialidad: Pendiente"
        self.resumen_contacto.controls[1].value = "Contacto: Pendiente"
        self.resumen_mensaje.value = "Esta información se actualizará al registrar el médico"
        self.resumen_mensaje.color = ft.colors.GREY_700
        
        
        self.page.update()
        
        
        if e:  
            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Campos limpiados"),
                    bgcolor=ft.colors.BLUE_500,
                    action="OK",
                )
            )

