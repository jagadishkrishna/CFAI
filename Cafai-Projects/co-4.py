# ===========================================================
# CO4 - Decision Making & Game Reasoning
# Fault Diagnosis in Industrial Systems
# ===========================================================

import math
import random

# -----------------------------------------------------------
# Machine Profile
# -----------------------------------------------------------

machine = {
    "machine_id": "M-101",
    "temperature": 95,
    "vibration": 8.5,
    "current": 18,
    "severity": 8
}

# -----------------------------------------------------------
# Maintenance Actions Database
# success_rate = benefit (%)
# risk = failure risk (%)
# cost = maintenance cost
# -----------------------------------------------------------

maintenance_actions = {

    "Replace Bearing": {
        "success_rate": 95,
        "risk": 5,
        "cost": 60
    },

    "Replace Motor": {
        "success_rate": 92,
        "risk": 8,
        "cost": 100
    },

    "Lubrication": {
        "success_rate": 75,
        "risk": 12,
        "cost": 20
    },

    "Sensor Calibration": {
        "success_rate": 85,
        "risk": 10,
        "cost": 30
    }
}

# -----------------------------------------------------------
# Utility Function
# Utility = Success - Risk - Cost Factor
# -----------------------------------------------------------

def compute_utility(success_rate, risk, cost):

    utility = success_rate - risk - (cost * 0.25)

    return round(utility, 2)

# -----------------------------------------------------------
# Evaluate Action
# -----------------------------------------------------------

def evaluate(action):

    data = maintenance_actions[action]

    return compute_utility(
        data["success_rate"],
        data["risk"],
        data["cost"]
    )

# -----------------------------------------------------------
# Minimax Algorithm
# -----------------------------------------------------------

def minimax(depth, maximizing, actions):

    if depth == 0 or not actions:
        return 0

    if maximizing:

        best = -math.inf

        for action in actions:

            value = evaluate(action)

            best = max(
                best,
                value + minimax(depth - 1, False, [])
            )

        return best

    else:

        worst = math.inf

        for action in actions:

            value = evaluate(action)

            worst = min(
                worst,
                value - minimax(depth - 1, True, [])
            )

        return worst

# -----------------------------------------------------------
# Alpha Beta Pruning
# -----------------------------------------------------------

def alpha_beta(depth, alpha, beta,
               maximizing, actions):

    if depth == 0 or not actions:
        return 0

    if maximizing:

        value = -math.inf

        for action in actions:

            score = evaluate(action)

            value = max(value, score)

            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return value

    else:

        value = math.inf

        for action in actions:

            score = evaluate(action)

            value = min(value, score)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value

# -----------------------------------------------------------
# Select Best Maintenance Policy
# -----------------------------------------------------------

def select_best_policy():

    best_action = None
    best_score = -math.inf

    print("\nUtility Scores:\n")

    for action in maintenance_actions:

        score = evaluate(action)

        print(
            f"  {action:<20}"
            f"Utility = {score}"
        )

        if score > best_score:

            best_score = score
            best_action = action

    return best_action, best_score

# -----------------------------------------------------------
# Iterative Deepening Search
# -----------------------------------------------------------

def iterative_deepening(max_depth):

    print("\nIterative Deepening Search:\n")

    for depth in range(1, max_depth + 1):

        score = minimax(
            depth,
            True,
            list(maintenance_actions.keys())
        )

        print(
            f"  Depth {depth}"
            f" -> Best Score = {score}"
        )

# -----------------------------------------------------------
# Expectimax
# -----------------------------------------------------------

def expectimax():

    print("\nExpectimax Results:\n")

    for action, data in maintenance_actions.items():

        p_success = data["success_rate"] / 100

        p_fail = 1 - p_success

        expected_utility = (
            p_success * 100
            -
            p_fail * data["risk"]
        )

        print(
            f"  {action:<20}"
            f"Expected Utility = "
            f"{expected_utility:.2f}"
        )

# -----------------------------------------------------------
# Bounded Rationality
# -----------------------------------------------------------

def bounded_rationality():

    return random.choice(
        list(maintenance_actions.keys())
    )

# -----------------------------------------------------------
# Multi Agent Decision Making
# -----------------------------------------------------------

def multi_agent_reasoning():

    print("\nMulti-Agent Reasoning:\n")

    engineer_agent = "Replace Bearing"

    manager_agent = "Lubrication"

    sensor_agent = "Replace Bearing"

    print(
        f"  Engineer Agent : "
        f"{engineer_agent}"
    )

    print(
        f"  Manager Agent  : "
        f"{manager_agent}"
    )

    print(
        f"  Sensor Agent   : "
        f"{sensor_agent}"
    )

    final_decision = engineer_agent

    print(
        f"\n  Final Decision : "
        f"{final_decision}"
    )

    return final_decision

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 55)
print("FAULT DIAGNOSIS IN INDUSTRIAL SYSTEMS")
print("CO4 - DECISION MAKING & GAME REASONING")
print("=" * 55)

print(
    f"\nMachine ID : "
    f"{machine['machine_id']}"
)

print(
    f"Temperature: "
    f"{machine['temperature']} °C"
)

print(
    f"Vibration  : "
    f"{machine['vibration']}"
)

print(
    f"Current    : "
    f"{machine['current']} A"
)

print(
    f"Severity   : "
    f"{machine['severity']}/10"
)

# Best Policy

best_action, best_score = select_best_policy()

print(
    f"\nSelected Action : "
    f"{best_action}"
)

print(
    f"Utility Score   : "
    f"{best_score}"
)

# Minimax

minimax_score = minimax(
    2,
    True,
    list(maintenance_actions.keys())
)

print(
    f"\nMinimax Score = "
    f"{minimax_score}"
)

# Alpha Beta

ab_score = alpha_beta(
    2,
    -math.inf,
    math.inf,
    True,
    list(maintenance_actions.keys())
)

print(
    f"Alpha-Beta Score = "
    f"{ab_score}"
)

# Iterative Deepening

iterative_deepening(3)

# Expectimax

expectimax()

# Quick Decision

quick_pick = bounded_rationality()

print(
    f"\nBounded Rationality Pick : "
    f"{quick_pick}"
)

# Multi Agent

final_action = multi_agent_reasoning()

print("\n" + "=" * 55)
print("DECISION PROCESS COMPLETED")
print("=" * 55)