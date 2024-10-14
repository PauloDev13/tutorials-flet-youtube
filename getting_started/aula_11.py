import flet
from flet import Page, IconButton, TextField, Row, icons, TextAlign, MainAxisAlignment


def main(page: Page):
    page.title = 'Exemplo de contador em Flet'
    page.vertical_alignment = 'center'

    txt_number = TextField(
        value='0',
        text_align=TextAlign.CENTER,
        width=100
    )

    def minus_clicked(_):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_clicked(_):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        Row(controls=[
            IconButton(icon=icons.REMOVE, on_click=minus_clicked),
            txt_number,
            IconButton(icon=icons.ADD, on_click=plus_clicked),
        ],
            alignment=MainAxisAlignment.CENTER
        )
    )


flet.app(target=main)
