# Track encryption key, game rules, scores.
# Winning shape: losing shape
WINNING_KEY = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}

# Invert the above
LOSING_KEY = {v: k for k, v in WINNING_KEY.items()}

SHAPE_KEY = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',

    # For part 1
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

OUTCOME_KEY = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

SHAPE_SCORES = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}


def get_shape_score(shape):
    return SHAPE_SCORES[shape]


def get_game_score(your_shape, opponent_shape):
    # You win
    if WINNING_KEY[your_shape] == opponent_shape:
        return 6

    # Draw
    elif  opponent_shape == your_shape:
        return 3

    # Loss
    return 0


def determine_required_shape(opponent_shape, result):
    if result == 'win':
        return LOSING_KEY[opponent_shape]
    elif result == 'draw':
        return opponent_shape
    elif result == 'lose':
        return WINNING_KEY[opponent_shape]


def get_score_list(strategies):
    """
    Given the list of strategies, returns a list of scores for each round.
    """
    score_list = []
    for opponent_shape, your_shape in strategies:
        score_list.append(get_shape_score(your_shape) + get_game_score(your_shape, opponent_shape))
    return score_list

if __name__ == "__main__":
    # Read input into a list of tuples as (opponent_shape, your_shape)
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    strategies = []
    for strategy in lines:
        opponent, you = strategy.split()
        strategies.append((SHAPE_KEY[opponent], SHAPE_KEY[you]))

    score_list = get_score_list(strategies)
    print(f"Day 1 Part 1: {sum(score_list)}")

    # Get the list of strategies, this time using the part 2 interpretation
    strategies = []
    for strategy in lines:
        opponent, outcome = strategy.split()
        your_move = determine_required_shape(SHAPE_KEY[opponent], OUTCOME_KEY[outcome])
        strategies.append((SHAPE_KEY[opponent], your_move))

    score_list = get_score_list(strategies)
    print(f"Day 1 Part 2: {sum(score_list)}")
