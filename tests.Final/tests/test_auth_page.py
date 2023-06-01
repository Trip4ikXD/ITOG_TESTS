import pytest
import time
from pages.auth_page import AuthPage
from pages.elements import WebElement

def test_authorisation_phone(web_browser):   #Тест1. Авторизация через телефон
    page = AuthPage(web_browser)
    page.phone_button.click()
    page.username_input.send_keys('79101501033')
    page.password_input.send_keys("313513137Aa")
    page.go_button.click()
    time.sleep(5)
    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()

def test_authorisation_email(web_browser):            #Тест2. Автроризация через почту.
    page = AuthPage(web_browser)

    page.email_button.click()
    page.username_input.send_keys('lyskovich228@gmail.com')

    page.password_input.send_keys("313513137Aa")

    page.go_button.click()
    time.sleep(5)
    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()


def test_authorisation_login(web_browser):              #Тест3. Авторизация через логин
    page = AuthPage(web_browser)

    page.login_button.click()
    page.username_input.send_keys('rtkid_1685381747507')

    page.password_input.send_keys("313513137Aa")

    page.go_button.click()

    time.sleep(5)

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()

def test_authorisation_wrongusername_negative(web_browser):   #Тест4.Негативный.Неверный логин, вход не состоится.

    page = AuthPage(web_browser)
    page.phone_button.click()
    page.username_input.send_keys('79101501033')
    page.password_input.send_keys("313513137A")
    page.go_button.click()
    assert page.error.is_visible() == True

def test_authorisation_fogotpossword(web_browser):      #Тест5. Кнопка забыла пароль переводит на нужную страницу. ( Не знаю как сделать подвтерждение телефона, поэтому проверяю нахождение на странице.)
    page = AuthPage(web_browser)
    page.forgot_password_button.click()
    assert page.forgot_password_text.is_visible() == True


def test_authorisation_passsword_wrong_negative(web_browser):     #Тест6. Неверный пароль, при верном логине/почте/номеру.
    page = AuthPage(web_browser)
    page.phone_button.click()
    page.username_input.send_keys('lyskovich228@gmail.com')
    page.password_input.send_keys("313513137")
    page.go_button.click()
    assert page.error.is_visible() == True

def test_authorisation_registrion_page(web_browser): # Тест7. Кнопка регестрации переводит на нужную страницу.

    page = AuthPage(web_browser)
    page.reg_button.click()
    assert page.regestrion_text.is_visible() == True

def test_authorisation_registrion(web_browser):    #Тест8. Страница регестрирует НЕзарегестрированный(номер/почту).(Ввести нерегистрированную почту).
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('313513137Aaa')
    page.reg_password2.send_keys('313513137Aaa')
    page.reg_confrim.click()
    assert 'https://b2c.passport.rt.ru/auth' in page.get_current_url()


def test_authorisation_reg_negative_1_name(web_browser):    #Тест9. Страница выдает ошибку при неправильном вводе имени.
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Л')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('313513137Aaa')
    page.reg_password2.send_keys('313513137Aaa')
    page.reg_confrim.click()
    assert page.name_error.is_visible() == True

def test_authorisation_reg_negative_2_surnname(web_browser):    #Тест10. Страница выдает ошибку при неправильном вводе Фамилии.
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Л')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('313513137Aaa')
    page.reg_password2.send_keys('313513137Aaa')
    page.reg_confrim.click()
    assert page.surname_error.is_visible() == True


def test_authorisation_reg_negative_3_phone_email(web_browser):    #Тест11. Страница выдает ошибку при вводе некорректной почты/телефона.
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('11111')
    page.reg_password1.send_keys('313513137Aaa')
    page.reg_password2.send_keys('313513137Aaa')
    page.reg_confrim.click()
    assert page.email_error.is_visible() == True



def test_authorisation_reg_negative_4_wrongpassword(web_browser):    #Тест11. Страница выдает ошибку при некорректном вводе пароля. Без букв.
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('11111111')
    page.reg_password2.send_keys('11111111')
    assert page.password_nowords.is_visible() == True


def test_authorisation_reg_negative_5_wrongpassword2(web_browser):    #Тест12. Страница выдает ошибку при неодинаковых паролях.
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('313513137AaA')
    page.reg_password2.send_keys('2222222228AaA')
    page.reg_confrim.click()

    assert page.password_wrong12.is_visible() == True

def test_test_authorisation_old_account(web_browser): #Тест13. Страница даст выбор,что делать дальше,если аккаунт уже зарегестрирован
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('lyskovich228@gmail.com')
    page.reg_password1.send_keys('313513137AaA')
    page.reg_password2.send_keys('313513137AaA')
    page.reg_confrim.click()
    time.sleep(5)
    assert page.anounce.is_visible() == True

def test_test_authorisation_old_account_join(web_browser): #Тест14. Выбираем на странице Войти, и убеждаемся , что она переводит на страницу авторизации
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('lyskovich228@gmail.com')
    page.reg_password1.send_keys('313513137AaA')
    page.reg_password2.send_keys('313513137AaA')
    page.reg_confrim.click()
    time.sleep(5)
    page.button_go_to_login.click()
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate' in page.get_current_url()

def test_test_authorisation_old_account_reset(web_browser): #Тест15. Выбираем на странице Восстановить пароль, и убеждаемся , что она переводит на страницу авторизации
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('lyskovich228@gmail.com')
    page.reg_password1.send_keys('313513137AaA')
    page.reg_password2.send_keys('313513137AaA')
    page.reg_confrim.click()
    time.sleep(5)
    page.button_go_to_password.click()
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials' in page.get_current_url()



def test_authorisation_reg_negative_4_wrongpassword3(web_browser):    #Тест16. Пароль должен выдать ошибку. Только с заглавной буквой
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('11111111A')
    page.reg_password2.send_keys('11111111A')
    assert page.password_nowords.is_visible() == True

def test_authorisation_reg_negative_4_wrongpassword4(web_browser):    #Тест17. Пароль должен выдать ошибку. С строчной буквой
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('11111111a')
    page.reg_password2.send_keys('11111111a')
    assert page.password_nowords.is_visible() == True

def test_authorisation_confrim_users(web_browser):    #Тест18. Авторизация через лицевой счет.
    page = AuthPage(web_browser)
    page.ls_button.click()
    page.username_input.send_keys('')  # Нужно ввести лицевой счет, у меня его нет, так как нет услуг ростелекома
    page.password_input.send_keys('')  # Пароль с лицевым счетом
    page.go_button.click()
    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()

def test_authorisation_reg_negative_2_surnname2(web_browser):    #Тест10. Страница выдает ошибку при неправильном вводе Фамилии.Латинские буквы
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Максим')
    page.reg_surname.send_keys('Lyskovich')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('313513137Aaa')
    page.reg_password2.send_keys('313513137Aaa')
    page.reg_confrim.click()
    assert page.surname_error.is_visible() == True

def test_authorisation_reg_negative_1_name2(web_browser):    #Тест20. Страница выдает ошибку при неправильном вводе имени. Латинские буквы
    page = AuthPage(web_browser)
    page.reg_button.click()
    page.reg_name.send_keys('Maksim')
    page.reg_surname.send_keys('Лыскович')
    page.reg_email.send_keys('mlyskovich@mail.ru')
    page.reg_password1.send_keys('313513137Aaa')
    page.reg_password2.send_keys('313513137Aaa')
    page.reg_confrim.click()
    assert page.name_error.is_visible() == True































