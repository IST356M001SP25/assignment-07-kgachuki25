from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, timeout = 60000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.archive.org/web/20241111165815/https://www.tullysgoodtimes.com/menus/")

    # List of dicts for each extracted item:
    extracted_items = []

    # Looping through each section/title of the menu:
    for title in page.query_selector_all("h3.foodmenu__menu-section-title"):
        title_name = title.inner_text()
        next_element = title.query_selector("~ *")
        menu_items = next_element.query_selector("~ *")
        # Loop through each item in the section:
        for item in menu_items.query_selector_all("div.foodmenu__menu-item"):
            text = item.inner_text()
            menu_item = extract_menu_item(title_name, text)
            item_dict = menu_item.to_dict()
            extracted_items.append(item_dict)

    menu_df = pd.DataFrame(extracted_items)
    menu_df.to_csv("cache/tullys_menu.csv", index = False)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
