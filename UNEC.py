from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from webdriver_manager.chrome import ChromeDriverManager
import time

termDict = {
    '1': '1000105'
}

yearDict = {
    '1': '1000044'
}

examDict = {
    '1': ['20001063', '507']
}


service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_argument("--headless")
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)


driver.get("https://kabinet.unec.edu.az")


login = driver.find_element(By.XPATH, "//input[@class='user-l']")
login.send_keys("r.bayramov36")

password = driver.find_element(By.XPATH, "//input[@class='password-l']")
password.send_keys("WycS9qJ")

button = driver.find_element(By.XPATH, "//input[@type='submit']")
button.click()

exams = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='İmtahan nəticələri ']")))
exams.click()


year = driver.find_element(By.XPATH, "//select[@name='eyear']")
select_year = Select(year)

term = driver.find_element(By.XPATH, "//select[@name='term']")
select_term = Select(term)


year_input = input("Какой курс? ").strip()
term_input = input("Какой семестр? (1ый -> 1, 2-ой -> 2) ").strip()
exam_input = input("Какого типа экзамен? (Сессия -> 1, Коллоквиум -> 2) ").strip()

def result():
    select_year.select_by_value(yearDict[year_input])
    time.sleep(0.3)
    select_term.select_by_value(termDict[term_input])
    for i in examDict[exam_input]:
        examtype = driver.find_element(By.XPATH, "//select[@name='examType']")
        select_examtype = Select(examtype)
        select_examtype.select_by_value(i)
        results = driver.find_elements(By.XPATH, "//font[@color='#265325']")
        for result in results:
            print(result.text.strip())
result()
