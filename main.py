from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pag
from time import sleep
from PIL import Image
import cv2
import pytesseract


def render_doc_text(file_path):
    img = cv2.imread(file_path, 0)
    img = Image.fromarray(img)

    result = pytesseract.image_to_string(img, lang="eng")

    return result


driver = webdriver.Chrome()

driver.get("https://sushida.net/")

consent_button = pag.center(pag.locateOnScreen("./images/consent.png"))
pag.click(consent_button.x - 780, consent_button.y - 780)

sleep(3)

start = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a[1]/img')
start.click()

sleep(7)

setting_button = pag.center(pag.locateOnScreen("./images/setting.png"))

start_button = pag.click(setting_button.x - 600, setting_button.y - 760)

sleep(3)

price_button = pag.click(setting_button.x - 600, setting_button.y - 700)

sleep(3)

pag.press("space")

sleep(3)

while 1:
    game = driver.find_element(By.XPATH, '//*[@id="#canvas"]')
    game.screenshot("./images/image.png")
    im = Image.open("./images/image.png")
    im.crop((70, 230, 450, 260)).save("./images/image.png", quality=95)
    string = render_doc_text("./images/image.png")
    pag.write(string)
