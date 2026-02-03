#!/usr/bin/env python3
"""Game Analytics Dashboard
This module simulates a game analytics dashboard that processes player data
and displays various statistics using comprehensions and combined analysis.
"""

import random


def display_combined_analysis(data: dict[str, any]) -> None:
    """Display combined analysis of player data.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== Combined Analysis ===")
    total_players = len(data['players'])
    global_achievements = set()
    total_score_sum = 0

    best_player_name = ""
    best_score = -1
    best_nb_achievements = 0

    for player_name in data['players']:
        current_player_profil = data['players'][player_name]
        score = current_player_profil['total_score']

        total_score_sum += score
        global_achievements.update(current_player_profil['achievement_event'])

        if score > best_score:
            best_score = score
            best_player_name = player_name
            best_nb_achievements = current_player_profil['achievement_event']

        average_score = total_score_sum / total_players
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(global_achievements)}")
    print(f"Average score: {average_score:.1f}")
    print(f"Top performer: {best_player_name} ({best_score} points, "
          f"{len(best_nb_achievements)} achievements)")


def display_dictionary_comprehension(data: dict[str, any]) -> None:
    """Display dictionary comprehension examples.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== Dict Comprehension Examples ===")
    dict_players_scores = {}
    dict_score_categories = {'high': 0, 'medium': 0, 'low': 0}
    dict_achievement_counts = {}

    for player_name in data['players']:
        current_player_profil = data['players'][player_name]
        score_player = current_player_profil['total_score']
        if score_player >= 2000:
            dict_score_categories['high'] += 1
        elif score_player > 1000 and score_player < 2000:
            dict_score_categories['medium'] += 1
        else:
            dict_score_categories['low'] += 1
        dict_players_scores[player_name] = score_player
        count_achievement = current_player_profil['achievements_count']
        dict_achievement_counts[player_name] = count_achievement
    print(f"Player scores: {dict_players_scores}")
    print(f"Score categories: {dict_score_categories}")
    print(f"Achievement counts: {dict_achievement_counts}")


def display_list_comprehension(data: dict[str, any]) -> None:
    """Display list comprehension examples.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== List Comprehension Examples ===")
    list_top_scorers = []
    list_scores_doubled = []
    list_player = []

    for player_name in data['players']:
        current_player_profil = data['players'][player_name]
        hight_score = current_player_profil['total_score']
        double_score = current_player_profil['total_score'] * 2
        if hight_score > 2000:
            list_top_scorers.append(player_name)
        list_scores_doubled.append(double_score)
    print(f"High scorers (>2000): {list_top_scorers}")
    print(f"Scores doubled: {list_scores_doubled}")

    for session in data['sessions']:
        if session['active']:
            player_name = session['player']
            list_player.append(player_name)
    print(f"Active players: {list_player}")


def display_set_comprehension(data: dict[str, any]) -> None:
    """Display set comprehension examples.
    Args:
        data (dict): The game data containing player profiles.
    """

    print("\n=== Set Comprehension Examples ===")
    unique_players = set()
    unique_achievements = set()
    active_regions = set()

    for session in data['sessions']:
        unique_players.add(session['player'])
        player_name = session['player']
        current_player_profil = data['players'][player_name]
        unique_achievements.update(current_player_profil['achievement_event'])
        active_regions.add(current_player_profil['region'])
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")


def assigned_random_value(
        players: set, achievements: set,
        game_mode: set, region: set) -> dict[str, any]:
    """Assign random values to players and generate session data.
    Args:
        players (set): Set of player names.
        achievements (set): Set of achievement names.
        game_mode (set): Set of game modes.
        region (set): Set of regions.
    Returns:
        dict: A dictionary containing player profiles and session data.
    """

    players_list = list(players)
    game_mode_list = list(game_mode)
    achievements_list = list(achievements)
    region_list = list(region)

    # Player statistics
    players_data = {}
    for player in players:
        nb_achievement = random.randint(1, len(achievements))
        name_achivements = random.sample(achievements_list, k=nb_achievement)
        players_data[player] = {
            'level': random.randint(1, 50),
            'total_score': random.randint(10, 3000),
            'sessions_played': random.randint(10, 100),
            'favorite_mode': random.choice(game_mode_list),
            'achievements_count': nb_achievement,
            'achievement_event': name_achivements,
            'region': random.choice(region_list)
        }

    # Session data for comprehensions
    sessions = [
        {
            'player': random.choice(players_list),
            'duration_minutes': random.randint(5, 120),
            'mode': random.choice(game_mode_list),
            'active': random.choice([True, False])
        }
        for _ in range(5)
    ]

    return {
        'players': players_data,
        'sessions': sessions,
        'game_modes': [game_mode_list],
        'achievements': achievements
    }


def game_management() -> dict[str, any]:
    """Manage game data generation.
    Returns:
        dict: The generated game data.
    """

    players = {'alice', 'bob', 'charlie', 'diana', 'eve', 'frank'}
    achievements = {
                    "first_kill", "level_10", "level_50", "level_100",
                    "speedrun", "explorer", "treasure_hunter", "boss_slayer",
                    "collector", "perfectionist", "social_butterfly",
                    "lone_wolf", "strategist", "berserker", "pacifist",
                    "completionist"}
    game_modes = {'casual', 'competitive', 'ranked'}
    region = {"north", "south", "east", "west", "central"}

    data = assigned_random_value(players, achievements, game_modes, region)
    return data


def main() -> None:
    """Main function to run the game analytics dashboard."""

    print("=== Game Analytics Dashboard ===")
    data = game_management()
    display_list_comprehension(data)
    display_dictionary_comprehension(data)
    display_set_comprehension(data)
    display_combined_analysis(data)


if __name__ == "__main__":
    main()
