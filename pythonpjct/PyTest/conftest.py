import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    print("Executing setup")
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.get("http://127.0.0.1:8000/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    

    request.cls.driver = driver
    yield
    print("Executing teardown")
    time.sleep(5)
    driver.quit()