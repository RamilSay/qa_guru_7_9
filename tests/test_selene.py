import allure
from selene.support.shared import browser


def test_github():
    with allure.step("Открываем главую страницу GitHub")
        browser.open("https://github.com")

