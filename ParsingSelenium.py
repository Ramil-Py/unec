from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time, os

service = Service("/Users/ramil/Documents/Education/Programming/Drivers/chromedriver 01-41-43-955")
options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"
options.add_argument("--headless")
# options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15")
# prefs = {
#     "download.default_directory": f"{os.getcwd()}"
# }
# options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

for n in range(1,143):
    driver.get(f"https://flowwow.com/moscow/cakes/page-{n}/?cake_sort=1")
    links = driver.find_elements(By.XPATH, "//div[@class='tab-content-products']//a")

    for i in range(len(links)):
        links[i] = links[i].get_attribute("href")

    for link in links:
        try:
            print(link)
            driver.get(link)
            VISIBILITY = (By.CLASS_NAME, "shop-rating")
            wait.until(ec.visibility_of_element_located(VISIBILITY))
            name = driver.find_element(By.TAG_NAME, "h1").text.strip()
            price = driver.find_element(By.CLASS_NAME, "footer-price").text.strip().replace("\n", "")
            review = driver.find_element(By.CLASS_NAME, "review-count").text.strip().split()[0].replace("\n", "")
            weight = driver.find_element(By.CLASS_NAME, "property-text").text.strip().replace("\n", "")
            shop = driver.find_element(By.CLASS_NAME, "shop-name").text.strip().replace("\n", "")
            rating = driver.find_element(By.CLASS_NAME, "shop-rating").text.strip().split()[0].replace("\n", "")
            score = driver.find_element(By.CLASS_NAME, "shop-score").text.strip().split()[0].replace("\n", "")
            buy = driver.find_element(By.CLASS_NAME, "shop-score").text.strip().split()[3]
            storelink = driver.find_element(By.CLASS_NAME, "shop-link").get_attribute("href").strip()
            img = driver.find_element(By.TAG_NAME, "img").get_attribute("src").strip().replace("\n", "")
        
        except Exception as e:
            continue

        print(name, price, review, weight, shop, rating, score, buy, storelink, img, sep=" | ")