#!/usr/bin/env python3
"""Game Analytics Dashboard
This module simulates a game analytics dashboard that processes player data
and displays various statistics using comprehensions and combined analysis.
"""


def display_combined_analysis(data: dict[str, any]) -> None:
    """Display combined analysis of player data.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== Combined Analysis ===")
    total_players = len(data['players'])

    total_score_sum = sum(player['score'] for player
                          in data['players'].values())
    global_achievements = {
        achiev
        for player in data['players'].values()
        for achiev in player['achievements']
    }
    stats_list = [
        (player['score'], player_name, len(player['achievements']))
        for player_name, player in data['players'].items()
    ]
    best_score, best_player_name, best_nb_achievements = max(stats_list)

    average_score = total_score_sum / total_players
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(global_achievements)}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top performer: {best_player_name} ({best_score} points, "
          f"{best_nb_achievements} achievements)")


def display_dictionary_comprehension(data: dict[str, any]) -> None:
    """Display dictionary comprehension examples.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== Dict Comprehension Examples ===")
    dict_players_scores = {
        player_name: player_data['score']
        for player_name, player_data in data['players'].items()
    }
    dict_score_categories = {'high': 0, 'medium': 0, 'low': 0}

    dict_achievement_counts = {
        player_name: len(player_data['achievements'])
        for player_name, player_data in data['players'].items()
    }

    for player_name in data['players']:
        current_player_profil = data['players'][player_name]
        score_player = current_player_profil['score']
        if score_player >= 2000:
            dict_score_categories['high'] += 1
        elif score_player > 1000 and score_player < 2000:
            dict_score_categories['medium'] += 1
        else:
            dict_score_categories['low'] += 1

    print(f"Player scores: {dict_players_scores}")
    print(f"Score categories: {dict_score_categories}")
    print(f"Achievement counts: {dict_achievement_counts}")


def display_list_comprehension(data: dict[str, any]) -> None:
    """Display list comprehension examples.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== List Comprehension Examples ===")
    list_top_scorers = [
        player_name for player_name, player_data in
        data['players'].items() if player_data['score'] > 2000
    ]
    list_scores_doubled = [
        player_data['score'] * 2 for player_data in data['players'].values()
    ]
    list_player = [
        session['player'] for session in data['sessions']
        if session['active']
    ]

    print(f"High scorers (>2000): {list_top_scorers}")
    print(f"Scores doubled: {list_scores_doubled}")
    print(f"Active players: {list_player}")


def display_set_comprehension(data: dict[str, any]) -> None:
    """Display set comprehension examples.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== Set Comprehension Examples ===")
    unique_players = {session['player'] for session in data['sessions']}
    active_regions = {session['region'] for session in data['sessions']}
    unique_achievements = {
        achiev
        for player_data in data['players'].values()
        for achiev in player_data['achievements']
    }

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")


def get_game_data() -> dict:
    """Generate game data for players and sessions.
    Returns:
        dict: The generated game data.
    """

    players_data = {
        'alice': {'score': 2300,
                  'achievements': {'first_kill', 'level_10', 'boss_slayer'},
                  'level': 25},
        'bob': {'score': 1800, 'achievements': {'boss_slayer'}, 'level': 12},
        'charlie': {'score': 2150, 'achievements': {'level_10', 'collector'},
                    'level': 20},
        'diana': {'score': 2050, 'achievements': {'speedrun', 'no_damage'},
                  'level': 30}
    }

    sessions = [
        {'player': 'alice', 'region': 'north', 'active': True},
        {'player': 'bob', 'region': 'east', 'active': False},
        {'player': 'charlie', 'region': 'north', 'active': True},
        {'player': 'diana', 'region': 'west', 'active': True}
    ]
    return {'players': players_data, 'sessions': sessions}


def main() -> None:
    """Main function to run the game analytics dashboard."""

    print("=== Game Analytics Dashboard ===")
    data = get_game_data()
    display_list_comprehension(data)
    display_dictionary_comprehension(data)
    display_set_comprehension(data)
    display_combined_analysis(data)


if __name__ == "__main__":
    main()
