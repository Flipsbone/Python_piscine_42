#!/usr/bin/env python3

import random

def display_list_comprehension(data: dict[str,any]) -> None:
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



def display_set_comprehension(data: dict[str,any]) -> None:
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

    players_list = list(players)
    game_mode_list = list(game_mode)
    achievements_list = list(achievements)
    region_list = list(region)

    # Player statistics
    players_data = {} 
    for player in players:
        nb_achievement = random.randint(1, len(achievements))
        unlock_achivement = random.sample(achievements_list, k=nb_achievement)
        players_data[player] = {
            'level': random.randint(1, 50),
            'total_score': random.randint(10, 3000),
            'sessions_played': random.randint(10, 100),
            'favorite_mode': random.choice(game_mode_list),
            'achievements_count': nb_achievement,
            'achievement_event': unlock_achivement,
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

def game_management() -> dict[str,any]:
    players = {'alice', 'bob', 'charlie', 'diana', 'eve', 'frank'}
    achievements = {
                    "first_kill", "level_10", "level_50", "level_100",
                    "speedrun", "explorer", "treasure_hunter", "boss_slayer",
                    "collector", "perfectionist", "social_butterfly",
                    "lone_wolf", "strategist", "berserker", "pacifist",
                    "completionist"}
    game_modes = {'casual', 'competitive', 'ranked'}
    region = {"north", "south", "east", "west", "central"}
    hight_score_threshold = 2000

    data = assigned_random_value(players, achievements, game_modes, region)
    return data

def main() -> None:
    print("=== Game Analytics Dashboard ===")
    data = game_management()
    display_list_comprehension(data)
    display_set_comprehension(data)

if __name__ == "__main__":
    main()
