import csv

def teamData():
    infile=open(r"./../Data/matches.csv",'r')
    teamsData = csv.DictReader(infile)
    return list(teamsData)

def teamsMenu():
    teams = {1: " Sunrisers Hyderabad", 2: " Rising Pune Supergiant",3: " Kolkata Knight Riders", 4: "Chennai Super Kings",5: "Rajasthan Royals",
             6: "Royal Challengers Bangalore",7: "Mumbai Indians",8: "Kings XI Punjab",9: " Deccan Chargers",10: "Kochi Tuskers Kerala"}
    for key in teams:
        print(key,".",teams[key])
    teamName = int(input("Enter Team name"))
    return teams[teamName]

def toss_Winning_Stats(team):
    matches_played =len([x for x in teamData() if x["TEAM1"]==team or x["TEAM2"]==team])
    tossWin = len([x for x in teamData() if x["TOSS_WINNER"]==team])
    return team,matches_played,tossWin


def year_wise_matchPlayed(team):
    matchPlayed = [x["SEASON"] for x in teamData() if x["TEAM1"]==team or x["TEAM2"]==team]
    matchesWon =  [x["SEASON"] for x in teamData() if x["WINNER"]==team]
    years = sorted(set(matchPlayed))
    yearwiseDict = {}
    for year in years:
        yearwiseDict[year]={"matcthPlayed" : matchPlayed.count(year),
        "matchWon": matchesWon.count(year)}
    return yearwiseDict

def city_wise_matchplayed(team):
    print(team)
    cityWiseMatchPlayed = [x["CITY"] for x in teamData() if x["TEAM1"] == team or x["TEAM2"] == team]
    cityWiseMatchWon =[x["CITY"] for x in teamData() if x["WINNER"]==team]
    cities = sorted(set(cityWiseMatchPlayed))
    print(' ' * 3,"CITY", ' ' * 7,"MATCHES PLAYED", ' ' * 7,"MATCHES WON")
    for cwm in cities:
        print(f"{ ' '* 3} {cwm} {' ' * 7}      {cityWiseMatchPlayed.count(cwm)}{' ' * 7}             {cityWiseMatchWon.count(cwm)}")

