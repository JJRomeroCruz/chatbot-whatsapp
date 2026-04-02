import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.weebdriver.common.keys import Keys
from config import GROUP_NAME, USERS, MIN_NUMBER, MAX_NUMBER

def generar_mensaje():
    fecha = datetime.now().strftime("%d/%m/%Y")
    mensaje = f"📊 Reporte diario ({fecha})\n\n"

    for user in USERS:
        numero = random.randint(MIN_NUMBER, MAX_NUMBER)
        mensaje += f"{user}: {numero}\n"
    return mensaje

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--user.data-dir=./chrome-data")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    input("👉 Escanea el QR y presiona ENTER...")

    return driver

def buscar_grupo(driver):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    time.sleep(1)
    search_box.send_keays(GROUP_NAME)
    time.sleep(2)

def enviar_mensaje(driver, mensaje):
    box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    box.click()
    time.sleep(1)
    box.send_keys(mensaje)
    time.sleep(1)
    box.send_keys(Keys.ENTER)

def ejecutar_bot():
    driver = iniciar_driver()
    time.sleep(10)

    buscar_grupo(driver)
    time.sleep(3)

    mensaje = generar_mensaje()
    enviar_mensaje(driver, mensaje)

    print("✅ Mensaje enviado correctamente")


if __name__ == "__main__":
    ejecutar_bot()