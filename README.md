# web-scraping-challenge
This assignment was to create a web app that scrapes data related to Mars missions.


The scrape_mars.py app defines a function that runs code to scrape all of our Mars-related data from the web and returns it in a dictionary:

* 'latest_title' returns the headlines of a recent news article related to Mars (found at https://redplanetscience.com/)
* 'latest_paragraph' returns the teaser paragraph for the recent news article
* 'featured_image_url' returns the url of a featured image of Mars (found at https://spaceimages-mars.com/)
* 'mars_table' returns an html-formatted table of Mars data (found at https://galaxyfacts-mars.com/)
* 'hemisphere_image_urls' returns the urls of high-quality images of Mars' hemispheres (found at https://marshemispheres.com/)

The app.py app will create a flask server to run the template and test out this code. Run this app, then on your browser go to "http://127.0.0.1:5000/".

Click on the "Refresh News" button to update the data scraper and display new information.

Reference screenshots of this template found in the "Screenshots" folder!
