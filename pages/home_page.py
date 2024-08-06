import allure
from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):
    @allure.step('Закрыть всплывающее окно принятия куки, нажатием кнопки "Да все привыкли!"')
    def click_cookie_button(self):
        self.click_element(HomePageLocators.cookie_button)

    @allure.step('Кликнуть по логотипу Яндекс - для перехода на dzen.ru')
    def click_logo_yandex_in_button(self):
        self.click_element(HomePageLocators.logo_yandex_in_header)

    @allure.step('Кликнуть по логотипу Самокат - для перехода на главную страницу')
    def click_logo_scooter_in_button(self):
        self.click_element(HomePageLocators.logo_scooter_in_header)

    @allure.step('Нажать на пноку "Заказать" в хедере')
    def click_order_button_in_header(self):
        self.click_element(HomePageLocators.order_button_in_header)

    @allure.step('Нажать на кнопку "Заказать" в мейн')
    def click_order_button_in_main(self):
        self.click_element(HomePageLocators.order_button_in_main)

    @allure.step('Скроллит до заголовка раздела с вопросами')
    def scroll_to_element(self):
        quest_title_element = self.driver_setup.find_element(*QuestionPageLocators.quest_title)
        self.driver_setup.execute_script("arguments[0].scrollIntoView(true);", quest_title_element)

    @allure.step('Расскрыть вопрос в разделе FAQ')
    def click_buttons_questions(self, number_question):
        self.click_element(QuestionPageLocators.buttons_questions(number_question))

    @allure.step('Получение текста')
    def getting_text_in_questions(self, number_answer):
        text_in_answer = self.find_element(QuestionPageLocators.answer_question(number_answer)).text
        return text_in_answer
