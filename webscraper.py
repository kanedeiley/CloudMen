from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Set the path to the uBlock Origin extension file
extension_path = "C:/Users/danie/Downloads/gighmmpiobklfepjocnamgkkbiglidom"

# Create a new instance of the Chrome driver with uBlock Origin extension
options = webdriver.ChromeOptions()
options.add_extension(extension_path)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

# Load the search results page
driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1162")

# Click the "Close" button of the overlay if it exists
try:
    close_button = driver.find_element(By.CSS_SELECTOR, "button.CCPAModal__StyledCloseButton-sc-10x9kq-2.gvGrz")
    close_button.click()
    time.sleep(1)
except:
    pass

# Click the "Show More" button multiple times until it is no longer visible
while True:
    try:
        # Close any pop-up ads
        for window_handle in driver.window_handles:
            driver.switch_to.window(window_handle)
            if "pop-up ad" in driver.title.lower():
                driver.close()
        
        show_more_button = driver.find_element(By.CSS_SELECTOR, "button.PaginationButton__StyledPaginationButton-txi1dr-1.gjQZal")
        if show_more_button.is_displayed():
            try:
                show_more_button.click()
                time.sleep(1)
            except:
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ReactModal__Overlay")))
                show_more_button.click()
                time.sleep(1)
        else:
            break
    except:
        # Handle any exceptions that may occur during the loop, such as element not found errors
        pass

# Get the complete HTML code of the page
html_code = driver.page_source

# Close the driver
driver.quit()

# Print the HTML code
print(html_code)
