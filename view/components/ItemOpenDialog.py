from typing import Callable
import flet as ft

from model.Product import Product



def ItemOpenDialog(product: Product,
                   on_minus: Callable,
                   on_plus: Callable,
                   on_close: Callable,
                   on_confirm: Callable) -> ft.AlertDialog:
    return ft.AlertDialog(
        title=ft.Text(
            f'{product.name}   -  P{product.price}   - x{product.stocks}'
        ),
        content=ft.Container(
            width=600,
            height=600,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(src=product.image, width=400, height=400),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton('-',
                                              on_click=lambda _: on_minus()),
                            ft.ElevatedButton('+',
                                              on_click=lambda _: on_plus()),

                        ]
                    )
                ]
            )
        ),
        actions=[
        ]
    )
