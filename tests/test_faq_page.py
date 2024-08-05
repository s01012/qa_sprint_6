import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from utils.locators import *
from utils.test_data import AnswersToQuestions
from utils.links import *


class TestFaqPage:
    @allure.title('Проверка идентичности ответов в разделе FAQ')
    @pytest.mark.parametrize(
        'question,answer,expected_result',
        [
            [0, 0, AnswersToQuestions.answer_1],
            [1, 1, AnswersToQuestions.answer_2],
            [2, 2, AnswersToQuestions.answer_3],
            [3, 3, AnswersToQuestions.answer_4],
            [4, 4, AnswersToQuestions.answer_5],
            [5, 5, AnswersToQuestions.answer_6],
            [6, 6, AnswersToQuestions.answer_7],
            [7, 7, AnswersToQuestions.answer_8]
        ]
    )
    def test_faq_click_to_question_display_answer(self, driver_setup, question, answer, expected_result):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            HomePageLocators.cookie_button))
        home_page.click_cookie_button()
        WebDriverWait(driver_setup, 3).until(expected_conditions.visibility_of_element_located(
            QuestionPageLocators.quest_title))
        home_page.scroll_to_element()
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                questions_section))
        WebDriverWait(driver_setup, 10).until(expected_conditions.element_to_be_clickable(QuestionPageLocators.
                                                                                          buttons_questions(question)))
        home_page.click_buttons_questions(question)
        answer_to_question = home_page.getting_text_in_questions(answer)
        assert answer_to_question == expected_result
        driver_setup.quit()
