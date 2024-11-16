class coloringNinja(): 
    def __init__(self, lineSize=6, paletteCost=3, points=1, paletteQuantitiy=2):
        self.size = lineSize
        self.colorList = ["🍓", "🐳", "🐸", "🌸"]
        self.paletteCost = paletteCost
        self.paletteQuantity = {color: paletteQuantitiy for color in self.colorList}
        self.points = points
        self.savings = 0
        self.line = ["uncolored"] * lineSize
        self.agentPosition = 0
        self.moves = 0

        self.initialState = self.getState()
        self.goalState = self.getGoalState()

    def displayLineState(self):
                """
                Displays the current state of the environment, including the line, agent position, savings, and palette quantities.
                """
                print("Current line state:")
                for index, cell in enumerate(self.line):
                    marker = "🔲" if cell == "uncolored" else "✅"
                    print(f"Position {index+1}: {cell} {marker}")
                print(f"Agent Position: {self.agentPosition}")
                print(f"Savings: {self.savings}, Points: {self.points}")
                print(f"Palette Quantities: {self.paletteQuantity}")

    def getState(self):
        return self.line, self.agentPosition, self.savings

    def getGoalState(self):
        goal = ["uncolored"] * self.size
        for pos in range(self.size):
            goal[pos] = self.getColorForPosition(pos)
            
        return tuple(goal)

    def getColorForPosition(self, pos):
        
        if (pos+1) % 2 == 0:
            return "🍓"
        elif (pos+1) % 3 == 0:
            return "🐸"
        elif (pos+1) % 5 == 0:
            return "🐳"
        
        return "🌸"

    def isGoal(self):
        if self.line == self.goalState:
            print("goal raeched")

    def printGoalState(self):
        print("Goal state:", self.goalState)

    def colorCells(self):
        # Only try to color if the cell is uncolored
        if self.line[self.agentPosition] == "uncolored":
            color = self.getColorForPosition(self.agentPosition)
            print(f"Attempting to color position {self.agentPosition} with {color}")

            if self.paletteQuantity[color] > 0:  # Coloring is possible
                self.line[self.agentPosition] = color
                self.paletteQuantity[color] -= 1
                self.savings += self.points
            else:  # Attempt refill if savings allow
                if self.savings >= self.paletteCost:
                    self.savings -= self.paletteCost
                    self.paletteQuantity[color] = 2 # Refill palette
                    self.line[self.agentPosition] = color
                    self.paletteQuantity[color] -= 1
                    self.savings += self.points
                else:  # Mark as skipped if coloring fails
                    print(f"Skipped cell at {self.agentPosition} due to insufficient resources.")
                    return False  # Skipped
            return True  # Colored successfully
        return None  # Already colored

    def moveAgent(self, direction):
        if direction == "left" and self.agentPosition > 0:
            self.agentPosition -= 1
            self.moves += 1
            return True
        elif direction == "right" and self.agentPosition < len(self.line) - 1:
            self.agentPosition += 1
            self.moves += 1
            return True
        else:
            print("Invalid move")
            return False

    def getActions(self, direction):
        actions = []
        skipped_positions = []

        while "uncolored" in self.line:
            success = self.colorCells()
            if success:
                color = self.line[self.agentPosition]
                actions.append(("color", color))
            elif success is False:  # Mark skipped cell
                skipped_positions.append(self.agentPosition)
                actions.append(("skipped", self.agentPosition))

            # Move the agent based on the direction
            if not self.moveAgent(direction):
                if skipped_positions:  # Revisit skipped positions
                    self.agentPosition = skipped_positions.pop(0)
                    print(f"Revisiting skipped cell at position {self.agentPosition}.")
                    continue
                else:  # End of line handling
                    break

        return actions

    
    
ninja = coloringNinja()
ninja.printGoalState()


# def test_color_cells():
#     ninja = coloringNinja(lineSize=32, paletteQuantitiy=2)  # Extended line size for position 24
#     ninja.agentPosition = 24  # Start at position 24 for testing

#     # Try to color the cells and check the results
#     ninja.colorCells()  # Should color position 24 ("blue")
#     assert ninja.line[24] == "blue", f"Expected 'blue' at position 24, but got {ninja.line[24]}"
#     assert ninja.paletteQuantity["blue"] == 1, f"Expected 1 'blue' palette, but got {ninja.paletteQuantity['blue']}"
    
#     print("Color cells test passed!")

# test_color_cells()

# test_color_cells()


# def run_tests():

#     test_color_cells()


# run_tests()


    
