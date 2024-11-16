import random
from environment import coloringNinja
from Node import Node

def generate_neighbors(environment, node):
    """
    Generates all possible neighbors for the given node.
    """
    neighbors = []
    for action in ["color", "move left", "move right"]:
        neighbor = Node.child(environment, node, action)
        neighbors.append(neighbor)
    return neighbors

def evaluate(environment, node):
    """
    Evaluates the quality of the current node.
    Example: Reward more completed cells in the line.
    """
    completed_cells = sum(1 for cell in environment.line if cell != 0)
    return completed_cells

def hill_climbing(environment, verbose=False):
    """
    Implements the Hill-Climbing algorithm for the coloringNinja environment.
    """
    # Initialize the root node and environment state
    current = Node.root(environment)
    current_score = evaluate(environment, current)

    if verbose:
        print("Initial state:")
        environment.displayLineState()
        print(f"Initial Score: {current_score}")

    while True:
        neighbors = generate_neighbors(environment, current)
        next_state = None
        best_score = current_score

        for neighbor in neighbors:
            environment.line = list(neighbor.state[:len(environment.line)])
            environment.agentPosition = neighbor.state[len(environment.line)]
            environment.savings = neighbor.state[len(environment.line) + 1]
            environment.paletteQuantity = dict(neighbor.state[len(environment.line) + 2])

            score = evaluate(environment, neighbor)
            if score > best_score:
                best_score = score
                next_state = neighbor

        if next_state is None:  # No better neighbor found
            if verbose:
                print("Reached local maximum.")
            break

        current = next_state
        current_score = best_score

        if verbose:
            print("Moved to new state:")
            environment.displayLineState()
            print(f"New Score: {current_score}")

    return current, current_score
