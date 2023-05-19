while True:
    #Ranked input in decreasing order please
    #Plays input in ascending order please
    ranked_count = int(input("How many ranked? ").strip())
    ranked = list(map(int, input("Enter ranked points: ").rstrip().split()))
    game_count = int(input("How many games? ").strip())
    games = list(map(int, input("Enter game points: ").rstrip().split()))
    if ranked_count != len(ranked) or game_count != len(games):
        print("Wrong ranked or player count, enter again!")
    else:
        for i in games:
            ct = 1
            for a in set(ranked):
                if a > i:
                    ct += 1
            print(f'You have been ranked {ct}. in leaderboard!')
        break
