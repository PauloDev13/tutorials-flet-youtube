import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Alert Dialog'

    def on_click(_) -> None:
        page.overlay.append(alert)
        alert.open = True
        page.update()

    def on_close(_, option: str) -> None:
        alert.open = False

        if option == 'y':
            print('Ação confirmada. Dados apagados')
        else:
            print('Ação cancelada')

        page.update()

    title = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.icons.START),
            ft.Text(
                value='CONFIRMAÇÃO',
                size=20
            )
        ]
    )

    alert = ft.AlertDialog(
        modal=True,
        title=title,
        content=ft.Text(value='Confirma a ação?'),
        actions=[
            ft.ElevatedButton(
                text='SIM',
                on_click=lambda e: on_close(e, option='y'),
            ),
            ft.ElevatedButton(
                text='NÃO',
                on_click=lambda e: on_close(e, option='n'),
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.overlay.remove(alert),
    )

    page.add(
        ft.ElevatedButton(
            text='Abrir dialog',
            on_click=on_click,
        )
    )


ft.app(target=main)
