if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    clean_string = price.replace("$", "").replace(",", "")
    return float(clean_string)

def clean_scraped_text(scraped_text: str) -> list[str]:
    str_list = scraped_text.split("\n")
    unwanted_values = ["", "NEW!", "NEW", "S", "V", "GS", "P"]
    str_clean = []

    for s in str_list:
        if s not in unwanted_values:
            str_clean.append(s)
    
    return str_clean

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    item_data = clean_scraped_text(scraped_text)
    if len(item_data) > 2:
        desc = item_data[2]
    else:
        desc = "No description available"

    cleaned_price = clean_price(item_data[1])
    
    menu_item = MenuItem(category = title, name = item_data[0],
                        price = cleaned_price, description = desc)
    
    return menu_item


if __name__=='__main__':
    pass
