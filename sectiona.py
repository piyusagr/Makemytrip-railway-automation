import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your ChromeDriver executable
 
pyautogui.screenshot('Code.png')
chrome_driver_path = "C:\\Users\\KIIT\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"

# Set up logging
logging.basicConfig(filename=r'automation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Create a ChromeDriverService
service = webdriver.chrome.service.Service(chrome_driver_path)

# Create an instance of the WebDriver
driver = webdriver.Chrome(service=service)

day=datetime.datetime.now().day
try:
    # Navigate to the MakeMyTrip railways page
    driver.get("https://www.makemytrip.com/railways/")

    # Verify landing on the correct page
    assert "MakeMyTrip" in driver.title, "Did not land on the correct page"
    logging.info("Landed on the correct page")
    pyautogui.screenshot('Makemytrip.png')

    # Print the URL and Title of the Page
    logging.info("Page URL: %s", driver.current_url)
    logging.info("Page Title: %s", driver.title)

    # Click on FROM
    from_element = driver.find_element(By.ID, "fromCity")
    from_element.click()
    from_element.send_keys(Keys.BACKSPACE)

    # Enter the city in FROM: DELHI
    from_element.send_keys("DELHI")
    time.sleep(1)  # Add a short delay to allow suggestions to appear
    from_element.send_keys(Keys.RETURN)
    logging.info("Selected FROM: DELHI")
    pyautogui.screenshot('fromadded.png')

    # Click on TO
    to_element = driver.find_element(By.ID, "toCity")
    to_element.click()
    to_element.send_keys(Keys.BACKSPACE)

    # Enter the city in TO: LUCKNOW
    to_element.send_keys("LUCKNOW")
    time.sleep(1)  # Add a short delay to allow suggestions to appear
    to_element.send_keys(Keys.RETURN)
    logging.info("Selected TO: LUCKNOW")
    pyautogui.screenshot('toadded.png')

    # Click on the Travel Date input field
    date_input = driver.find_element(By.ID, "travelDate")
    date_input.click()
    wait = WebDriverWait(driver, 10)
    date_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'20 May 24R̥')]")))

    # Click on the element
    date_element.click()
        
    # Wait until the calendar is visibleR̥R̥
    logging.info("selected 20th may")
    pyautogui.screenshot('date.png')

    
   # # Click on class
    class_element = driver.find_element(By.ID, "travelClass")
    class_element.click()
    logging.info('selected class')

    # Select a class from dropdown: Third AC
    select = Select(driver.find_element(By.ID, "travelClass"))
    select.select_by_visible_text("Third AC")
    logging.info("Selected Class: Third AC")
    pyautogui.screenshot('class.png')

    # Click on SEARCH Button
    search_button = driver.find_element(By.ID, "searchBtn")
    search_button.click()
    logging.info("Clicked on SEARCH Button")
    pyautogui.screenshot('search.png')
    # Wait for a moment to capture the screen recording
    time.sleep(3)

except Exception as e:
    logging.error("Error occurred: %s", str(e))

finally:
    # Close the WebDriver
    driver.quit()





































































































   # # # Click on class
    # class_element = driver.find_element(By.ID, "travelClass")
    # class_element.click()
    # logging.info('selected class')

    # # Select a class from dropdown: Third AC
    # select = Select(driver.find_element(By.ID, "travelClass"))
    # select.select_by_visible_text("Third AC")
    # logging.info("Selected Class: Third AC")
    # pyautogui.screenshot('class.png')

    # Click on SEARCH Button
    # search_button R̥= driver.find_element(By.ID, "searchBtn")
    # search_button.click()
    # logging.info("Clicked on SEARCH Button")
    # pyautogui.screenshot('search.png')