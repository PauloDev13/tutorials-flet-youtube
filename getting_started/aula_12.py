import flet
from flet import Page, ElevatedButton, TextField, Text


def main(page: Page):
    page.title = 'Exemplo de TextBox em Flet'

    def btn_clicked(_):
        if not txt_name.value:
            txt_name.error_text = 'Nome é obrigatório'
            txt_name.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(Text(value=f'Olá, {name}'))

    txt_name = TextField(label='Seu nome')

    page.add(txt_name, ElevatedButton(text='Diga olá', on_click=btn_clicked))


flet.app(target=main)
