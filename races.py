import requests
from bs4 import BeautifulSoup

# open quests file for writing
raceFile = open("races.csv", "w")

# get page from URL
URL = "https://dragonvale.fandom.com/wiki/Dragon_Track"
page = requests.get(URL)

# parse page
soup = BeautifulSoup(page.text, "html.parser")

# find tables
tables = soup.findAll("table")

# get the specific data table with race info
table = tables[1]

# collect data from each row of the data table
for row in table.tbody.find_all("tr"):

    # get each cell in the row
    cells = row.find_all("td")

    if (len(cells) == 4):
        # get race title
        title = cells[0].text.strip()

        # get elements
        elements = "\"" + ", ".join([a['title'].strip() for a in cells[1].find_all("a")]) + "\""
        
        # get recommended dragons
        recommendedDragons = "\"" + ", ".join([a.text.strip() for a in cells[2].find_all("a")]) + "\""

        # get perfect dragons
        if (cells[3].find_all("a") == []):
            perfectDragons = cells[3].text.strip()
        else:
            perfectDragons = "\"" + ", ".join([a.text.strip() for a in cells[3].find_all("a")]) + "\""

        # write to file
        raceFile.write(f"{title}, {elements}, {recommendedDragons}, {perfectDragons}\n")
        #print(f"the recommended dragons for {title} are {elements} dragons including {recommendedDragons} and the perfect dragons are {perfectDragons}")

raceFile.close()
