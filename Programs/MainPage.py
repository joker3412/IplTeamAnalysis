import MatchStat as m
if __name__=="__main__":
    menu = 'y'
    while menu in 'yY':
        print("===Statistics===\n1. Toss Winning Stats\n2. Yearwise matches played/won\n3. Citywide Matches played/won\n4. Exit")
        choice = int(input("Enter a choice:"))

        if choice == 1:
            toss = m.toss_Winning_Stats(m.teamsMenu())
            print("#" * 100, end="\n\n\n")
            print(toss[0])
            print("Total Matches played:", toss[1])
            print("No of times toss won:", toss[2])
            print("Toss winning percentage is", round(float(toss[2] / toss[1] * 100), 2))

        elif choice == 2:
            team =m.teamsMenu()
            yearWiseDict = m.year_wise_matchPlayed(team)
            print("#" * 100, end="\n\n\n")
            print(team)
            print(' ' * 3, "YEAR", ' ' * 7, "MATCHES PLAYED", ' ' * 7, "MATCHES WON")
            for key in yearWiseDict:
                print( f"{' ' * 3} {key} {' ' * 7}      {yearWiseDict[key]['matcthPlayed']}{' ' * 7}             {yearWiseDict[key]['matchWon']}")

        elif choice == 3:
            m.city_wise_matchplayed(m.teamsMenu())

        else:
            break
        menu =input("Want To see another team stat press y/Y : ")
        print("*"*100,end="\n\n\n")


















