from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Define path to chromedriver executable
path = './chromedriver-linux64/chromedriver'

# Configure Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-crash-reporter")
options.add_argument("--disable-oopr-debug-crash-dump")
options.add_argument("--no-crash-upload")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-low-res-tiling")
options.add_argument("--log-level=3")
options.add_argument("--silent")
options.add_argument("--headless")  # Enable headless mode

# Initialize Chrome webdriver with options
driver = webdriver.Chrome( options=options)

# URL to scrape
web = 'https://www.thesun.co.uk/sport/football/'

# Open the webpage
driver.get(web)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    try:
        title = container.find_element(by='xpath', value='.//a/h2').text
        subtitle = container.find_element(by='xpath', value='.//a/p').text
        link = container.find_element(by='xpath', value='.//a').get_attribute('href')
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
    except Exception as e:
        print(f"Error: {e}")

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv', index=False)

# Quit the driver
driver.quit()
