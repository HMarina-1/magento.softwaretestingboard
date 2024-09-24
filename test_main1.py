import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure

# Constants
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "hovmarina1981@gmail.com"
PASSWORD = "marina123!."
NEW_PASSWORD = "marina123!."


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.feature('Login Tests')
@allure.suite('Invalid Login Test Suite')
@allure.title('Test invalid login')
@allure.description('This test tries to log in with an invalid email and password and checks the error message.')
@allure.severity('critical')
@pytest.mark.regression
def test_invalid_login(driver):
    with allure.step('Open login page'):
        driver.get(LOGIN_URL)

    with allure.step('Enter invalid email'):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@gmail.com")

    with allure.step('Enter invalid password'):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys("invalidpassword")

    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step('Verify error message'):
        time.sleep(3)  # Wait for the page to load
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "Please wait and try again later" in error_message.text


@allure.feature('Login Tests')
@allure.suite('Valid Login Test Suite')
@allure.title('Test valid login')
@allure.description('This test logs in with valid credentials and checks the account URL.')
@allure.severity('critical')
@pytest.mark.smoke
def test_login(driver):
    with allure.step('Open login page'):
        driver.get(LOGIN_URL)

    with allure.step('Enter valid email'):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(EMAIL)

    with allure.step('Enter valid password'):
        password = driver.find_element(By.ID, "pass")
        password.send_keys(PASSWORD)

    with allure.step('Click login button'):
        button = driver.find_element(By.ID, "send2")
        button.click()

    with allure.step('Verify the URL is the account page'):
        time.sleep(3)
        assert driver.current_url == ACCOUNT_URL


@allure.feature('Password Change Tests')
@allure.suite('Password Change Error Handling')
@allure.title('Test incorrect current password')
@allure.description(
    'This test tries to change the password with an incorrect current password and verifies the error message.')
@allure.severity('major')
@pytest.mark.regression
def test_change_password_incorrect_current(driver):
    with allure.step('Open account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Click change password link'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter incorrect current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Confirm new password'):
        confirm_new_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Click save button'):
        button_save = driver.find_element(By.XPATH, "//button[@title='Save']")
        button_save.click()

    with allure.step('Verify error message'):
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "The password doesn't match this account." in error_message.text


@allure.feature('Password Change Tests')
@allure.suite('Password Change Error Handling')
@allure.title('Test password mismatch')
@allure.description(
    'This test tries to change the password where new passwords do not match and verifies the error message.')
@allure.severity('major')
@pytest.mark.regression
def test_change_password_mismatch(driver):
    with allure.step('Open account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Click change password link'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Enter mismatching password confirmation'):
        confirm_new_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_new_password_input.send_keys("mistakes")

    with allure.step('Click save button'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify password mismatch error'):
        error_message = driver.find_element(By.ID, "password-confirmation-error")
        assert "Please enter the same value again." in error_message.text


@allure.feature('Password Change Tests')
@allure.suite('Successful Password Change')
@allure.title('Test successful password change')
@allure.description('This test changes the password successfully and verifies the success message.')
@allure.severity('critical')
@pytest.mark.regression
def test_change_password(driver):
    with allure.step('Open account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Click change password link'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Confirm new password'):
        confirm_new_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Click save button'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify success message'):
        success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")
        assert "You saved the account information." in success_message.text
