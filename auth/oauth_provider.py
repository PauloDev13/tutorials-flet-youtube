import os

import flet as ft
from flet.auth.providers import GitHubOAuthProvider


def main(page: ft.Page) -> None:
    provider = GitHubOAuthProvider(
        client_id=os.getenv('GITHUB_CLIENT_ID'),
        client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
        redirect_url='http://localhost:8550/oauth/redirect',
    )

    def login_button_click(e) -> None:
        page.login(provider, scope=['public_repo'])

    def on_login(e: ft.LoginEvent):
        if not e.error:
            toggle_login_buttons()

    def logout_button_click(e) -> None:
        page.logout()

    def on_logout(e):
        toggle_login_buttons()

    def toggle_login_buttons() -> None:
        login_button.visible = page.auth is None
        logout_button.visible = page.logout is None
        page.update()

    login_button = ft.ElevatedButton(
        text='Login com GitHub',
        on_click=login_button_click,
    )

    logout_button = ft.ElevatedButton(
        text='Logout',
        on_click=logout_button_click,
    )

    toggle_login_buttons()
    page.on_login = on_login
    page.on_logout = on_logout
    page.add(login_button, logout_button)


ft.app(target=main, port=8550, view=ft.AppView.WEB_BROWSER)
