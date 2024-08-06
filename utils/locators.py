from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы для работы с домашней страницей"""

    cookie_button = [By.XPATH, ".//button[text()='да все привыкли']"]  # да все привыкли(кнопка принятия кук)
    order_button_in_header = [By.XPATH,
                              ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]  # кнопка заказа в хедере
    order_button_in_main = [By.XPATH,
                            ".//div[starts-with(@class, 'Home')]/button[(text()='Заказать')]"]  # кнопка заказа в майн
    logo_scooter_in_header = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"] #логотип Яндекс Самокат
    logo_yandex_in_header = [By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"] #логотип Яндекс
    questions_section = [By.XPATH, ".//div[starts-with(@class, 'Home_FAQ')]"] # раздел FAQ
    logo_dzen = [By.XPATH, ".//div[starts-with(@class, 'desktop-base-header')]"] # логотип Яндекс Дзен


class OrderPageLocators:
    """Локаторы для работы со страницей заказа самоката"""

    title_in_order_page = [By.XPATH, ".//div[text()='Для кого самокат']"] # Заголовок на 1 страницы заказа
    first_name_input = [By.XPATH, ".//input[@placeholder='* Имя']"] # Поля ввода Имя
    last_name_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"] # Поля ввода Фамилия
    delivery_address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"] # Поля ввода адреса
    metro_station_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"] # Поля ввода станции метро
    list_metro_station = [By.XPATH, ".//div[@class='select-search__select']"] # Список станций метро
    user_phone_input = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"] # Поля ввода телефона
    next_button = [By.XPATH, ".//button[text()='Далее']"] # Кнопка далее на 1 странице заказа
    title_rent_in_order_page = [By.XPATH, ".//div[text()='Про аренду']"] # Заголовок на 2 странице заказа
    delivery_date_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"] # Поля ввода даты
    rental_period_drop_down_list = [By.XPATH, ".//div[starts-with(@class, 'Dropdown-root')]"]  # Выпадающий список с кол-вом дней аренды
    comment_input_for_delivery = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"] # Поля ввода комментарий
    back_button = [By.XPATH, ".//button[text()='Назад']"] # Кнопка Назад
    order_button_in_order = [By.XPATH, ".//div[starts-with(@class, 'Order')]/button[text()='Заказать']"] # Кнопка Заказа
    question_title_in_order = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"] # Заголовок в попап окне
    quest_button_no_in_order = [By.XPATH, ".//button[text()='Нет']"] # Кнопка Нет в попап окне
    quest_button_yes_in_order = [By.XPATH, ".//button[text()='Да']"] # Кнопка Да в попап окне
    finish_title_in_order = [By.XPATH, ".//div[text()='Заказ оформлен']"] # Заголовок об успешном оформлении заказа
    view_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"] # Кнопка просмотра заказа

    @staticmethod
    def metro_station_button(name_metro: str): #Выбор станции метро из представленного списка
        metro_name = [By.XPATH,
                      f".//div[starts-with(@class, 'Order') and text()='{name_metro}']/parent::button[starts-with(@class, 'Order')]"]
        return metro_name

    @staticmethod
    def fill_dropdown_list(qnt_day: str):  # Выбор из списка кол-ва дней
        return [By.XPATH, f".//div[@class='Dropdown-option' and text()='{qnt_day}']"]

    @staticmethod
    def input_checkbox_color(name_color: str):  # Чекбокс по выбору цвета
        return [By.XPATH, f".//input[@id='{name_color}']"]


class QuestionPageLocators:
    """Локаторы раздела FAQ"""

    quest_title = [By.XPATH, "//div[text()='Вопросы о важном']"]  # Заголовок раздела вопросы о важном

    @staticmethod
    def buttons_questions(number: str): # Кнопка выпадающего списка вопроса
        number_question = [By.XPATH, f"//div[@class='accordion__button' and @id='accordion__heading-{number}']"]
        return number_question

    @staticmethod
    def answer_question(number: str): # Ответ на вопрос
        answer_question = [By.XPATH, f"//div[@class='accordion__panel' and @id='accordion__panel-{number}']/p"]
        return answer_question
