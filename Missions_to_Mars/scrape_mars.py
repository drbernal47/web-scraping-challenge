# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Scraping Function
def scrape():

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
    latest_paragraph = paragraphs[0].text


    # Scraping JPL Mars Space Images
    # URL of page to be scraped
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Collect the latest News Title and Paragraph Text
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_data = soup.find_all('img')

    # Store url for latest featured image (index 1, after the NASA logo) into a variable for later
    featured_image_url = url + image_data[1].get("src")


    # Scraping Mars Facts
    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com/'

    # Use pandas to scrape tables
    tables = pd.read_html(url)

    # Find the first table with desired data
    mars_table = tables[0]

    # Convert this table into an html string
    mars_table_html = mars_table.to_html(header=False, index=False)


    # Scraping images for Mars Hemispheres
    # URL of page to be scraped
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Find links on the main page for hemisphere pages and store link urls
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    all_links = soup.find_all('a', class_='itemLink')
    hemi_links = [all_links[1].get('href')]
    hemi_links.append(all_links[3].get('href'))
    hemi_links.append(all_links[5].get('href'))
    hemi_links.append(all_links[7].get('href'))

    # Create an empty list to store dictionaries
    hemisphere_image_urls = []

    # Scrape links and visit each to find data

    for hemi in hemi_links:
            
        # Go to hemisphere page
        hemi_url = url + hemi
        browser.visit(hemi_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
            
        # Store data for the title and enhanced image
        title = soup.find_all('h2', class_='title')[0].text
        img_url = url + soup.find('img', class_='wide-image').get('src')
        
        # Create a dictionary of this data and append to list
        hemi_dict = {'title': title, "img_url": img_url}
        hemisphere_image_urls.append(hemi_dict)
            
        # Go back to original page
        browser.visit(url)
        

    # Close the browser
    browser.quit()


    # Create a dictionary with all the scraped data
    scrape_dict = {
        "latest_title": latest_title,
        "latest_paragraph": latest_paragraph,
        "featured_image_url": featured_image_url,
        "mars_table_html": mars_table_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Return the dictionary to LOCATION
    return scrape_dict