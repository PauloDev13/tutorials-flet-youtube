import flet as ft

import time


def main(page: ft.Page):
    image = ft.Image(
        src='https://picsum.photos/200/200',
        width=200,
        height=200,
    )

    def animate(e):
        sw.content = ft.Image(
            src=f'https://picsum.photos/200/200?{time.time()}',
            width=200,
            height=200,
        )
        page.update()

    sw = ft.AnimatedSwitcher(
        image,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    page.add(
        sw,
        ft.ElevatedButton(text='Animate', on_click=animate),
    )


ft.app(target=main)
