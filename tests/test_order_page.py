import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage
from utils.locators import *
from utils.links import *
from utils.test_data import finish_title_in_order_popup
from utils.test_data import test_cases_data


class TestOrderPage:
    @allure.title('Проверка возможности заказать самокат')
    @pytest.mark.parametrize('test_data,order_button', [
        (test_cases_data[0], HomePageLocators.order_button_in_main),
        (test_cases_data[1], HomePageLocators.order_button_in_header)
    ])
    def test_order_page_show_finish_title(self, driver_setup, test_data, order_button):
        order_page = OrderPage(driver_setup)
        order_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            HomePageLocators.cookie_button))
        order_page.click_element(HomePageLocators.cookie_button)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            QuestionPageLocators.quest_title))
        order_page.scroll_to_element(QuestionPageLocators.quest_title)
        order_page.click_element(HomePageLocators.order_button_in_main)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.
                                                                                               title_in_order_page))
        order_page.send_first_name(test_data.get('first_name'))
        order_page.send_last_name(test_data.get('last_name'))
        order_page.send_address_name(test_data.get('adress'))
        order_page.click_metro_input()
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.
                                                                                               list_metro_station))
        order_page.click_metro_button(test_data.get('metro_station'))
        order_page.send_phone_name(test_data.get('phone_user'))
        order_page.click_in_button_next()
        WebDriverWait(driver_setup, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.title_rent_in_order_page))
        order_page.send_delivery_date(test_data.get('delivery_date'))
        order_page.click_element(OrderPageLocators.title_rent_in_order_page)
        order_page.click_in_rental_period_input()
        WebDriverWait(driver_setup, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.rental_period_drop_down_list))
        order_page.click_in_rental_period_button(test_data.get('rental_period'))
        order_page.click_in_checkbox_change_color(test_data.get('color_scooter'))
        order_page.send_in_comment(test_data.get('comment'))
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.
                                                                                               order_button_in_order))
        order_page.click_in_order_button_in_order()
        WebDriverWait(driver_setup, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.question_title_in_order))
        order_page.click_element(OrderPageLocators.quest_button_yes_in_order)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.
                                                                                               finish_title_in_order))
        assert finish_title_in_order_popup in order_page.getting_text_in_order_popup()
        driver_setup.quit()
