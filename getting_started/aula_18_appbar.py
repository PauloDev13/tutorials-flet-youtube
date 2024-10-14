import flet as ft


def main(page: ft.Page) -> None:
    page.appbar = ft.AppBar(
        bgcolor='#003377',
        title=ft.Text(value='Minha Loja'),
        leading=ft.Icon(name=ft.icons.ADD),
        leading_width=40,
        actions=[
            ft.IconButton(icon=ft.icons.WB_SUNNY_OUTLINED),
            ft.PopupMenuButton(
                tooltip='Exibir Menu',
                items=[
                    ft.PopupMenuItem(
                        text='Logar'
                    ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text='Sair'
                    )
                ]
            )
        ]
    )

    page.add(ft.Text(value='Body'))


ft.app(target=main)
