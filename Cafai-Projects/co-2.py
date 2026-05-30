 # ===========================================================
# CO2 - Search Algorithms
# Fault Diagnosis in Industrial Systems
# ===========================================================

from collections import deque
import heapq
import time

# -----------------------------------------------------------
# Industrial Fault Database with Costs
# -----------------------------------------------------------

FAULT_DB = {

    "Motor Failure": {
        "symptoms": [
            "overheating",
            "vibration",
            "noise",
            "power_loss",
            "burning_smell"
        ],
        "cost": 3
    },

    "Bearing Defect": {
        "symptoms": [
            "vibration",
            "noise",
            "friction",
            "temperature_rise"
        ],
        "cost": 2
    },

    "Sensor Malfunction": {
        "symptoms": [
            "incorrect_reading",
            "signal_loss",
            "fluctuation",
            "calibration_error"
        ],
        "cost": 1
    },

    "Pump Failure": {
        "symptoms": [
            "low_pressure",
            "leakage",
            "noise",
            "overheating"
        ],
        "cost": 4
    },

    "Short Circuit": {
        "symptoms": [
            "spark",
            "power_loss",
            "burning_smell",
            "system_shutdown"
        ],
        "cost": 2
    }
}

# -----------------------------------------------------------
# Machine Symptoms for Search
# -----------------------------------------------------------

SEARCH_MACHINE_SYMPTOMS = [
    "overheating",
    "noise",
    "vibration"
]

# -----------------------------------------------------------
# Heuristic Function
# h(n) = Number of unmatched symptoms
# -----------------------------------------------------------

def heuristic_unmatched(machine_symptoms, fault_symptoms):

    unmatched = 0

    for symptom in fault_symptoms:

        if symptom not in machine_symptoms:
            unmatched += 1

    return unmatched

# -----------------------------------------------------------
# BFS Search
# -----------------------------------------------------------

def bfs_search():

    print("\n" + "=" * 40)
    print("BREADTH FIRST SEARCH (BFS)")
    print("=" * 40)

    start_time = time.time()

    queue = deque(FAULT_DB.keys())
    visited = set()
    node_expansions = 0

    while queue:

        fault = queue.popleft()

        if fault not in visited:

            visited.add(fault)
            node_expansions += 1

            matched = [
                s for s in FAULT_DB[fault]["symptoms"]
                if s in SEARCH_MACHINE_SYMPTOMS
            ]

            print(f"Visited: {fault} | Matched Symptoms: {matched}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# DFS Search
# -----------------------------------------------------------

def dfs_recursive(faults, visited, node_expansions):

    if not faults:
        return node_expansions

    fault = faults.pop()

    if fault not in visited:

        visited.add(fault)
        node_expansions += 1

        matched = [
            s for s in FAULT_DB[fault]["symptoms"]
            if s in SEARCH_MACHINE_SYMPTOMS
        ]

        print(f"Visited: {fault} | Matched Symptoms: {matched}")

    return dfs_recursive(faults, visited, node_expansions)


def dfs_search():

    print("\n" + "=" * 40)
    print("DEPTH FIRST SEARCH (DFS)")
    print("=" * 40)

    start_time = time.time()

    faults = list(FAULT_DB.keys())
    visited = set()

    node_expansions = dfs_recursive(faults, visited, 0)

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# Uniform Cost Search (UCS)
# -----------------------------------------------------------

def ucs_search():

    print("\n" + "=" * 40)
    print("UNIFORM COST SEARCH (UCS)")
    print("=" * 40)

    start_time = time.time()

    priority_queue = []
    visited = set()
    node_expansions = 0

    for fault, info in FAULT_DB.items():
        heapq.heappush(priority_queue, (info["cost"], fault))

    while priority_queue:

        cost, fault = heapq.heappop(priority_queue)

        if fault not in visited:

            visited.add(fault)
            node_expansions += 1

            print(f"Visited: {fault} | Cost: {cost}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# Greedy Best First Search
# -----------------------------------------------------------

def greedy_search():

    print("\n" + "=" * 40)
    print("GREEDY BEST FIRST SEARCH")
    print("=" * 40)

    start_time = time.time()

    priority_queue = []
    visited = set()
    node_expansions = 0

    for fault, info in FAULT_DB.items():

        h = heuristic_unmatched(
            SEARCH_MACHINE_SYMPTOMS,
            info["symptoms"]
        )

        heapq.heappush(priority_queue, (h, fault))

    while priority_queue:

        h, fault = heapq.heappop(priority_queue)

        if fault not in visited:

            visited.add(fault)
            node_expansions += 1

            print(f"Visited: {fault} | Heuristic h(n): {h}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# A* Search
# -----------------------------------------------------------

def a_star_search():

    print("\n" + "=" * 40)
    print("A* SEARCH ALGORITHM")
    print("=" * 40)

    start_time = time.time()

    open_set = []
    closed_set = set()
    node_expansions = 0
    tie_breaker = 0

    for fault, info in FAULT_DB.items():

        g = info["cost"]

        h = heuristic_unmatched(
            SEARCH_MACHINE_SYMPTOMS,
            info["symptoms"]
        )

        f = g + h

        heapq.heappush(open_set, (f, tie_breaker, fault))
        tie_breaker += 1

    while open_set:

        f, _, fault = heapq.heappop(open_set)

        if fault not in closed_set:

            closed_set.add(fault)
            node_expansions += 1

            print(f"Visited: {fault} | f(n) = g + h = {f}")

    end_time = time.time()

    print(f"\nTotal Node Expansions: {node_expansions}")
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 55)
print("FAULT DIAGNOSIS IN INDUSTRIAL SYSTEMS")
print("CO2 - SEARCH ALGORITHMS")
print("=" * 55)

print(f"\nMachine Symptoms: {SEARCH_MACHINE_SYMPTOMS}")

bfs_search()
dfs_search()
ucs_search()
greedy_search()
a_star_search()

print("\n" + "=" * 55)
print("FAULT DIAGNOSIS COMPLETED")
print("=" * 55)