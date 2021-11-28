from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.url)
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "top-links")))
    elements = header_links.find_elements(By.TAG_NAME, 'li')
    assert len(elements) == 7
    # Check logo name
    logo = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.text == "Your Store"
    # Check search field is empty
    search = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "search")))
    assert search.get_attribute("placeholder") == "Search"
    # Check categories in menu
    menu = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "menu")))
    assert "Software" in menu.text
    footer_rights = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer > div > p")))
    assert "Your Store © 2021" in footer_rights.text


def test_catalog_page(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    # Check category name
    name_ctgr = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2")))
    assert "Laptops & Notebooks" == name_ctgr.text
    # Check amount of products cards on page
    content = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div:nth-child(7)")))
    elements = content.find_elements(By.CLASS_NAME, 'product-layout')
    assert len(elements) == 5
    # Check default sort filter
    sort_filter = browser.find_element(By.CSS_SELECTOR, "#input-sort > option[selected]")
    assert "Default" == sort_filter.text
    add_to_cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")))
    assert add_to_cart_btn.find_element(By.TAG_NAME, "span").text == "ADD TO CART"


def test_product_card(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=47")
    product_title = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 h1")))
    assert product_title.text == "HP LP3065"
    product_price = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")))
    assert product_price.text == "$122.00"
    cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    assert cart_btn.is_enabled()
    product_description = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#tab-description")))
    assert "HP LP3065" in product_description.text


def test_login_admin_page(browser):
    browser.get(browser.url + "/admin")
    username_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert username_field.get_attribute("placeholder") == "Username"
    password_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert password_field.get_attribute("placeholder") == "Password"
    forgotten_pswrd = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Forgotten Password")))
    assert forgotten_pswrd.text == "Forgotten Password"
    login_btn = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert login_btn.text == "Login"
    assert login_btn.is_enabled()


def test_registration_page(browser):
    browser.get(browser.url + "index.php?route=account/register")
    page_title = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > h1")))
    assert page_title.text == "Register Account"
    account_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".list-group")))
    assert ("Register" in account_links.text) and ("My Account" in account_links.text)
    password_fieldset = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "fieldset:nth-child(2)")))
    password_fields = password_fieldset.find_elements(By.CSS_SELECTOR, "input")
    for i in password_fields:
        assert i.get_attribute("type") == "password"
    continue_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='submit']")))
    assert continue_btn.is_enabled()
