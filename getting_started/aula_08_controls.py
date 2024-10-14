import flet as ft
from time import sleep


def main(page: ft.Page) -> None:
    def button_clicked(e):
        output_text.value = f'O valor escolhido é: {color_dropdown.value}'
        page.update()

    output_text = ft.Text()
    sumit_button = ft.ElevatedButton(text='Submit', on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=110,
        options=[
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Blue'),
            ft.dropdown.Option('Yellow')
        ]
    )

    page.add(
        ft.Row(
            controls=[
                color_dropdown,
                sumit_button,
            ]
        ),
        output_text
    )


ft.app(target=main)
