import flet
from flet import Page, Text, Checkbox


def main(page: Page):
    page.title = 'Exemplo de CheckBox em Flet'

    def checkbox_changed(_):
        output_text.value = f'Você está aprendendo Flet: {todo_check.value}'
        output_text.update()

    output_text = Text()

    todo_check = Checkbox(
        label='ToDo: Aprendendo a usar Flet',
        value=False,
        on_change=checkbox_changed
    )

    page.add(todo_check, output_text)


flet.app(target=main)
