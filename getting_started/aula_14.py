import flet
from flet import Page, Text, Dropdown, dropdown, ElevatedButton


def main(page: Page):
    page.title = 'Exemplo de Dropdown em Flet'

    def btn_clicked(_):
        output_text.value = f'O valor do Dropdown é: {color_dropdown.value}'
        output_text.update()

    output_text = Text()
    submit_btn = ElevatedButton(text='Submit', on_click=btn_clicked)
    color_dropdown = Dropdown(
        width=100,
        on_change=btn_clicked,
        options=[
            dropdown.Option('Vermelho'),
            dropdown.Option('Verde'),
            dropdown.Option('Azul'),
        ]
    )

    page.add(color_dropdown, submit_btn, output_text)


flet.app(target=main)
