# ===========================================================
# CO5 - Probabilistic Reasoning
# Fault Diagnosis in Industrial Systems
# ===========================================================

import random

# -----------------------------------------------------------
# Machine Profile
# -----------------------------------------------------------

machine = {
    "machine_id": "M-101",
    "temperature": 95,
    "vibration": 8.4,
    "current": 18,
    "voltage": 240
}

# -----------------------------------------------------------
# Fault Prior Probabilities
# -----------------------------------------------------------

fault_priors = {
    "Bearing Failure": 0.40,
    "Motor Failure": 0.30,
    "Overheating": 0.20,
    "Sensor Failure": 0.10
}

# -----------------------------------------------------------
# Likelihood P(Evidence | Fault)
# -----------------------------------------------------------

likelihoods = {
    "Bearing Failure": 0.90,
    "Motor Failure": 0.75,
    "Overheating": 0.60,
    "Sensor Failure": 0.40
}

# -----------------------------------------------------------
# Evidence Probability
# -----------------------------------------------------------

evidence_probability = 0.50

# -----------------------------------------------------------
# Bayesian Network
# -----------------------------------------------------------

bayesian_network = {

    "Bearing Failure": [
        "high_vibration",
        "noise",
        "temperature_rise"
    ],

    "Motor Failure": [
        "high_current",
        "overheating",
        "power_loss"
    ],

    "Overheating": [
        "high_temperature",
        "cooling_issue"
    ],

    "Sensor Failure": [
        "invalid_readings",
        "signal_loss"
    ]
}

# -----------------------------------------------------------
# Bayes Theorem
# -----------------------------------------------------------

def bayes_theorem(prior,
                  likelihood,
                  evidence):

    return (
        likelihood * prior
    ) / evidence

# -----------------------------------------------------------
# Bayesian Inference
# -----------------------------------------------------------

def bayesian_inference():

    print("\nBayesian Inference Results:\n")

    results = {}

    for fault in fault_priors:

        posterior = bayes_theorem(
            fault_priors[fault],
            likelihoods[fault],
            evidence_probability
        )

        results[fault] = posterior

        print(
            f"  {fault:<20}"
            f"Posterior = "
            f"{posterior:.4f}"
        )

    best_fault = max(
        results,
        key=results.get
    )

    print(
        f"\nMost Probable Fault: "
        f"{best_fault}"
    )

    return results

# -----------------------------------------------------------
# Variable Elimination
# -----------------------------------------------------------

def variable_elimination():

    print("\nVariable Elimination:\n")

    hidden_variable = "machine_health"

    print(
        f"Eliminating Hidden Variable: "
        f"{hidden_variable}"
    )

    combined = sum(
        fault_priors[f] *
        likelihoods[f]
        for f in fault_priors
    )

    print(
        f"Combined Marginal Probability = "
        f"{combined:.4f}"
    )

# -----------------------------------------------------------
# Belief Propagation
# -----------------------------------------------------------

def belief_propagation():

    print("\nBelief Propagation:\n")

    observed = [
        "high_vibration",
        "temperature_rise"
    ]

    for fault, symptoms in bayesian_network.items():

        matched = sum(
            1
            for s in symptoms
            if s in observed
        )

        belief = matched / len(symptoms)

        print(
            f"  {fault:<20}"
            f"Belief Score = "
            f"{belief:.2f}"
        )

# -----------------------------------------------------------
# Rejection Sampling
# -----------------------------------------------------------

def rejection_sampling(samples=1000):

    print("\nRejection Sampling:\n")

    accepted = sum(
        1
        for _ in range(samples)
        if random.random() < 0.60
    )

    estimate = accepted / samples

    print(
        f"Estimated Probability = "
        f"{estimate:.4f}"
    )

# -----------------------------------------------------------
# Likelihood Weighting
# -----------------------------------------------------------

def likelihood_weighting(samples=1000):

    print("\nLikelihood Weighting:\n")

    weights = [
        random.uniform(0.5, 1.0)
        for _ in range(samples)
    ]

    estimate = (
        sum(weights)
        / len(weights)
    )

    print(
        f"Weighted Estimate = "
        f"{estimate:.4f}"
    )

# -----------------------------------------------------------
# Markov Chain
# -----------------------------------------------------------

def markov_chain(steps=6):

    print("\nMarkov Chain Simulation:\n")

    states = [
        "Normal",
        "Warning",
        "Faulty",
        "Maintenance"
    ]

    current = "Normal"

    for step in range(steps):

        print(
            f"Step {step+1}: "
            f"{current}"
        )

        if current == "Normal":
            current = random.choice(
                ["Normal", "Warning"]
            )

        elif current == "Warning":
            current = random.choice(
                ["Warning", "Faulty"]
            )

        elif current == "Faulty":
            current = random.choice(
                ["Faulty", "Maintenance"]
            )

        else:
            current = random.choice(
                ["Maintenance", "Normal"]
            )

# -----------------------------------------------------------
# Hidden Markov Model
# -----------------------------------------------------------

def hmm_tracking():

    print("\nHidden Markov Model:\n")

    hidden_states = [
        "Healthy",
        "Degrading",
        "Failed"
    ]

    observations = [
        "Normal Reading",
        "High Vibration",
        "High Temperature",
        "Current Spike"
    ]

    for _ in range(5):

        hidden = random.choice(
            hidden_states
        )

        observed = random.choice(
            observations
        )

        print(
            f"Hidden State: "
            f"{hidden:<12}"
            f"| Observation: "
            f"{observed}"
        )

# -----------------------------------------------------------
# Sensor Fusion
# -----------------------------------------------------------

def sensor_fusion():

    print(
        "\nSensor Fusion Analysis:\n"
    )

    temperature = machine["temperature"]
    vibration = machine["vibration"]
    current = machine["current"]

    print(
        f"Temperature : "
        f"{temperature}"
    )

    print(
        f"Vibration   : "
        f"{vibration}"
    )

    print(
        f"Current     : "
        f"{current}"
    )

    if vibration > 8:

        print(
            "\nAlert: Bearing Failure "
            "Highly Suspected"
        )

    elif temperature > 90:

        print(
            "\nAlert: Overheating "
            "Detected"
        )

# -----------------------------------------------------------
# Expected Utility
# -----------------------------------------------------------

def expected_utility():

    print(
        "\nExpected Utility "
        "of Maintenance Actions:\n"
    )

    actions = {

        "Replace Bearing": {
            "p_success": 0.95,
            "utility": 95
        },

        "Replace Motor": {
            "p_success": 0.92,
            "utility": 90
        },

        "Lubrication": {
            "p_success": 0.75,
            "utility": 70
        }
    }

    for action, data in actions.items():

        value = (
            data["p_success"]
            *
            data["utility"]
        )

        print(
            f"  {action:<20}"
            f"Expected Utility = "
            f"{value:.2f}"
        )

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 55)
print("FAULT DIAGNOSIS IN INDUSTRIAL SYSTEMS")
print("CO5 - PROBABILISTIC REASONING")
print("=" * 55)

print(
    f"\nMachine ID : "
    f"{machine['machine_id']}"
)

bayesian_inference()

print("\nBayesian Network:\n")

for fault, symptoms in bayesian_network.items():

    print(
        f"  {fault} -> "
        f"{symptoms}"
    )

variable_elimination()
belief_propagation()
rejection_sampling()
likelihood_weighting()
markov_chain()
hmm_tracking()
sensor_fusion()
expected_utility()

print("\n" + "=" * 55)
print("PROBABILISTIC REASONING COMPLETED")
print("=" * 55)