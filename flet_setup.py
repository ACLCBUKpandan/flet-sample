import flet as ft

from view.MainMenuView import main_menu_page
from view.NewTransactionView import new_transaction_page

from view.LoginView import login_page


def main(page: ft.Page):
    page.title = "App"
    page.theme = ft.Theme(color_scheme_seed='green', )
    page.dark_theme = ft.Theme(color_scheme_seed='green', )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    views: list[ft.View] = [
        login_page(page, ft.View('/login')),
        main_menu_page(page, ft.View('/')),
        new_transaction_page(page, ft.View('/new')),
    ]

    def route_change(route):
        page.views.clear()

        print(route)

        sel = tuple(filter(lambda v: v.route == page.route, views))

        page.views.append(sel[0])
        page.go(sel[0].route)

    page.on_route_change = route_change
    page.go(page.route)
