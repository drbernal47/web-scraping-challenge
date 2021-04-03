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

# Close the browser
browser.quit()

# Store the latest content from the scraped data into variables for later
latest_title = news_titles[0].text
print(latest_title)
print('====================================================================')

latest_paragraph = paragraphs[0].text
print(latest_paragraph)