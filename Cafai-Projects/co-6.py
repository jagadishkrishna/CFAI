 # ===========================================================
# CO6 - Hybrid AI System
# Fault Diagnosis in Industrial Systems
# ===========================================================

import heapq

# -----------------------------------------------------------
# Machine Profile
# -----------------------------------------------------------

machine = {
    "machine_id": "M-101",
    "temperature": 95,
    "vibration": 8.4,
    "current": 18,
    "voltage": 240,
    "severity": 8
}

# -----------------------------------------------------------
# Fault Database
# -----------------------------------------------------------

fault_database = {

    "Bearing Failure": {
        "symptoms": [
            "high_vibration",
            "noise",
            "temperature_rise"
        ],
        "probability": 0.90,
        "maintenance": [
            "Replace Bearing",
            "Lubrication"
        ],
        "cost": 2
    },

    "Motor Failure": {
        "symptoms": [
            "high_current",
            "power_loss",
            "overheating"
        ],
        "probability": 0.75,
        "maintenance": [
            "Replace Motor"
        ],
        "cost": 3
    },

    "Overheating": {
        "symptoms": [
            "high_temperature",
            "cooling_issue"
        ],
        "probability": 0.60,
        "maintenance": [
            "Cooling System Check"
        ],
        "cost": 1
    },

    "Sensor Failure": {
        "symptoms": [
            "invalid_readings",
            "signal_loss"
        ],
        "probability": 0.40,
        "maintenance": [
            "Sensor Calibration"
        ],
        "cost": 2
    }
}

# -----------------------------------------------------------
# Explainability Logs
# -----------------------------------------------------------

logs = []

# -----------------------------------------------------------
# Heuristic Function
# -----------------------------------------------------------

def heuristic(observed, symptoms):

    return sum(
        1
        for s in symptoms
        if s not in observed
    )

# -----------------------------------------------------------
# A* Search
# -----------------------------------------------------------

def a_star_fault_search():

    print("\nA* SEARCH ANALYSIS:\n")

    observed = [
        "high_vibration",
        "temperature_rise"
    ]

    pq = []

    for fault, info in fault_database.items():

        g = info["cost"]

        h = heuristic(
            observed,
            info["symptoms"]
        )

        f = g + h

        heapq.heappush(
            pq,
            (f, fault)
        )

    ranking = []

    while pq:

        score, fault = heapq.heappop(pq)

        print(
            f"  {fault:<20}"
            f"f(n) = {score}"
        )

        ranking.append(fault)

    return ranking

# -----------------------------------------------------------
# Safe Maintenance Check
# -----------------------------------------------------------

def safe_maintenance():

    print(
        "\nMAINTENANCE VALIDATION:\n"
    )

    valid_actions = {}

    for fault, info in fault_database.items():

        valid_actions[fault] = info["maintenance"]

        print(
            f"  {fault:<20}"
            f"{info['maintenance']}"
        )

    return valid_actions

# -----------------------------------------------------------
# Bayesian Reasoning
# -----------------------------------------------------------

def probabilistic_reasoning():

    print(
        "\nPROBABILISTIC ANALYSIS:\n"
    )

    results = {}

    for fault, info in fault_database.items():

        probability = (
            info["probability"]
        )

        results[fault] = probability

        print(
            f"  {fault:<20}"
            f"{probability:.2f}"
        )

    return results

# -----------------------------------------------------------
# Utility Function
# -----------------------------------------------------------

def utility_function(
        probability,
        maintenance_count,
        severity):

    utility = (
        probability * 100
        -
        maintenance_count * 5
        +
        severity
    )

    return round(
        utility,
        2
    )

# -----------------------------------------------------------
# Best Decision Selection
# -----------------------------------------------------------

def decision_engine(
        probabilities,
        maintenance_actions):

    print(
        "\nDECISION ENGINE:\n"
    )

    best_fault = None

    best_utility = -999

    for fault in probabilities:

        utility = utility_function(
            probabilities[fault],
            len(
                maintenance_actions[fault]
            ),
            machine["severity"]
        )

        print(
            f"  {fault:<20}"
            f"Utility = {utility}"
        )

        if utility > best_utility:

            best_utility = utility

            best_fault = fault

    return (
        best_fault,
        best_utility
    )

# -----------------------------------------------------------
# Explainability Module
# -----------------------------------------------------------

def explain_result(
        final_fault,
        maintenance_actions):

    print(
        "\nEXPLAINABILITY REPORT:\n"
    )

    print(
        f"Machine ID      : "
        f"{machine['machine_id']}"
    )

    print(
        f"Temperature     : "
        f"{machine['temperature']} °C"
    )

    print(
        f"Vibration       : "
        f"{machine['vibration']}"
    )

    print(
        f"Current         : "
        f"{machine['current']} A"
    )

    print(
        f"\nPredicted Fault : "
        f"{final_fault}"
    )

    print(
        f"\nRecommended Maintenance:"
    )

    for action in maintenance_actions[
        final_fault
    ]:

        print(f"  - {action}")

    print(
        "\nReasoning:"
    )

    print(
        "  High vibration detected."
    )

    print(
        "  Fault probability highest."
    )

    print(
        "  Utility score maximum."
    )

# -----------------------------------------------------------
# Failure Analysis
# -----------------------------------------------------------

def failure_analysis():

    print(
        "\nFAILURE ANALYSIS:\n"
    )

    issues = [

        "Limited fault database",

        "Probabilities manually assigned",

        "No real-time IoT integration",

        "No historical maintenance data"
    ]

    for issue in issues:

        print(
            f"  - {issue}"
        )

# -----------------------------------------------------------
# Ethics & Limitations
# -----------------------------------------------------------

def ethics_limitations():

    print(
        "\nETHICS & LIMITATIONS:\n"
    )

    points = [

        "Human expert validation required",

        "Not a replacement for engineers",

        "May miss rare failures",

        "Sensor data privacy must be protected"
    ]

    for point in points:

        print(
            f"  - {point}"
        )

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 60)
print("FAULT DIAGNOSIS IN INDUSTRIAL SYSTEMS")
print("CO6 - HYBRID AI SYSTEM")
print("=" * 60)

# Search Analysis

search_result = a_star_fault_search()

# Maintenance Validation

maintenance_actions = safe_maintenance()

# Probabilistic Analysis

probabilities = probabilistic_reasoning()

# Decision Making

final_fault, utility = decision_engine(
    probabilities,
    maintenance_actions
)

print(
    f"\nFINAL FAULT DIAGNOSIS : "
    f"{final_fault}"
)

print(
    f"UTILITY SCORE         : "
    f"{utility}"
)

# Explainability

explain_result(
    final_fault,
    maintenance_actions
)

# Performance Summary

print(
    "\nPERFORMANCE SUMMARY:\n"
)

print(
    f"Faults Evaluated : "
    f"{len(fault_database)}"
)

print(
    f"Severity Level   : "
    f"{machine['severity']}/10"
)

print(
    f"Machine ID       : "
    f"{machine['machine_id']}"
)

# Failure Analysis

failure_analysis()

# Ethics

ethics_limitations()

print("\n" + "=" * 60)
print("HYBRID AI PROCESS COMPLETED")
print("=" * 60)