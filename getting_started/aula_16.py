import flet
from flet import Page, AppBar, ElevatedButton, Text, TextStyle, TextThemeStyle, View, colors


def main(page: Page):
    page.title = 'Exemplo de Navigation e Route em Flet'

    print('Rota inicial:', page.route)

    def route_change(e):
        print('Rota mudou:', e.route)
        page.views.clear()
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text(value='App Flet')),
                    ElevatedButton(
                        text='Ir para configurações',
                        on_click=open_settings
                    ),
                ]
            )
        )

        if page.route == '/settings' or page.route == '/':
            page.views.append(
                View(
                    route='/settings',
                    controls=[
                        AppBar(title=Text(value='Settings'),
                               bgcolor=colors.SURFACE_VARIANT),
                        Text(value='Settings', style=TextThemeStyle.BODY_MEDIUM),
                        ElevatedButton(
                            text='Ir para email',
                            on_click=open_mail_settings
                        ),
                    ]
                )
            )

        if page.route == '/settings/mail':
            page.views.append(
                View(
                    route='/settings/mail',
                    controls=[
                        AppBar(title=Text(value='Mail settings'),
                               bgcolor=colors.SURFACE_VARIANT),
                        Text(value='Mail settings'),
                    ]
                )
            )

        page.update()

    def view_pop(e):
        print('Vista pop', e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_mail_settings(e):
        page.go('/settings/mail')

    def open_settings(e):
        page.go('/settings')

    page.go(page.route)


flet.app(target=main, view=flet.AppView.WEB_BROWSER)
