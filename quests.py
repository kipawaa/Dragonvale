import requests
from bs4 import BeautifulSoup

# open quests file for writing
questFile = open("quests.csv", "w")

# get page from URL
URL = "https://dragonvale.fandom.com/wiki/Quests"
page = requests.get(URL)

# parse page
soup = BeautifulSoup(page.text, "html.parser")

# find tables
tables = soup.findAll("table")

# get the specific data table with quest info
table = tables[1]

# collect data from each row of the data table
for row in table.tbody.find_all("tr"):

    # get each cell in the row
    cells = row.find_all("td")

    if (cells != []):
        title = cells[0].text.strip()
        dragon = cells[2].text.strip()
        time = cells[4].text.strip()
        questFile.write(f"{title}, {dragon}, {time}\n")
        print(f"The perfect dragon for the \"{title}\" quest is the {dragon}, taking {time}")

questFile.close()
