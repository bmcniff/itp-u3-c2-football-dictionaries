def players_by_position(squads_list):
    result = {}
    for player in squads_list:
        def players_as_dictionaries(player):
            player_dict = {}
            player_dict['number'] = player[0]
            player_dict['position'] = player[1]
            player_dict['name'] = player[2]
            player_dict['date_of_birth'] = player[3]
            player_dict['caps'] = player[4]
            player_dict['club'] = player[5]
            player_dict['country'] = player[6]
            player_dict['club_country'] = player[7]
            player_dict['year'] = player[8]
            return player_dict
        player_as_dict = players_as_dictionaries(player)
        position = player[1]
        result.setdefault(position, [])
        result[position].append(player_as_dict)
    return result
