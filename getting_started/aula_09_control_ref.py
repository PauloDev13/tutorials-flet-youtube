import flet
from flet import Page, TextField, Column, ElevatedButton, Text


def main(page: Page):
    txt_first_name = TextField(label='Nome', autofocus=True)
    txt_last_name = TextField(label='Sobrenome')
    col_controls = Column()

    def on_submit(_):
        col_controls.controls.append(
            Text(
                value=f'Olá {txt_first_name.value} {txt_last_name.value}',
                size=20
            )
        )
        txt_first_name.value = ''
        txt_last_name.value = ''

        page.update()
        txt_first_name.focus()

    btn_submit = ElevatedButton(text='Submeter', on_click=on_submit)

    page.add(
        txt_first_name,
        txt_last_name,
        btn_submit,
        col_controls,
    )


flet.app(target=main)
