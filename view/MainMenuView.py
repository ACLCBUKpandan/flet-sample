import flet as ft

def MainMenuCard(name: str,
                 icon,
                 on_click,
                 color=ft.colors.YELLOW_ACCENT_400,
                 ) -> ft.Control:
    return ft.Container(
        padding=10,
        width=200,
        height=200,
        bgcolor=color,
        on_click=on_click,
        content=ft.Column(
            [
                ft.Icon(icon, size=64),
                ft.Text(name)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


def main_menu_page(page: ft.Page, view: ft.View) -> ft.View:

    view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    view.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_new_transaction(_):
        page.go('/new')

    def on_history(_):
        page.go('/new')

    def on_logout(_):
        page.go('/login')

    view.controls = [
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                MainMenuCard('Create Transaction',
                             ft.icons.ADD,
                             on_click=on_new_transaction),

                MainMenuCard('History',
                             ft.icons.BOOK,
                             on_click=on_history),

                MainMenuCard('Log-out',
                             ft.icons.LOGOUT,
                             on_click=on_logout),
            ],

        )
    ]

    return view

