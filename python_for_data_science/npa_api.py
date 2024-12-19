
''' 
We will use the NBA API to determine how well the Golden State Warriors performed against the Toronto Raptors. 
We will use the API to determine the number of points t
he Golden State Warriors won or lost by for each game.
 So if the value is three, the Golden State Warriors won by three points. 
 Similarly it the Golden State Warriors lost by two points the result will be negative two.
   The API will handle a lot of the details, such a Endpoints and Authentication.
'''

from nba_api.stats.static import teams
import matplotlib.pyplot as plt
import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# The method get_teams() returns a list of dictionaries.
nba_teams = teams.get_teams()

#  first three elements of the list
print(nba_teams[0:3])

# convert dictionary to a table 
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
print("teams dataframe : ", df_teams.head())

# use nickname to find the unique id 
df_warriors = df_teams[df_teams['nickname']=='Warriors']
print("\ndf_warriors : \n", df_warriors)

# access first col of dataset
# we now have an integer that can be used to request the Warriors information 
id_warriors = df_warriors[['id']].values[0][0]
print("\n id_warriors : \n", id_warriors)

# The function "League Game Finder " will make an API call, 
# it's in the module stats.endpoints.
# The parameter team_id_nullable is the unique ID for the warriors
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
print("\n gamefinder json : \n", gamefinder.get_json())

'''
The game finder object has a method get_data_frames(), that returns a dataframe. 
If we view the dataframe, it contains information about all the games the Warriors played. 
The PLUS_MINUS column contains information on the score, 
if the value is negative, the Warriors lost by that many points, 
if the value is positive, the warriors won by that amount of points. 
The column MATCHUP has the team the Warriors were playing, 
GSW stands for Golden State Warriors and TOR means Toronto Raptors. 
vs signifies it was a home game and the @ symbol means an away game.
'''
games = gamefinder.get_data_frames()[0]
print("\ngames : \n", games.head()) 

# download the dataframe from the API call for Golden State and 
# run the rest like a video.

import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")

file_name = "Golden_State.pkl"
games_golden_state = pd.read_pickle(file_name)
print("\n Games Golden State : \n", games_golden_state.head())

# create two dataframes, one for the games that the Warriors faced the raptors at home, 
# and the second for away games.

games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']

print("\n Games Home Mean: \n", games_home['PLUS_MINUS'].mean())
print("\n Games Away Mean: \n", games_away['PLUS_MINUS'].mean())

# plot out the PLUS MINUS column for the dataframes games_home and  games_away. 
# We see the warriors played better at home.
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()