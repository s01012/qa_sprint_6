import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from utils.locators import *
from utils.links import *


class TestBasePage:
    @allure.title('Проверка перехода на сайт dzen.ru из главной страницы')
    def test_transition_to_dzen_click_on_logo_ya_identical_url_value(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            HomePageLocators.logo_yandex_in_header))
        home_page.click_logo_yandex_in_button()
        WebDriverWait(driver_setup, 10).until(expected_conditions.number_of_windows_to_be(2))
        driver_setup.switch_to.window(driver_setup.window_handles[-1])
        WebDriverWait(driver_setup, 10).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.logo_dzen))
        current_url = home_page.current_url()
        assert Links.yandex_dzen in current_url

    @allure.title('Проверка перехода на главную страницу из страницы заказа')
    def test_transition_to_main_click_on_logo_identical_url_value(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.order_page)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            HomePageLocators.logo_scooter_in_header))
        home_page.click_logo_scooter_in_button()
        current_url = home_page.current_url()
        assert current_url == Links.main_page

    @allure.title('Проверка перехода на страницу заказа из главной страницы, если нажать кнопку Заказать в хедере')
    def test_transition_to_order_click_on_button_header_identical_url_value(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            HomePageLocators.cookie_button))
        home_page.click_order_button_in_header()
        current_url = home_page.current_url()
        assert current_url == Links.order_page

    @allure.title('Проверка перехода на страницу заказа из главной страницы, если нажать кнопку Заказать в мейн')
    def test_transition_to_order_click_on_button_main_identical_url_value(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            HomePageLocators.cookie_button))
        home_page.click_element(HomePageLocators.cookie_button)
        home_page.scroll_to_element()
        home_page.click_order_button_in_main()
        assert home_page.current_url() == Links.order_page
