import flet as ft


def main(page: ft.Page) -> None:
    class Task(ft.Row):
        def __init__(self, text):
            super().__init__()
            self.is_isolated = True
            self.text_view = ft.Text(value=text)
            self.text_edit = ft.TextField(
                value=text,
                visible=False
            )
            self.edit_button = ft.IconButton(
                icon=ft.icons.EDIT,
                on_click=self.edit
            )
            self.save_button = ft.IconButton(
                icon=ft.icons.SAVE,
                on_click=self.save,
                visible=False
            )

            self.controls = [
                ft.Checkbox(),
                self.text_view,
                self.text_edit,
                self.edit_button,
                self.save_button,
            ]

        def edit(self, e) -> None:
            self.edit_button.visible = False
            self.save_button.visible = True
            self.text_view.visible = False
            self.text_edit.visible = True
            self.update()

        def save(self, e) -> None:
            self.edit_button.visible = True
            self.save_button.visible = False
            self.text_view.visible = True
            self.text_edit.visible = False
            self.text_view.value = self.text_edit.value
            self.update()

    page.add(
        Task(text='Lavar roupa'),
        Task(text='Fazer o jantar')
    )


ft.app(target=main)
