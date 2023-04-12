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

# prep a dictionary for organization
raceDict = {}

# collect data from each row of the data tables
for table in (tables[1], tables[2]):
    print("\n\n\nnew table\n\n\n")
    for row in table.tbody.find_all("tr"):

        race = {}

        # get each cell in the row
        cells = row.find_all("td")

        if (len(cells) == 4):
            # get race title
            title = cells[0].text.strip()

            # construct race dictionary
            # get elements
            race["Elements"] = "\"" + ", ".join([a['title'].strip() for a in cells[1].find_all("a")]) + "\""
            
            # get recommended dragons
            race["Recommended Dragons"] = "\"" + ", ".join([a.text.strip() for a in cells[2].find_all("a")]) + "\""

            # get perfect dragons
            if (cells[3].find_all("a") == []):
                race["Perfect Dragons"] = cells[3].text.strip()
            else:
                race["Perfect Dragons"] = "\"" + ", ".join([a.text.strip() for a in cells[3].find_all("a")]) + "\""

            # add race to dictionary if it hasn't been added by the newer table
            if title not in raceDict:
                raceDict[title] = race

# once the dictionary is complete, write the contents to file
for race in sorted(list(raceDict.keys())):
    # write to file
    raceFile.write(f"{race}, {raceDict[race]['Elements']}, {raceDict[race]['Perfect Dragons']}, {raceDict[race]['Recommended Dragons']}\n")
    #print(f"the recommended dragons for {title} are {elements} dragons including {recommendedDragons} and the perfect dragons are {perfectDragons}")

raceFile.close()
