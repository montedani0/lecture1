import flet as ft

from gestionale.controller import Controller
from gestionale.view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.set_controller(c)
    v.carica_interfaccia()

ft.app(target=main)