import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Rotas'

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.HOME,
                label='Início',
                tooltip='Ir para o inicio'
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.EXPLORE,
                label='Explorar',
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.COMMUTE,
                label='Rotas',
            )
        ]
    )

    page.add(
        ft.Text(value='Body')
    )


ft.app(target=main)
