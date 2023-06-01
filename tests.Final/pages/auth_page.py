from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    username_input = WebElement(id='username')
    phone_button = WebElement(id='t-btn-tab-phone')
    email_button = WebElement(id='t-btn-tab-mail')
    login_button = WebElement(id='t-btn-tab-login')
    ls_button = WebElement(id='t-btn-tab-ls')
    forgot_password_button = WebElement(id='forgot_password')
    password_input = WebElement(id='password')
    reg_button = WebElement(id='kc-register')
    go_button = WebElement(id='kc-login')
    lk_button = WebElement(id='lk-btn')
    error = WebElement(id='form-error-message')
    forgot_password_text = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/h1[1]')
    regestrion_text = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/h1[1]')
    reg_name = WebElement(name='firstName')
    reg_surname = WebElement(name='lastName')
    reg_email = WebElement(xpath='//*[@id="address"]')
    reg_password1 = WebElement(id='password')
    reg_password2 = WebElement(id='password-confirm')
    reg_confrim = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
    name_error = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    surname_error = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
    email_error = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]')
    password_nowords = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]')
    password_wrong12 = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]')
    anounce = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/h2[1]')
    button_go_to_login = WebElement(name='gotoLogin')
    button_go_to_password = WebElement(id='reg-err-reset-pass')
    confrim_user = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/a[1]')
