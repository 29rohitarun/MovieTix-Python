from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



options = Options()
options.add_experimental_option("detach", True)

def scrape():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                        options=options)

    driver.get("https://www.fandango.com/")


    try:
                
        wrapper = WebDriverWait(driver, 600).until(
            EC.url_contains("Checkout?"))
        
        print("In checkout page")
        
    except:
        print("There was an error")
        exit()

    try:
        title = driver.find_element(By.CLASS_NAME, 'movie-theater__movie-title')
        title_string = title.get_attribute('innerHTML')
        print(title_string)
    except:
        print("There was an exception for title")
        pass

    try:
        theater = driver.find_element(By.CLASS_NAME, 'movie-theater__theater-name')
        theater_string = theater.get_attribute('innerHTML')
        print(theater_string)
    except:
        print("There was an exception for theater")
        pass

    try:
        address = driver.find_element(By.CLASS_NAME, 'movie-theater__address')
        address_string = address.get_attribute('innerHTML')
        print(address_string)
    except:
        print("There was an exception for address")
        pass

    try:
        auditorium = driver.find_element(By.ID, 'auditorium')
        auditorium_string = auditorium.get_attribute('innerHTML')
        print(auditorium_string)
    except:
        print("There was an exception for auditorium")
        pass

    try:
        seats = driver.find_element(By.CLASS_NAME, 'seat-selection__reserved-seats')
        seats_string = seats.get_attribute('innerHTML')
        print(seats_string)
    except:
        print("There was an exception for seats")
        pass

    try:
        datetime = driver.find_element(By.CLASS_NAME, 'movie-theater__show-date-time')
        datetime_string = datetime.get_attribute('innerHTML')

        datetime_arr = datetime_string.split(' at ')

        date = datetime_arr[0].strip()
        time = datetime_arr[1].strip()

        print(date)
        print(time)
    except:
        print("There was an exception for datetime")
        pass


    try:
        tix = driver.find_element(By.ID, 'TicketSelectionEditQtyBtn')
        tix_string = tix.get_attribute('innerHTML')
        print(tix_string)

    except:
        print("There was an exception for tix")
        pass

    try:
        price = driver.find_element(By.CLASS_NAME, 'order-summary__total-price')
        price_string = price.get_attribute('innerHTML')
        print(price_string)

    except:
        print("There was an exception for price")
        pass

def main():

    scrape()

if __name__ == '__main__':
    main()


