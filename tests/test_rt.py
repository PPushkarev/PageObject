#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#


from pages.rt import MainPage
import pytest
from selenium import webdriver


# Фикстура для создания и закрытия драйвера
@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Устанавливаем размер окна браузера
    driver.set_window_size(1200, 800)
    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth')

    yield driver

    driver.quit()


    """Testing of Main Page"""
def test_main_page_default_check(driver):
    """ TEST 1 Check default Main Page status of type access"""
    page = MainPage(driver)
    page.phone_field.find()



def test_main_page_email_type(driver):
    """ TEST 2 Check how we can switch to email type access"""
    page = MainPage(driver)
    page.email_button.click()
    page.email_field.find()



def test_main_page_login_type(driver):
    """ TEST 3 Check how we can switch to login type access"""
    page = MainPage(driver)
    page.login_button.click()
    page.login_field.find()



def test_main_page_account_type(driver):
    """ TEST 4 Check how we can switch to account type access"""
    page = MainPage(driver)
    page.account_button.click()
    page.account_field.find()



def test_main_page_phone_type(driver):
    """ TEST 5 Check how we can switch to phone  type access back """
    page = MainPage(driver)
    page.phone_button.click()
    page.phone_field.find()


"""Testing Page of Authorization"""
def test_registration_by_email(driver):
    """ TEST 6 Register new user by Email"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = '2136823@gmail.com'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=30)

def test_registration_by_email_password_8_symbols(driver):
    """ TEST 7 Register new user by Email"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = '2136823@gmail.com'
    page.password = 'Ab455000'
    page.password_confirm = 'Ab455000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)


def test_registration_by_email_password_20_symbols(driver):
    """ TEST 8 Register new user by Email"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = '2136823@gmail.com'
    page.password = 'Ab455000000000000778'
    page.password_confirm = 'Ab455000000000000778'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)


def test_registration_by_phone(driver):
    """ TEST 9 Register new user by  Phone"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Виталий'
    page.lastname_field = 'Иванов'
    page.address = '79139856823'
    page.password = 'Ab455000sd'
    page.password_confirm = 'Ab455000sd'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=30)



def test_negative_registration_by_email_latin_name(driver):
    """ NEGATIVE TEST 10 Register new user by Email with latin NAME"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Aleksei'
    page.lastname_field = 'Пушкин'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    # Поиск ошибки на странице с помощью метода find
    page.name_error.find()

def test_negative_registration_by_email_latin_lastname(driver):
    """ NEGATIVE TEST 11 Register new user by Email with latin LASTNAME"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Pushkin'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    # Поиск ошибки на странице с помощью метода find
    page.lastname_error.find()

def test_negative_registration_by_email_name_over(driver):
    """ NEGATIVE TEST 12 Register new user by Email with long firstname"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексеййййййййййййййййййййййййййййййййййййййййййййййййййййййййййййййййййй'
    page.lastname_field = 'Пушкин'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.name_error.find()

def test_negative_registration_by_email_lastname_over(driver):
    """ NEGATIVE TEST 13 Register new user by Email with long lastname"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкинннннннннннннннннннннннннннннннннннннннннннннннннннннннннннннннн'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    # Поиск ошибки на странице с помощью метода find
    page.lastname_error.find()

def test_negative_registration_by_email_name_with_special_symbols(driver):
    """ NEGATIVE TEST 14 Register new user by Email with special symbols firstname"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = '{}()><$%^'
    page.lastname_field = 'Пушкин'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.name_error.find()

def test_negative_registration_by_email_lastname_with_special_symbols(driver):
    """ NEGATIVE TEST 15 Register new user by Email with special symbols lastname"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'у@{}()><$%^'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    # Поиск ошибки на странице с помощью метода find
    page.lastname_error.find()

def test_negative_registration_by_email_with_worng_email(driver):
    """ NEGATIVE TEST 16 Register new user by Email with wrong email with special symbols"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = '@{}()><$%'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.email_error.find()

def test_negative_registration_by_email_with_worng_phone_number(driver):
    """ NEGATIVE TEST 17 Register new user by Email with wrong phone with symbols over 12 """

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = '7915229162234'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.email_error.find()


def test_negative_registration_by_email_with_short_password(driver):
    """ NEGATIVE TEST 18 Register new user by Email with short password"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = 'peternsk@inbox.ru'
    page.password = '45'
    page.password_confirm = '45'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.password_error.find()

def test_negative_registration_by_email_with_password_that_do_not_match(driver):
    """ NEGATIVE TEST 19 Register new user by Email with different password"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Алексей'
    page.lastname_field = 'Пушкин'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000FG'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.password_check_error.find()

def test_registration_by_phone_user_already_exist(driver):
    """ TEST 20 Register user already exist by  Phone"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Виталий'
    page.lastname_field = 'Иванов'
    page.address = '79152291622'
    page.password = 'Ab455000sd'
    page.password_confirm = 'Ab455000sd'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=10)
    page.warning_user_exist.find()


def test_registration_by_email_secondtime(driver):
    """ TEST 21 Register user already exist by  Email"""

    page = MainPage(driver)
    page.register_button.click()
    page.firstname_field = 'Петр'
    page.lastname_field = 'Пушкарев'
    page.address = 'peternsk@inbox.ru'
    page.password = 'Ab45500000'
    page.password_confirm = 'Ab45500000'
    page.register_button_confirm.click()
    page.wait_page_loaded(sleep_time=30)
    page.warning_user_exist.find()



