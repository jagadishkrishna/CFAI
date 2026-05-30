# ===========================================================
# CO3 - Constraint Satisfaction Problem (CSP)
# Fault Diagnosis in Industrial Systems
# ===========================================================

import random

# -----------------------------------------------------------
# Machine Profile
# -----------------------------------------------------------

machine = {
    "machine_id": "MCH-204",
    "type": "Industrial Conveyor System",
    "symptoms": [
        "overheating",
        "vibration",
        "noise",
        "slow_speed"
    ],
    "restricted_repairs": [
        "coolant_flush",
        "motor_replacement"
    ],
    "maintenance_history": "Last serviced 6 months ago"
}

# -----------------------------------------------------------
# Fault Variables and Repair Domains
# -----------------------------------------------------------

fault_variables = {
    "Motor_Failure": [
        "bearing_replacement",
        "motor_replacement",
        "lubrication"
    ],

    "Overheating_Issue": [
        "coolant_flush",
        "fan_cleaning",
        "thermal_check"
    ],

    "Belt_Misalignment": [
        "belt_adjustment",
        "pulley_alignment",
        "lubrication"
    ],

    "Sensor_Failure": [
        "sensor_reset",
        "sensor_replacement",
        "wiring_check"
    ],

    "Gearbox_Fault": [
        "gear_oil_change",
        "gear_replacement",
        "vibration_analysis"
    ]
}

# -----------------------------------------------------------
# Diagnostic Logs
# -----------------------------------------------------------

diagnosis_logs = []

# -----------------------------------------------------------
# Constraint Check
# -----------------------------------------------------------

def is_repair_safe(repair):

    for restricted in machine["restricted_repairs"]:

        if repair.lower() == restricted.lower():

            diagnosis_logs.append(
                f"[REJECTED] {repair} -> Restricted repair operation."
            )

            return False

    return True

# -----------------------------------------------------------
# Forward Checking
# -----------------------------------------------------------

def forward_checking_faults(domains):

    print("\nForward Checking Results:\n")

    valid_domains = {}

    for fault, repairs in domains.items():

        safe_repairs = [
            r for r in repairs
            if is_repair_safe(r)
        ]

        valid_domains[fault] = safe_repairs

        print(f"  {fault} -> {safe_repairs}")

    return valid_domains

# -----------------------------------------------------------
# MRV Heuristic
# -----------------------------------------------------------

def mrv_heuristic(domains):

    selected = min(
        domains,
        key=lambda x: len(domains[x])
    )

    return selected

# -----------------------------------------------------------
# Degree Heuristic
# -----------------------------------------------------------

def degree_heuristic(domains):

    selected = max(
        domains,
        key=lambda x: len(domains[x])
    )

    return selected

# -----------------------------------------------------------
# LCV Heuristic
# -----------------------------------------------------------

def lcv_order(values):

    return sorted(values)

# -----------------------------------------------------------
# Backtracking Algorithm
# -----------------------------------------------------------

def backtracking_csp(assignment, domains):

    if len(domains) == 0:
        return assignment

    variable = mrv_heuristic(domains)

    ordered_values = lcv_order(domains[variable])

    for value in ordered_values:

        if is_repair_safe(value):

            assignment[variable] = value

            diagnosis_logs.append(
                f"[ASSIGNED] {value} -> {variable}"
            )

            reduced_domains = {
                k: v for k, v in domains.items()
                if k != variable
            }

     

            diagnosis_logs.append(
                f"[BACKTRACK] Removing {value}"
            )

            assignment.pop(variable)

    return None

# -----------------------------------------------------------
# Min-Conflicts Algorithm
# -----------------------------------------------------------

def min_conflicts_faults(domains, max_steps=50):

    current = {
        d: random.choice(v)
        for d, v in domains.items()
    }

    for _ in range(max_steps):

        conflicts = [
            d for d, v in current.items()
            if not is_repair_safe(v)
        ]

        if not conflicts:
            return current

        variable = random.choice(conflicts)

        valid_values = [
            v for v in domains[variable]
            if is_repair_safe(v)
        ]

        if valid_values:
            current[variable] = random.choice(valid_values)

    return current

# -----------------------------------------------------------
# Maintenance Scheduling
# -----------------------------------------------------------

maintenance_schedule = {
    "Motor Inspection": "9:00 AM",
    "Cooling System Check": "11:00 AM",
    "Belt Alignment": "1:00 PM",
    "Sensor Calibration": "3:00 PM"
}

# -----------------------------------------------------------
# SAT Logic Diagnosis
# -----------------------------------------------------------

def sat_fault_check(symptoms):

    overheating = "overheating" in symptoms
    vibration   = "vibration" in symptoms
    noise       = "noise" in symptoms

    # overheating AND vibration AND noise
    if overheating and vibration and noise:
        return "SAT Result: Motor Failure Suspected"

    if overheating and vibration:
        return "SAT Result: Mechanical Fault Detected"

    return "SAT Result: No Major Fault Detected"

# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("\n" + "=" * 55)
print("FAULT DIAGNOSIS IN INDUSTRIAL SYSTEM")
print("CO3 - CONSTRAINT SATISFACTION PROBLEM")
print("=" * 55)

print(f"\nMachine ID : {machine['machine_id']}")
print(f"Machine Type : {machine['type']}")

print(f"\nSymptoms : {machine['symptoms']}")

print(f"Restricted Repairs : {machine['restricted_repairs']}")

# Forward Checking
filtered_domains = forward_checking_faults(fault_variables)

# MRV Heuristic
print(f"\nMRV Selected Fault: {mrv_heuristic(filtered_domains)}")

# Degree Heuristic
print(f"Degree Heuristic Fault: {degree_heuristic(filtered_domains)}")

# Backtracking Solution
print("\nBacktracking Solution:\n")

bt_solution = backtracking_csp({}, filtered_domains)

print(bt_solution)

# Min-Conflicts Solution
print("\nMin-Conflicts Solution:\n")

mc_solution = min_conflicts_faults(filtered_domains)

print(mc_solution)

# Maintenance Scheduling
print("\nMaintenance Scheduling:\n")

for task, time in maintenance_schedule.items():

    print(f"  {task} -> {time}")

# SAT Check
print(f"\n{sat_fault_check(machine['symptoms'])}")

# Logs
print("\nDiagnosis Logs:\n")

for log in diagnosis_logs:

    print(f"  {log}")

print("\n" + "=" * 55)
print("FAULT DIAGNOSIS PROCESS COMPLETED")
print("=" * 55)