from django.conf.urls import url
from objectpack import desktop

from app.actions import UserPack
from app.controller import controller


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экшен-паков
    """
    return controller.packs.extend([UserPack()])


def register_desktop_menu():
    """
    Регистрация элементов рабочего стола
    """
    desktop.uificate_the_controller(
        controller, menu_root=desktop.MainMenu.SubMenu("Demo")
    )
