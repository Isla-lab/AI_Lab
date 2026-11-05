
from envs.obsgrid_env import ObsGrid


class AquaticEnv(ObsGrid):
    """
    Fully observable aquatic environment with deterministic actions.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}

        grid = [
            ["S", "O", "O", "F", "F", "F", "F", "O", "O", "O"],
            ["O", "F", "O", "O", "O", "O", "F", "E", "F", "O"],
            ["O", "O", "F", "F", "F", "O", "F", "F", "F", "O"],
            ["F", "O", "F", "F", "E", "O", "F", "O", "F", "O"],
            ["F", "O", "F", "F", "F", "O", "F", "O", "F", "O"],
            ["F", "E", "F", "O", "O", "O", "F", "E", "F", "O"],
            ["O", "O", "O", "O", "O", "O", "F", "F", "F", "O"],
            ["O", "F", "F", "F", "O", "O", "O", "F", "F", "O"],
            ["O", "O", "O", "O", "F", "F", "F", "F", "F", "O"],
            ["F", "F", "F", "O", "O", "O", "O", "G", "O", "F"]
        ]

        rewards = {
            "S": -0.04, "O": -0.04,
            "F": -0.1, "C": -0.04,
            "R": -5.0, "E": 1.0,
            "G": 20.0
        }

        actdyn = {a: {a: 1.0} for a in actions}

        super().__init__(actions, grid, actdyn, rewards)


class AquaticSmallEnv(ObsGrid):
    """
    Smaller aquatic environment for search algorithm comparisons.
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}

        grid = [
            ["S", "O", "F", "O", "F", "O"],
            ["O", "C", "F", "O", "O", "O"],
            ["O", "O", "F", "F", "F", "F"],
            ["F", "F", "F", "W", "W", "O"],
            ["O", "W", "O", "F", "W", "W"],
            ["F", "E", "F", "O", "O", "G"]
        ]

        rewards = {
            "S": -0.04, "O": -0.04,
            "F": -0.1, "C": -0.04,
            "W": -5.0, "E": 1.0,
            "G": 20.0
        }

        actdyn = {a: {a: 1.0} for a in actions}

        super().__init__(actions, grid, actdyn, rewards)
