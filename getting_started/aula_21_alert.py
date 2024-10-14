import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Modal'

    def on_click(_) -> None:
        page.overlay.append(alert)
        alert.open = True
        page.update()

    def on_close(_) -> None:
        alert.open = False
        page.update()

    title = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.icons.START),
            ft.Text(
                value='Título do alerta',
                size=20
            )
        ]
    )

    alert = ft.AlertDialog(
        title=title,
        actions=[
            ft.ElevatedButton(
                text='Fechar',
                on_click=on_close,
            )
        ],
        content=ft.Text(value='Este é o conteúdo do alerta'),
        on_dismiss=lambda e: page.overlay.remove(alert),
    )

    page.add(
        ft.ElevatedButton(
            text='Abrir alerta',
            on_click=on_click,
        )
    )


ft.app(target=main)
