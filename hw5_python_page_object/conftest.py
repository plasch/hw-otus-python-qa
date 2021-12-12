import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVERS_DIRECTORY = os.path.expanduser("~/Dev/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="http://localhost:8081/")


def driver_factory(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = False
        service = Service(executable_path=DRIVERS_DIRECTORY + '/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=DRIVERS_DIRECTORY + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=DRIVERS_DIRECTORY + "/operadriver")
    else:
        raise Exception("Driver not supported")
    return driver


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")
    driver = driver_factory(request)
    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.url = url
    return driver
