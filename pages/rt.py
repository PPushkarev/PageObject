#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement



class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/auth'

        super().__init__(web_driver, url)

# MAin page
    #  phone type acess switcher
    phone_button = WebElement(id ='t-btn-tab-phone')
    # email type acess
    email_button = WebElement(id='t-btn-tab-mail')
    # login type acess
    login_button = WebElement(id='t-btn-tab-login')
    # account type acess
    account_button = WebElement(id='t-btn-tab-ls')

    # type of acess field
    phone_field= WebElement(xpath ='//span[@class="rt-input__placeholder" and contains(text(), "Мобильный телефон")]')
    email_field = WebElement(xpath='//span[@class="rt-input__placeholder" and contains(text(), "Электронная почта")]')
    login_field = WebElement(xpath='//span[@class="rt-input__placeholder" and contains(text(), "Логин")]')
    account_field = WebElement(xpath='//span[@class="rt-input__placeholder" and contains(text(), "Лицевой счёт")]')


    # register button
    register_button = WebElement(id='kc-register')


    # firstname field
    firstname_field = WebElement(name ='firstName')
    # lastname field
    lastname_field = WebElement(name ='lastName')
    # email field
    address = WebElement(id ='address')
    # password field
    password = WebElement(id ='password')
    # password confirmation
    password_confirm = WebElement(id ='password-confirm')
    # register button confirmation
    register_button_confirm = WebElement(name ='register')




    # ERRORS
    # # user already exist
    # user_exist = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/div/h2')
    # error name
    name_error = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span')
    # error withlastname
    lastname_error = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span')
    # error that email is worng
    email_error = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span')
    # short password
    password_error =WebElement(xpath= '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span')
    # pasword do not match
    password_check_error = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')


    # Warnings
    # user exist
    warning_user_exist = WebElement(xpath="//h2[@class='card-modal__title' and contains(text(), 'Учётная запись уже существует')]")




