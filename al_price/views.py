import re
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from .models import Settings

def get_allegro_price(request, ean):
    print('get_allegro_price')

    sett = Settings.objects.last().allegro_path
    url = sett.format(ean)

    browser = load_driver()

    for i in range(3):
        try:
            browser.get(url)
            break
        except:
            continue
    try:
        priceAllegro = getPrice(browser)
    except:
        priceAllegro = 0
    browser.close()
    return JsonResponse({ 
                    'priceAllegro': priceAllegro,
                })

def getPrice(browser):
    print('getPrice')
    price = 0
    all_links = browser.find_elements(By.TAG_NAME, 'article')
    for i in all_links:
        spans = i.find_elements(By.TAG_NAME, 'span')
        for a in spans:
            priceLable = a.get_attribute('aria-label')
            if priceLable is not None:
                try:
                    value = float(re.findall(r"[-+]?\d*\.\d+|\d+", str(priceLable).replace(',', '.'))[0])
                    if price == 0:
                        price = value
                    elif value < price:
                        price = value
                except:
                    continue
    return price

def  load_driver():
    firefox_dev_binary = FirefoxBinary('/opt/firefox/firefox')
    executable_path = 'drivers/geckodriver.log'
    log_path='/var/www/AP/geckodriver.log'
    opts = FirefoxOptions()
    opts.add_argument('--headless')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    browser = webdriver.Firefox(firefox_binary=firefox_dev_binary, executable_path=executable_path, options=opts, service_log_path=log_path)
    return browser

try:
    if Settings.objects.all().count() == 0:
        Settings.objects.create()
except:
    pass