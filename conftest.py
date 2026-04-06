"""Конфигурация тестов и кастомные опции pytest"""
import os
import pytest


def pytest_addoption(parser):
    """Добавление кастомных аргументов командной строки"""
    parser.addoption(
        "--br",
        action="store",
        default="chromium",
        help="Browser: chromium, firefox, webkit",
    )
    parser.addoption(
        "--app",
        default=None,
        help="Path to mobile app file (.apk for Android, .app/.ipa for iOS)",
    )
    parser.addoption(
        "--allure-print",
        action="store_true",
        default=True,
        help="Включить вывод шагов Allure в консоль.",
    )
    parser.addoption(
        "--locale",
        action="store",
        default="en",
        help="Locale to run tests in (e.g. en, ru).",
    )


@pytest.fixture(scope="session")
def browser_context_args():  # Убрали аргумент из скобок
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


@pytest.fixture(scope="session")
def test_config():
    return {
        "base_url": os.getenv("BASE_URL"),
        "admin_url": f"{os.getenv('BASE_URL')}/admin",
        "admin_creds": (os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD")),
        "user_creds": (os.getenv("USER_EMAIL"), os.getenv("USER_PASSWORD")),
    }
