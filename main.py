import time
import pytz
import logging
import warnings
from playwright.sync_api import sync_playwright
from controllers.conf import format_time_exec, time_converter

logging.getLogger('asyncio').setLevel(logging.INFO)
warnings.filterwarnings("ignore")

logging.Formatter.converter = time_converter(pytz.timezone('America/Mexico_City'))
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='log.log',
    filemode='w')

def main():
    inicio = time.time()
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.playwright.dev/python/")
        page.screenshot(path="output/test.png")
        browser.close()

    logging.info(format_time_exec(inicio))
    print('Done')

if __name__ == "__main__":
    main()