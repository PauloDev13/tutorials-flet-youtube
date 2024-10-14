import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Banner'

    def on_click(_) -> None:
        page.overlay.append(banner)
        banner.open = True
        page.update()

    def on_close(e, options: str) -> None:
        banner.open = False

        if options == 'a':
            print(f'Atualizações do ID: {banner.data['id']} aplicadas com sucesso!')

        elif options == 'b':
            print('Atualizações serão lembradas mais tarde!')

        else:
            print('Atualizações foram canceladas!')

        page.overlay.remove(banner)
        banner.update()

    content = ft.ResponsiveRow(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value='Olá, atualizações disponíveis. Deseja atualizar?',
                size=20
            )
        ]
    )

    banner = ft.Banner(
        bgcolor=ft.colors.BLUE_800,
        margin=ft.Margin(top=100, left=100, bottom=0, right=100),
        content=content,
        leading=ft.Icon(ft.icons.WARNING, color=ft.colors.WHITE),
        data={'id': 28},
        actions=[
            ft.TextButton(
                text='Atualizar agora',
                on_click=lambda e: on_close(e, options='a'),
            ),
            ft.TextButton(
                text='Lembrar mais tarde',
                on_click=lambda e: on_close(e, options='b'),
            ),
            ft.TextButton(
                text='Cancelar',
                on_click=lambda e: on_close(e, options='c'),
            )
        ],
    )

    page.add(
        ft.ElevatedButton(
            text='Abrir banner',
            on_click=on_click,
        )
    )


ft.app(target=main)
