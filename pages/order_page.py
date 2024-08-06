import allure
from pages.base_page import BasePage
from utils.locators import *


class OrderPage(BasePage):
    @allure.step('Заполнение поля Имя')
    def send_first_name(self, first_name):
        self.find_element(OrderPageLocators.first_name_input).send_keys(first_name)

    @allure.step('Заполнение поля Фамилия')
    def send_last_name(self, last_name):
        self.find_element(OrderPageLocators.last_name_input).send_keys(last_name)

    @allure.step('Заполнение поля Адрес')
    def send_address_name(self, delivery_address):
        self.find_element(OrderPageLocators.delivery_address_input).send_keys(delivery_address)

    @allure.step('Клик по полю метро')
    def click_metro_input(self):
        self.click_element(OrderPageLocators.metro_station_input)

    @allure.step('Выбор станции метро')
    def click_metro_button(self, metro_station):
        self.click_element(OrderPageLocators.metro_station_button(metro_station))

    @allure.step('Заполнение поля Телефон')
    def send_phone_name(self, user_phone):
        self.find_element(OrderPageLocators.user_phone_input).send_keys(user_phone)

    @allure.step('Клик по кнопке Далее')
    def click_in_button_next(self):
        self.click_element(OrderPageLocators.next_button)

    @allure.step('Заполнение даты доставки')
    def send_delivery_date(self, delivery_date):
        self.find_element(OrderPageLocators.delivery_date_input).send_keys(delivery_date)

    @allure.step('Клик по выпадающему списку срока аренды')
    def click_in_rental_period_input(self):
        self.click_element(OrderPageLocators.rental_period_drop_down_list)

    @allure.step('Клик по кнопке выпадающего списка срока аренды (сколько дней)')
    def click_in_rental_period_button(self, qnt_day):
        self.click_element(OrderPageLocators.fill_dropdown_list(qnt_day))

    @allure.step('Выбор цвета самоката')
    def click_in_checkbox_change_color(self, color):
        self.click_element(OrderPageLocators.input_checkbox_color(color))

    @allure.step('Заполнение поля комментарий')
    def send_in_comment(self, comment):
        self.find_element(OrderPageLocators.comment_input_for_delivery).send_keys(comment)

    @allure.step('Клик по кнопке Заказать')
    def click_in_order_button_in_order(self):
        self.click_element(OrderPageLocators.order_button_in_order)

    @allure.step('Получение текста')
    def getting_text_in_order_popup(self):
        text_in_popup = self.find_element(OrderPageLocators.finish_title_in_order).text
        return text_in_popup
