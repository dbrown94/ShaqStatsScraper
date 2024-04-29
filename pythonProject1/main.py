import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_shaq_stats():
    # Send a GET request to the Wikipedia page
    url = 'https://en.wikipedia.org/wiki/List_of_career_achievements_by_Shaquille_O%27Neal'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing Shaq's career achievements
    table = soup.find('table', class_='wikitable')

    # Extract data from the table
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all(['th', 'td'])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    # Convert the data into a DataFrame
    shaq_stats = pd.DataFrame(data[1:], columns=data[0])

    return shaq_stats

# Call the function to scrape Shaq's stats
shaq_stats = scrape_shaq_stats()

# Display the DataFrame
print(shaq_stats)
