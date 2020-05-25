def players_as_dictionaries(squads_list):
    result = []
    for i in squads_list:
        player = {}
        player['number'] = i[0]
        player['position'] = i[1]
        player['name'] = i[2]
        player['date_of_birth'] = i[3]
        player['caps'] = i[4]
        player['club'] = i[5]
        player['country'] = i[6]
        player['club_country'] = i[7]
        player['year'] = i[8]
        result.append(player)
    return result
