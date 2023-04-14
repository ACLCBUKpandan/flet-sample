import flet as ft

from controller.AuthController import login

def login_page(root: ft.Page, page: ft.View):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # page variables
    username = ft.TextField(icon=ft.icons.PERSON)

    password = ft.TextField(password=True,
                            icon=ft.icons.PASSWORD,
                            can_reveal_password=True)

    login_fail: bool = False

    def login_click(e):
        if login(username=username.value, password=password.value):
            root.go('/')
        else:
            root.snack_bar = ft.SnackBar(
                ft.Text('Username or password not found!',
                        color="#ff0000"),
                bgcolor="#ffcccb")
            root.snack_bar.open = True

            root.update()


    def show_login_error():
        if login_fail:
            return ft.Text('Username or password error',
                           bgcolor="#ffcccb",
                           color="#ff0000")
        else:
            return ft.Container()

    page.controls = [(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=500,
            controls=[
                ft.Image(src="https://cdn-icons-png.flaticon.com/512/9845/9845764.png",
                         width=140,
                         height=140),

                ft.Text('Lambda Store', size=20,),
                username,
                password,
                show_login_error(),
                ft.Row(
                    [
                        ft.FilledButton('LOGIN', on_click=login_click),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )
    )]

    return page
