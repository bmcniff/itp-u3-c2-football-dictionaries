def players_by_country_and_position(squads_list):
    final = {}
    result = {}
    for player in squads_list:
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
        position = player[1]
        result.setdefault(position, [])
        result[position].append(player_dict)
    for player in SQUADS_DATA:
        country = player[6]
        final.setdefault(country, [])
        final[country].append({position : player})
    return final
