import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import pandas as pd

class Extractor:
    def __init__(self, link="https://www.theguardian.com/football/results", days_ago=1):
        self.link = link #"https://www.theguardian.com/football/results"
        self.response = requests.get(self.link).text
        self.target_date = datetime.today() - timedelta(days=days_ago)
    
    def get_data(self):
        soup = BeautifulSoup(self.response, 'html.parser')
        formated_date = self.target_date.strftime("%A %d %B %Y")

        matches = []
        day_match = soup.find(lambda tag: tag.name == "div" and  formated_date in tag.text, class_="football-matches__day") 

        if day_match:
            football_matches_table = day_match.findAll("div", class_="football-table__container")

            for match_table in football_matches_table:
                table = match_table.find("table")
                title = table.find("caption").a.text
                for match in table.findAll("tr")[1:]:
                    team_names = match.findAll("span", class_="team-name__long")
                    scores = match.findAll("div", class_="football-team__score")
                    matches.append(
                        {
                            "Date": self.target_date.strftime("%Y-%m-%d"),
                            "Competition":title,
                            "Team_a":team_names[0].text,
                            "Score_a":scores[0].text,
                            "Team_b":team_names[1].text,
                            "Score_b":scores[1].text
                        }
                    )  
            
            pd.DataFrame(matches).to_json(f"./match-data-{self.target_date.strftime('%Y-%m-%d')}.json", orient="records")
            print("Save sucessfully")
        else:
            print(f"No match on day {self.target_date.strftime('%Y-%m-%d')}.")
