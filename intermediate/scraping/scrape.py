"""
From 30 Days of Python tutorial, made by Coding Entrepreneurs.

Day 12 - Web Scraping Box Office $$ Numbers

To run this code, you need to install the next packages:

(python)$ pip install requests
(python)$ pip install requests-html
(python)$ pip install pandas

Scrapping a web site
"""
import os
import sys
import datetime
import requests
import pandas as pd
from requests_html import HTML

# Get the path of current directory
BASE_DIR = os.path.dirname(__file__)

def url_to_txt(url, filename=None, year=None, save=False):
    """
    Make a request to an url, if save is True, save 
    the text of response into a file

    @param url Url to get
    @param filename The name to use in html file 
    that save the text of web page requested
    @param year Year of reference
    @param save Check if html file need to be saved
    """
    # Make a request to the url and save the response in a variable
    r = requests.get(url)
    html_text = ''
    # Check the status code of response
    if r.status_code == 200:
        # Save the text content of the web site
        html_text = r.text
        if save:
            # Set the folder to save the html file
            path = os.path.join(BASE_DIR, 'html')
            # Create the folder if not exist
            os.makedirs(path, exist_ok=True)
            if not filename:
                filename = f"url-query{year}.html"
            # Set the filepath with the name of html
            filepath = os.path.join(path, filename)
            with open(filepath, 'w') as f:
                f.write(html_text)
        return html_text
    return ""

def parse_and_extract(url, year='2020'):
    """
    Call to url_to_txt function to get a web page
    text, parse that text to HTML object and extract
    a table of interest.

    Save the data in the table extracted into a list
    of lists and store that data in a csv file

    @param url A valid Url to request
    @param year The year to search
    """
    # Get the text of the response
    html_text = url_to_txt(url, year=year, save=True)
    if html_text == None:
        return False
    # Get an html object
    r_html = HTML(html=html_text)
    # Search an element by html marker (table, a, h1, ...)
    #r_element = r_html.find('table')

    # To this example, im searching by the imdb table in the web page
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)

    # To save the scraped table into a list
    table_data = []
    # To save the header of table into a list
    header_names = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    for row in rows[1:]:
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            row_data.append(col.text)
        table_data.append(row_data)

    # Print the header of table
    print(header_names)
    # Print the selected row of table
    print(table_data[5])

    # Define a Data Frame class of pandas
    df = pd.DataFrame(table_data, columns=header_names)
    # Set the folder to save the csv file
    path = os.path.join(BASE_DIR, 'data')
    # Create the folder if not exist
    os.makedirs(path, exist_ok=True)
    # Set the filepath with the name of csv
    filepath = os.path.join(path, f'{year}.csv')
    df.to_csv(filepath, index=False)

    return True

def run(start_year=None, years_ago=10):
    """
    Call to parse_and_extract function to get the
    data of movies rank in provided years 

    @param start_year Year to start the search
    @param years_ago Number of years to lookup
    """
    # Get the current date
    now = datetime.datetime.now()
    if start_year == None:
        # Get the current year
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert 1977 <= start_year <= now.year
    for i in range(0, years_ago+1):
        # Set the url to scrap
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        # Save the data to search
        finished = parse_and_extract(url, start_year)
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"The {start_year} is not finished")
        start_year -= 1

if __name__ == '__main__':
    """
    Make call to run function to start the scrape of
    a web page and process the data

    @param sys.argv[1] Start year to search
    @param sys.argv[2] Number of years to lookup backward
    """
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0
    run(start_year=start, years_ago=count)