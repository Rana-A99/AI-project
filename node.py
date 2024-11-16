from environment import coloringNinja
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # Tuple containing line, agent position, savings, and palette
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    @staticmethod
    def root(environment):
        line, agentPosition, savings = environment.getState()
        palette = tuple(environment.paletteQuantity.items())
        state = (*line, agentPosition, savings, palette)
        return Node(state)

    @staticmethod
    def child(environment, parent_node, action):
        *line, agentPosition, savings, palette = parent_node.state
        palette = dict(palette)

        # Reconstruct the environment state
        new_env = coloringNinja()
        new_env.line = list(line)
        new_env.agentPosition = agentPosition
        new_env.savings = savings
        new_env.paletteQuantity = palette

        # Perform the action
        if action == "color":
            new_env.colorCells()
        elif action == "skip":
            pass  # Skipping does not modify the environment
        elif action == "move left":
            new_env.moveAgent("left")
        elif action == "move right":
            new_env.moveAgent("right")

        # Create the new state
        new_state = (*new_env.line, new_env.agentPosition, new_env.savings, tuple(new_env.paletteQuantity.items()))
        return Node(new_state, parent_node, action)
