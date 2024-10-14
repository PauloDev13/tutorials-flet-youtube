import flet as ft


def main(page: ft.Page) -> None:

    def on_navigation(e):
        if e.control.selected_index == 1:
            print('Estamos na página de índice 1')

        elif e.control.selected_index == 2:
            print('Estamos na página de índice 2')
        else:
            print('Estamos na página de índice 0')

    page.title = 'Barr lateral'

    rail = ft.NavigationRail(
        selected_index=0,
        group_alignment=-0.9,
        extended=False,
        min_width=100,
        min_extended_width=200,
        label_type=ft.NavigationRailLabelType.ALL,
        leading=ft.FloatingActionButton(
            icon=ft.icons.CREATE,
            text='Criar'
        ),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER,
                selected_icon=ft.icons.FAVORITE,
                label='Favorito'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label='Marcar'
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon=ft.icons.SETTINGS,
                label='Configurações'
            )
        ],
        on_change=lambda e: on_navigation(e)
    )

    page.add(
        ft.Row(
            expand=True,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    controls=[
                        ft.Text(value='Body')
                    ]
                )
            ]
        )
    )


ft.app(target=main)
