import flet
from flet import Page, TextField, Column, ElevatedButton, Text, Ref


def main(page: Page):
    txt_first_name = Ref[TextField]()
    txt_last_name = Ref[TextField]()
    col_controls = Ref[Column]()

    def on_btn_clicked(_):
        col_controls.current.controls.append(
            Text(
                value=f'Olá {txt_first_name.current.value} {txt_last_name.current.value}',
                size=20
            )
        )
        txt_first_name.value = ''
        txt_last_name.value = ''

        page.update()
        txt_first_name.current.focus()

    btn_submit = ElevatedButton(text='Submeter', on_click=on_btn_clicked)

    page.add(
        TextField(ref=txt_first_name, label='First Name', on_focus=True),
        TextField(ref=txt_last_name, label='Last Name'),
        btn_submit,
        Column(ref=col_controls),
    )


flet.app(target=main)
