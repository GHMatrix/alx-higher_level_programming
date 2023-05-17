#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = max(a_dictionary.values())
    best_keys = [k for k, v in a_dictionary.items() if v == max_score]
    return best_keys[0]
