#!/usr/bin/env python3
""" Player Score Analytics: A script to analyze player scores
provided as command-line arguments."""

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        nb_args = len(sys.argv)
        lst_scores = []
        for score in sys.argv[1:]:
            try:
                score = int(score)
                lst_scores.append(score)
            except ValueError:
                print(f"Invalid '{score}' must be number")

        if len(lst_scores) > 0:
            print(f"Scores processed: {lst_scores}")

            player = len(lst_scores)
            print(f"Total players: {player}")

            sum_scores = sum(lst_scores)
            print(f"Total score: {sum_scores}")

            average_score = sum_scores / player
            print(f"Average score: {average_score}")

            high_score = max(lst_scores)
            print(f"High score: {high_score}")

            min_score = min(lst_scores)
            print(f"Low score: {min_score}")

            score_range = high_score - min_score
            print(f"Score range: {score_range}")
