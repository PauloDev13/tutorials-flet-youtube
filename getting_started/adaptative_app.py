import flet as ft


def main(page: ft.Page):
    page.adaptive = True

    page.appbar = ft.AppBar(
        leading=ft.TextButton(
            text='Novo',
            style=ft.ButtonStyle(padding=0)
        ),
        title=ft.Text(value='Barra adaptável'),
        bgcolor=ft.colors.with_opacity(
            0.04,
            ft.cupertino_colors.SYSTEM_BACKGROUND
        )
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.EXPLORE,
                label='Explorar'
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.COMMUTE,
                label='Comutar'
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label='Marcador'
            )
        ],
        border=ft.Border(
            top=ft.BorderSide(
                color=ft.cupertino_colors.SYSTEM_GREY2,
                width=0
            )
        )
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[
                    ft.Checkbox(
                        value=False,
                        label='Modo escuro'
                    ),
                    ft.Text(value='Primeiro campo'),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Text(value='Segundo campo'),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Switch(label='Chave'),
                    ft.FilledButton(
                        content=ft.Text(value='Botão'),
                    ),
                    ft.Text('Texto 1'),
                    ft.Text('Texto 2'),
                    ft.Text('Texto 3'),
                ]
            )
        )
    )


ft.app(target=main)
