import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.common import NoAlertPresentException #for negative alert exception

from FormFields_page import Form_Fields_page


@allure.description("Negative scenario. Application form")
def test_scenario_negative_1():
    work_url = "https://practice-automation.com/form-fields/"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=options, service=Service())
    driver.get(work_url)
    driver.maximize_window()

    print("\nStart positive scenario with form filling\n")

    ffp = Form_Fields_page(driver)

    try:
        ffp.check_current_location()

        #ffp.set_name()
        ffp.set_password()
        ffp.set_drink_1()
        ffp.set_drink_2()

        #ffp.set_color()
        color = ffp.get_color_set()
        driver.execute_script("arguments[0].click();", color)

        ffp.set_automation()
        ffp.set_email()

        ffp.list_parsing()
        ffp.set_message()

        #ffp.click_submit()
        submit = ffp.get_submit_bt()
        driver.execute_script("arguments[0].click();", submit)

        ffp.check_submit_form()

    except NoAlertPresentException as exception:
        ffp.except_for_negative()

    finally:
        time.sleep(4)
        driver.close()




#python -m pytest -s -v SS_SDET_tempProj/test_scenario_negative.py