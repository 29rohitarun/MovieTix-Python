from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import process

options = Options()
user_agent = 'jaycurry'
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("detach", True)

def scrape():

    scrape_arr = [""] * 11
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
        scrape_arr[0] = title_string
        print(title_string)
    except:
        print("There was an exception for title")
        pass


    try:
        rating = driver.find_element(By.CLASS_NAME, 'movie-theater__movie-rating')
        rating_string = rating.get_attribute('innerHTML')
        scrape_arr[1] = rating_string
        print(rating_string)
    except:
        print("There was an exception for rating")
        pass

    try:
        theater = driver.find_element(By.CLASS_NAME, 'movie-theater__theater-name')
        theater_string = theater.get_attribute('innerHTML')
        try:
            scrape_arr[2] = theater_string.split('amp;')[0] + theater_string.split('amp;')[1]
        except:
            scrape_arr[2] = theater_string
            pass
        print(theater_string)
    except:
        print("There was an exception for theater")
        pass

    try:
        address = driver.find_element(By.CLASS_NAME, 'movie-theater__address')
        address_string = address.get_attribute('innerHTML')
        print(address_string)
        street = address_string.split('<br>')[0]
        zip = address_string.split('<br>')[1]
        scrape_arr[3] = street.strip()
        scrape_arr[4] = zip.strip()
    except:
        print("There was an exception for address")
        pass

    try:
        auditorium = driver.find_element(By.ID, 'auditorium')
        auditorium_string = auditorium.get_attribute('innerHTML')
        scrape_arr[5] = auditorium_string
        print(auditorium_string)
    except:
        print("There was an exception for auditorium")
        pass

    try:
        seats = driver.find_element(By.CLASS_NAME, 'seat-selection__reserved-seats')
        seats_string = seats.get_attribute('innerHTML')
        scrape_arr[6] = seats_string
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

        scrape_arr[7] = date
        scrape_arr[8] = time

        print(date)
        print(time)
    except:
        print("There was an exception for datetime")
        pass

    try:
        tix = driver.find_element(By.ID, 'TicketSelectionEditQtyBtn')
        tix_string = tix.get_attribute('innerHTML')
        scrape_arr[9] = tix_string
        print(tix_string)

    except:
        print("There was an exception for tix")
        pass

    try:
        price = driver.find_element(By.CLASS_NAME, 'order-summary__total-price')
        price_string = price.get_attribute('innerHTML')
        scrape_arr[10] = price_string
        print(price_string)

    except:
        print("There was an exception for price")
        pass

    driver.close()

    return scrape_arr

def main():

    arr = process.main(scrape())
    return arr

if __name__ == '__main__':
    main()


