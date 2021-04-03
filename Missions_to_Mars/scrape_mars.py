# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Scraping NASA Mars News

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# URL of page to be scraped
url = 'https://redplanetscience.com/'
browser.visit(url)

# Collect the latest News Title and Paragraph Text
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
news_titles = soup.find_all('div', class_='content_title')
paragraphs = soup.find_all('div', class_='article_teaser_body')

# Store the latest content from the scraped data into variables for later
latest_title = news_titles[0].text
print(latest_title)
print('====================================================================')

latest_paragraph = paragraphs[0].text
print(latest_paragraph)


# Scraping JPL Mars Space Images
# URL of page to be scraped
url = 'https://spaceimages-mars.com/'
browser.visit(url)

# Collect the latest News Title and Paragraph Text
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image_data = soup.find_all('img')

# Close the browser
browser.quit()

# Store url for latest featured image (index 1, after the NASA logo) into a variable for later
featured_image_url = url + image_data[1].get("src")
print(featured_image_url)


# Scraping Mars Facts
# URL of page to be scraped
url = 'https://galaxyfacts-mars.com/'

# Use pandas to scrape tables
tables = pd.read_html(url)

# Find the first table with desired data
mars_table = tables[0]

# Convert this table into an html string
mars_table.to_html('table.html')

print(mars_table)