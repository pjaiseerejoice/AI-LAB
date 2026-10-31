# Step 1: Define symptom patterns and guidance
rules = {
    "fever": [
        "fever", "high temperature", "body heat"
    ],
    "cold": [
        "cold", "sneezing", "runny nose"
    ],
    "headache": [
        "headache", "head pain"
    ],
    "stomach_problem": [
        "stomach pain", "stomach ache", "vomiting"
    ]
}

# Step 2: Define guidance for each pattern
guidance = {
    "fever": "Monitor temperature and consult a doctor if symptoms persist.",
    "cold": "Take adequate rest and seek medical advice if symptoms worsen.",
    "headache": "Rest and consult a healthcare professional if severe or persistent.",
    "stomach_problem": "Seek medical advice for proper assessment."
}

# Step 3: Get patient symptoms
symptoms = input("Enter your symptoms: ").lower()

# Step 4: Pattern matching
matched = False

print("\nSymptom Assessment:")

for pattern, keywords in rules.items():
    for keyword in keywords:
        if keyword in symptoms:
            print("Identified Pattern:", pattern)
            print("Guidance:", guidance[pattern])
            matched = True
            break

# Step 5: Display result
if not matched:
    print("No predefined symptom pattern found.")
    print("Please consult a healthcare professional for assessment.")

print("\nAssessment Completed.")




