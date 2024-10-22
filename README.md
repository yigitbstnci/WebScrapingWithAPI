# Web Scraping with [ScraperAPI](https://www.scraperapi.com/) - sahibinden.com

This project demonstrates a web scraping solution using **ScraperAPI** to extract vehicle listing data from [sahibinden.com](https://www.sahibinden.com/), a popular Turkish online marketplace.
The scraped data is processed with **Pandas** and saved in a structured format, suitable for data analysis or reporting.

## Overview

The goal of this project is to scrape relevant information about vehicle listings, such as brand, model, price, seller information, and more, from **sahibinden.com**. 
The data is then converted into a Pandas DataFrame and exported to xlsx format for further analysis.

This project is for **educational purposes only**, and not intended for professional use. The aim is to demonstrate the process of web scraping, data extraction, and processing using Python.

## Tools & Technologies

- **ScraperAPI**: A service that handles IP rotation and prevents CAPTCHA issues, allowing for smoother web scraping experiences.
- **BeautifulSoup**: A Python library for parsing HTML and extracting the necessary data.
- **Pandas**: A Python library used for data manipulation and analysis, mainly to store, clean, and export the data into a XLSX or CSV format.


### Installation

1. **Clone the Repository**:

   First, clone the GitHub repository to your local machine:

   ```bash
     git clone https://github.com/yigitbstnci/WebScrapingWithAPI.git
     cd WebScrapingWithAPI

2. **Install Required Libraries:**:

    ```bash
    pip3 install requests beautifulsoup4 pandas

3.	**Get ScraperAPI Key**:
You will need a [ScraperAPI](https://www.scraperapi.com/) key to handle dynamic content and bypass CAPTCHA restrictions while scraping sahibinden.com.
Create an account on [ScraperAPI](https://www.scraperapi.com/) and obtain your API key.

4. **Run the Script**:
 ```bash
   python WebScrapingWithAPI.py

