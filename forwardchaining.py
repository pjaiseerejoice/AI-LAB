# Step 1: Initial facts
facts = {
    "patient_registered",
    "has_severe_symptoms",
    "doctor_available"
}

# Step 2: Define rules
rules = [
    ({"patient_registered"}, "verified_patient"),
    ({"has_severe_symptoms"}, "priority_required"),
    ({"verified_patient", "priority_required"},
     "priority_eligible"),
    ({"priority_eligible", "doctor_available"},
     "priority_appointment")
]

# Step 3: Forward Chaining
print("Initial Facts:")
print(facts)

print("\nNewly Inferred Facts:")

while True:
    new_fact_added = False

    for conditions, conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            print("Inferred:", conclusion)
            new_fact_added = True

    if not new_fact_added:
        break

# Step 4: Display final facts
print("\nFinal Set of Facts:")
print(facts)

# Step 5: Display result
if "priority_appointment" in facts:
    print("\nResult: Patient is eligible for priority consultation.")
else:
    print("\nResult: Patient is not eligible for priority consultation.")

