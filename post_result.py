import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def post_result(white, black, outcome):
    driver = webdriver.Chrome()
    driver.get("https://swissonlinetournament.com/Identity/Account/Login")
    email_input = driver.find_element(By.CSS_SELECTOR, "input[name='Input.Email']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='Input.Password']")
    email_input.send_keys(config.username)
    password_input.send_keys(config.password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    driver.get('https://swissonlinetournament.com/Tournament/Details/' + config.tournament)
    xpath1 = '//tr[contains(td[2], "{}") and contains(td[6], "{}")]'.format(white, black)
    game_elements = driver.find_elements(By.XPATH, xpath1)

    if(game_elements == []):
        driver.quit()
        return -1
    game_element = game_elements[0]
    dropdown = game_element.find_element(By.CSS_SELECTOR, 'a.pair-result')
    dropdown.click()
    xpath2 = f"//a[@data-value='{outcome}']"
    option = driver.find_element(By.XPATH, xpath2)
    option.click()
    time.sleep(5)
    driver.quit()

# if __name__ == "__main__":
#     post_result(<white username>, <black username>, <Win/Draw/Loss>)
