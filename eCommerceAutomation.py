import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




# Fixture to initialize the WebDriver
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def refresh_browser(browser):
    browser.refresh()

# Test Case 1: Verify Flipkart is present on the left side of the top
def test_verify_flipkart_presence(browser):
    browser.get("https://www.flipkart.com/")
    
    # Wait for Flipkart element to be present
    flipkart_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@title='Flipkart']"))
    )
    
    assert flipkart_element is not None, "Flipkart element not found"

# Test Case 2: Search for "MacBook air m2"
def test_search_and_select_item(browser):
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("MacBook air m2")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for search results to load
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-id]"))
    )

    # Click on the first displayed item
    first_item = browser.find_element(By.XPATH, "//div[@data-id][1]//a[@target='_blank']")
    first_item.click()

# Test Case 3: Add item to cart
def test_add_to_cart(browser):
    
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[1])
    
    # Click on the Add to Cart button
    add_to_cart_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
    )
    add_to_cart_button.click()
    time.sleep(3)
    refresh_browser(browser)

# Test Case 4: Verify item added to cart successfully
def test_verify_item_added_to_cart(browser):
    # Wait for the cart icon to update (indicating the item has been added)
    time.sleep(5)
    expected_test = 'GO TO CART'
    
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//button[text()='GO TO CART']"), expected_test)
    )


        
if __name__ == "__main__":
    pytest.main(["-v", "eCommerceAutomation.py"])
