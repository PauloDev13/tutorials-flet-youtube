import flet
from flet import Page, Text, ListView


def main(page: Page):
    page.title = 'Exemplo de ListView em Flet'

    lv = ListView(expand=True, spacing=10, item_extent=30)

    for i in range(500):
        lv.controls.append(Text(f'Linha {i}'))

    page.add(lv)


flet.app(target=main, view=flet.AppView.WEB_BROWSER)
