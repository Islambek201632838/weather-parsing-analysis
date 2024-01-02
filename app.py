import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def convert_to_numeric(temp_str):
    # Replacing non-standard minus sign and degree symbol
    temp_str = temp_str.replace('°', '').replace('−', '-').strip()
    try:
        # Converting to float
        return float(temp_str)
    except ValueError:
        # Returning None or a default value if conversion fails
        return None

# Initializing the driver and open the website
driver = webdriver.Chrome()
driver.get('https://yandex.kz/pogoda/month?lat=43.273564&lon=76.914851&via=hnav')
sleep(1)
weather_data = {}

# Get temperature values
day_temps = driver.find_elements(By.CSS_SELECTOR, 'div.climate-calendar-day__temp-day > span.temp__value_with-unit')
night_temps = driver.find_elements(By.CSS_SELECTOR, 'div.climate-calendar-day__temp-night > span.temp__value_with-unit')

# Getting day values
days = driver.find_elements(By.CLASS_NAME, 'climate-calendar-day__day')
if len(days) == len(day_temps) == len(night_temps):
    for i in range(len(days)):
        # Convertting temperatures to numeric values
        day_temp = convert_to_numeric(day_temps[i].text)
        night_temp = convert_to_numeric(night_temps[i].text)
        weather_data[days[i].text] = {'day_temp': day_temp, 'night_temp': night_temp}

# Writing the weather data to a CSV file
with open('weather_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['Date', 'Day Temperature', 'Night Temperature'])
    
    # Writting the weather data
    for date, temps in weather_data.items():
        writer.writerow([date, temps['day_temp'], temps['night_temp']])

print("CSV file has been created.")

# Closing the driver after scraping
driver.close()
