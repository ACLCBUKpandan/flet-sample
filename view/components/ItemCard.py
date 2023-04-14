from typing import Callable
import flet as ft

from model.Product import Product


def ItemCard(product: Product,
             on_click: Callable) -> ft.Control:
    return ft.Container(
        on_click=lambda _: on_click(),
        bgcolor=ft.colors.YELLOW_ACCENT_700,
        border_radius=5,
        padding=20,
        margin=2,

        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,

            controls=[
                ft.Image(src=product.image,
                         width=150,height=150),
                ft.Text(value=product.name,
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.W_900),
                ft.Text(value=f'x {product.stocks}',
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.W_300),
                ft.Text(value=f'P {product.price}',
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.W_400),
            ],
        ),

    )
