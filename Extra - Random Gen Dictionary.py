import random as r


def gen_player(player_list):
    player_count = int(input("How many players?"))
    for i in range(player_count):
        player_list["player_" + str(i)] = {}
        player_list["player_" + str(i)].update({"Name": "Orc " + str(i + 1),
                                                "Money": r.randint(500, 1000),
                                                "Guess": r.randint(1, 6)})


player_list = {}
gen_player(player_list)
print(player_list)