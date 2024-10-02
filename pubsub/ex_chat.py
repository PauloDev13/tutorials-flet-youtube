import flet as ft


def main(page: ft.Page):
    page.title = 'Flet Chat'

    def on_message(msg):
        messages.controls.append(ft.Text(value=msg))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f'{user.value}: {message.value}')
        message.value = ''
        page.update()

    messages = ft.Column()
    user = ft.TextField(hint_text='Seu nome', width=150)
    message = ft.TextField(hint_text='Sua mensagem', width=150, expand=True)
    send = ft.ElevatedButton(text='Enviar', on_click=send_click)
    page.add(messages, ft.Row(
        controls=[
            user,
            message,
            send
        ]
    ))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
