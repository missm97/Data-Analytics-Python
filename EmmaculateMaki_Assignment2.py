import pandas as pd
import sqlite3
from pymongo import MongoClient


#1.Read the datasets and provide a quick summary of the dataset.
games = pd.read_csv('C:/Users/emmam/Downloads/nflgames.csv') 
teams = pd.read_csv('C:/Users/emmam/Downloads/nflteams.csv')
players = pd.read_csv('C:/Users/emmam/Downloads/nflplayers (1).csv')
position = pd.read_csv('C:/Users/emmam/Downloads/nflpositions (1).csv')

print("Games DataFrame Columns:")
print(games.columns)

print("\nTeams DataFrame Columns:")
print(teams.columns)

print("\nPlayers DataFrame Columns:")
print(players.columns)


print("\nGames Dataset Head:")
print(games.head())

print("\nTeams Dataset Head:")
print(teams.head())

print("\nPlayers Dataset Head:")
print(players.head())

print("\nGames Dataset Summary:")
print(games.info())
print(games.describe())

print("\nTeams Dataset Summary:")
print(teams.info())
print(teams.describe())

print("\nPlayers Dataset Summary:")
print(players.info())
print(players.describe())

print("\nPosition Dataset summary")
print(position.info())
print(position.describe())

#2.Find the team name that has the highest average AwayScore as the Away Team
games_teams = games.merge(teams, left_on='AwayTeamID', right_on='TeamID')
averagescores = games_teams.groupby('TeamName')['AwayScore'].mean().sort_values(ascending=False)
HighestTeam = averagescores.idxmax()
highestScore = averagescores.max()

print(f"\nThe team with the highest average AwayScore as the Away Team is {HighestTeam} with an average score of {highestScore}.")

#3. Which FieldType has the highest total scores (HomeScore + AwayScore) on average (averaging over the games in this FieldType)? Which has the lowest?
games['TotalScore'] = games['HomeScore'] + games['AwayScore']
averageGames = games.groupby('FieldType')['TotalScore'].mean().sort_values()
HighestField = averageGames.idxmax()
Lowestfield = averageGames.idxmin()
print(f"\nThe FieldType with the highest average total scores is {HighestField}.")
print(f"The FieldType with the lowest average total scores is {Lowestfield}.")

#4. On average, how many players does a team have in each position?


players.columns = players.columns.str.strip()
teams.columns = teams.columns.str.strip()

playerNo = players.merge(teams, on='TeamID')
averageposition = playerNo.groupby('PositionID')['PlayerID'].size() / players['TeamID'].nunique()

print(f"\nAverage number of players per position:\n{averageposition}")

#Part II (12 points)
#1. Put down your student number and name in a database table (sqlite, or other database such as postgres, mongodb, etc.)

client = MongoClient('mongodb://localhost:27017/')
db = client['student_database']
collection = db['student_info']

student_info = {
    'student_number': '200595950',
    'student_name': 'Emmaculate Maki'
}
collection.insert_one(student_info)

#2. Read the database table, print out your student number and name.
# Retrieve the student's information
Studentdata = collection.find_one({'student_number': '200595950'})
print("Student Number:", Studentdata['student_number'])
print("Student Name:", Studentdata['student_name'])


#3. Write a function/method to print out the sum of each digit of your student number.
def studentfxn(student_number):
    return sum(int(digit) for digit in student_number)

DigitSum = studentfxn(Studentdata['student_number'])
print(DigitSum)


def NameAlphabet(student_name):
    return ''.join(sorted(student_name.replace(' ', '').lower()))

Sortedname = NameAlphabet(Studentdata['student_name'])
print(Sortedname)