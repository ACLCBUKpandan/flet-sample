
import flet as ft

from functools import reduce

from controller.ProductController import get_products

from model.Product import Product
from view.components.ItemCard import ItemCard



def new_transaction_page(page: ft.Page, view: ft.View):
    products: list[Product] = get_products()
    selected_product: Product | None = None

    cart_items: list[tuple[Product, int]] = []

    total: float = 0

    view.appbar = ft.AppBar(title=ft.Text('New Transaction'),
                            leading=ft.IconButton(icon=ft.icons.ARROW_BACK,
                                                  on_click=lambda _: page.go('/')),)

    vw_product_list = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=300,
        spacing=5,
        run_spacing=5,
    )
    vw_cartlist = ft.ListView()

    vw_total = ft.Text(f'P {0}',
                       weight=ft.FontWeight.W_900,
                       size=30)

    def on_item_click(product: Product):
        print('Hi')
        quantity: int = 1
        subtotal: float = product.price * quantity

        vw_quantity = ft.Text(f'x {quantity}', weight=ft.FontWeight.BOLD)
        vw_subtotal = ft.Text(f'P {subtotal}',
                              weight=ft.FontWeight.BOLD,
                              size=24)

        def on_plus(_):
            nonlocal quantity

            quantity = quantity if quantity >= product.stocks else quantity + 1
            subtotal = product.price * quantity
            print(quantity)
            vw_quantity.value = f'x {quantity}'
            vw_subtotal.value = f'P {subtotal}'
            page.update()

        def on_minus(_):
            nonlocal quantity
            quantity = quantity if quantity - 1 <= 0 else quantity - 1
            subtotal = product.price * quantity
            vw_quantity.value = f'x {quantity}'
            vw_subtotal.value = f'P {subtotal}'
            page.update()

        def on_confirm(_):

            cart_items.append((product, quantity))

            # calculate total
            total = reduce(lambda acc, item:
                           acc + item[0].price * item[1],
                           cart_items,
                           0)
            set_cart_listview()
            vw_total.value = f'P {total}'
            vw_total.update()
            dialog.open = False
            dialog.update()

        def on_close(_):
            dialog.open = False
            dialog.update()

        dialog: ft.AlertDialog = ft.AlertDialog(
            title=ft.Text(
                f'{product.name}   -  P{product.price}   - x{product.stocks}'
            ),
            content=ft.Container(
                width=600,
                height=600,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=product.image, width=400, height=400),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton('-', on_click=on_minus),
                                vw_quantity,
                                ft.ElevatedButton('+', on_click=on_plus),
                            ]
                        ),
                        vw_subtotal
                    ],
                )
            ),
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.TextButton('CANCEL', on_click=on_close),
                ft.TextButton('CONFIRM', on_click=on_confirm),
            ],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def set_products_list() -> ft.GridView:
        cards = map(
            lambda x:
                ItemCard(product=x,
                         on_click=lambda: on_item_click(product=x),),
            products)

        vw_product_list.controls = list(cards)
        return vw_product_list

    def set_cart_listview():
        cards = map(lambda x:
                    ft.Container(
                        on_click=lambda: None,
                        bgcolor=ft.colors.GREEN,
                        border_radius=5,
                        padding=20,
                        margin=2,
                        content=ft.Row(
                            controls=[
                                ft.Text(value=x[0].name,
                                        color=ft.colors.WHITE
                                        ),
                                ft.Text(value=f'x {x[1]}',
                                        color=ft.colors.WHITE
                                        ),
                                ft.Text(value=f'P {x[0].price}',
                                        color=ft.colors.WHITE
                                        ),
                            ],
                        ),

                    ), cart_items)
        vw_cartlist.controls = list(cards)
        vw_cartlist.update()

    view.controls = [
        ft.ResponsiveRow(
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Column(col=9, controls=[set_products_list()]),


                ft.Column(col=3,
                          horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                          controls= [
                              ft.Column(controls=[
                                  ft.Text('TOTAL '),
                                  vw_total,
                                  ft.FilledButton('CHECKOUT', width=1000),
                              ]),

                              ft.Text(' : '),
                              vw_cartlist
                          ],
                          )
            ]
        )

    ]


    return view
