# Weather Data Scraper and Analyzer

## Overview
This project contains a Python script for scraping weather data from Yandex Weather using Selenium and a Jupyter Notebook for analyzing the data to find average temperatures, as well as the hottest and coldest days.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Pandas
- Matplotlib
- Polars (optional for additional data analysis)

## Installation
1. Clone this repository.
2. Install the required Python packages:
3. Make sure `chromedriver` is installed and in your system's PATH.

## Usage
1. Run the Python script `weather_scraper.py` to scrape weather data.
This will create a `weather_data.csv` file with the scraped data.

2. Open the Jupyter Notebook `data_analysis.ipynb` to analyze the data.
- The notebook includes code to calculate average, minimum, and maximum temperatures.
- It also contains visualizations for day and night temperature trends.

3. Execute the cells in the Jupyter Notebook to see the analysis results.

## Features
- Web scraping with Selenium.
- Data cleaning and numeric conversion.
- Data analysis with Pandas and Polars.
- Data visualization with Matplotlib.


