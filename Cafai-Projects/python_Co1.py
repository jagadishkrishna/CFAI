# cook your dish here
# ===========================================================
# CO1 - Intelligent Agent Model
# Fault Diagnosis in Industrial Systems
# ===========================================================

from dataclasses import dataclass
from typing import List, Dict

# -----------------------------------------------------------
# Machine Profile
# -----------------------------------------------------------

@dataclass
class MachineProfile:
    machine_name: str
    machine_id: int
    department: str
    symptoms: List[str]
    maintenance_history: str


# -----------------------------------------------------------
# Fault Diagnosis Agent
# -----------------------------------------------------------

class FaultDiagnosisAgent:

    def __init__(self):

        # Knowledge Base
        # Fault -> Symptoms

        self.knowledge_base: Dict[str, List[str]] = {

            "Motor Failure": [
                "overheating",
                "burning_smell",
                "vibration",
                "power_loss",
                "noise"
            ],

            "Bearing Damage": [
                "vibration",
                "grinding_noise",
                "temperature_rise",
                "lubrication_leak",
                "shaft_misalignment"
            ],

            "Hydraulic Leakage": [
                "oil_leak",
                "pressure_drop",
                "slow_operation",
                "fluid_loss",
                "overheating"
            ],

            "Sensor Failure": [
                "incorrect_reading",
                "signal_loss",
                "system_shutdown",
                "data_fluctuation",
                "warning_alarm"
            ],

            "Cooling System Failure": [
                "high_temperature",
                "coolant_leak",
                "fan_failure",
                "overheating",
                "reduced_efficiency"
            ]
        }

    # -------------------------------------------------------
    # Diagnosis Function
    # -------------------------------------------------------

    def diagnose(self, machine: MachineProfile):

        possible_faults = []

        print("\n================================================")
        print("FAULT DIAGNOSIS REPORT")
        print("================================================")

        print(f"Machine Name      : {machine.machine_name}")
        print(f"Machine ID        : {machine.machine_id}")
        print(f"Department        : {machine.department}")
        print(f"Maintenance Info  : {machine.maintenance_history}")

        print("\nSymptoms Detected:")
        for symptom in machine.symptoms:
            print(f"- {symptom}")

        print("\nScanning Knowledge Base...\n")

        for fault, symptoms in self.knowledge_base.items():

            match_count = 0

            print(f"Checking Fault: {fault}")

            for symptom in symptoms:

                if symptom in machine.symptoms:

                    match_count += 1
                    print(f"  Matched Symptom: {symptom}")

            match_percentage = (match_count / len(symptoms)) * 100

            print(f"  Match Score: {match_count}/{len(symptoms)} "
                  f"({match_percentage:.1f}%)\n")

            # Minimum 2 matching symptoms
            if match_count >= 2:
                possible_faults.append(fault)

        return possible_faults


# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------

print("================================================")
print("FAULT DIAGNOSIS IN INDUSTRIAL SYSTEMS")
print("CO1 - INTELLIGENT AGENT MODEL")
print("================================================")

machine1 = MachineProfile(
    machine_name="Hydraulic Press Machine",
    machine_id=1001,
    department="Manufacturing Unit",
    symptoms=[
        "overheating",
        "oil_leak",
        "pressure_drop",
        "slow_operation"
    ],
    maintenance_history="Serviced 2 months ago"
)

agent = FaultDiagnosisAgent()

result = agent.diagnose(machine1)

print("================================================")
print("POSSIBLE FAULTS DETECTED")
print("================================================")

for fault in result:
    print("->", fault)

print("================================================")