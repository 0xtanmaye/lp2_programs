# ============================================================
#   MEDICAL EXPERT SYSTEM - Hospital Doctor Recommendation
#   Expert System Type: Rule-Based (IF-THEN Logic)
#   Input : Symptoms entered by user
#   Output: Recommended type of doctor to consult
# ============================================================

# ── KNOWLEDGE BASE ──────────────────────────────────────────
# Each entry maps a DOCTOR TYPE to:
#   - keywords : symptom words that trigger this specialist
#   - advice   : brief guidance shown to the user
# ────────────────────────────────────────────────────────────
KNOWLEDGE_BASE = {
    "Cardiologist (Heart Specialist)": {
        "keywords": [
            "chest pain", "chest tightness", "palpitations", "irregular heartbeat",
            "shortness of breath", "heart racing", "high blood pressure",
            "swollen legs", "dizziness", "fainting", "heart attack"
        ],
        "advice": "Avoid strenuous activity. If chest pain is severe, call emergency services immediately."
    },

    "Neurologist (Brain & Nerve Specialist)": {
        "keywords": [
            "headache", "migraine", "seizure", "memory loss", "numbness",
            "tingling", "weakness", "tremor", "confusion", "stroke",
            "blurred vision", "loss of balance", "paralysis", "epilepsy"
        ],
        "advice": "Keep a symptom diary (when it occurs, duration, triggers). Avoid stress and get adequate sleep."
    },

    "Gastroenterologist (Digestive System Specialist)": {
        "keywords": [
            "stomach pain", "abdominal pain", "nausea", "vomiting", "diarrhea",
            "constipation", "bloating", "acid reflux", "heartburn", "indigestion",
            "blood in stool", "jaundice", "loss of appetite", "ulcer"
        ],
        "advice": "Eat smaller meals, avoid spicy food, and stay hydrated. Keep a food diary to identify triggers."
    },

    "Dermatologist (Skin Specialist)": {
        "keywords": [
            "rash", "itching", "acne", "eczema", "psoriasis", "skin redness",
            "hives", "dry skin", "skin irritation", "blisters", "hair loss",
            "nail problems", "mole", "warts", "skin infection"
        ],
        "advice": "Avoid scratching. Use mild soap and moisturizer. Protect skin from sun exposure."
    },

    "Orthopedician (Bone & Joint Specialist)": {
        "keywords": [
            "joint pain", "knee pain", "back pain", "bone pain", "fracture",
            "sprain", "arthritis", "swollen joint", "stiffness", "neck pain",
            "shoulder pain", "hip pain", "muscle pain", "ligament", "slip disc"
        ],
        "advice": "Rest the affected area. Apply ice for swelling. Avoid lifting heavy objects."
    },

    "Pulmonologist (Lung & Respiratory Specialist)": {
        "keywords": [
            "cough", "chronic cough", "wheezing", "breathlessness", "asthma",
            "tuberculosis", "pneumonia", "chest congestion", "snoring",
            "sleep apnea", "blood in cough", "lung infection", "bronchitis"
        ],
        "advice": "Avoid smoke and dust. Use prescribed inhalers if available. Breathe in steam for congestion."
    },

    "Ophthalmologist (Eye Specialist)": {
        "keywords": [
            "eye pain", "red eyes", "itchy eyes", "blurred vision", "double vision",
            "watery eyes", "eye discharge", "light sensitivity", "floaters",
            "night blindness", "swollen eyelid", "cataracts", "glaucoma"
        ],
        "advice": "Avoid rubbing your eyes. Reduce screen time. Wear sunglasses outdoors."
    },

    "ENT Specialist (Ear, Nose & Throat)": {
        "keywords": [
            "ear pain", "hearing loss", "ringing in ears", "sore throat",
            "difficulty swallowing", "hoarse voice", "nasal congestion",
            "runny nose", "sinus", "nosebleed", "tonsil", "sneezing", "ear infection"
        ],
        "advice": "Stay hydrated. Use a humidifier for nasal issues. Avoid loud noise exposure for ear problems."
    },

    "Endocrinologist (Hormones & Diabetes Specialist)": {
        "keywords": [
            "diabetes", "excessive thirst", "frequent urination", "weight gain",
            "weight loss", "fatigue", "thyroid", "hair thinning", "cold intolerance",
            "heat intolerance", "irregular periods", "mood swings", "hormonal imbalance"
        ],
        "advice": "Monitor blood sugar regularly. Follow a balanced diet and exercise routine."
    },

    "Psychiatrist / Psychologist (Mental Health Specialist)": {
        "keywords": [
            "depression", "anxiety", "stress", "panic attack", "insomnia",
            "mood swings", "hallucinations", "suicidal thoughts", "phobia",
            "obsessive thoughts", "eating disorder", "trauma", "bipolar", "addiction"
        ],
        "advice": "Talk to someone you trust. Avoid isolation. Meditation and routine sleep can help significantly."
    },

    "General Physician (Family Doctor)": {
        "keywords": [
            "fever", "cold", "flu", "body ache", "weakness", "tiredness",
            "chills", "sweating", "loss of taste", "loss of smell", "general check up",
            "vaccination", "mild cough", "sore muscles"
        ],
        "advice": "Rest, drink plenty of fluids, and take over-the-counter medication if needed."
    }
}


# ── INFERENCE ENGINE ─────────────────────────────────────────
# Matches user symptoms against the knowledge base keywords
# Returns a list of (doctor, matched_symptoms, advice) tuples
# ─────────────────────────────────────────────────────────────
def diagnose(user_input):
    """
    Takes a string of symptoms from the user.
    Returns a sorted list of matching doctors and matched keywords.
    """
    # Lowercase the input so matching is case-insensitive
    user_input = user_input.lower()

    results = []  # Will store (doctor_name, matched_list, advice)

    for doctor, data in KNOWLEDGE_BASE.items():
        matched = []  # Track which keywords matched

        for keyword in data["keywords"]:
            # Check if the keyword appears anywhere in the user's input
            if keyword in user_input:
                matched.append(keyword)

        # If at least one keyword matched, add this doctor to results
        if matched:
            results.append((doctor, matched, data["advice"]))

    # Sort by most matched symptoms first (most likely doctor at the top)
    results.sort(key=lambda x: len(x[1]), reverse=True)

    return results


# ── DISPLAY RESULTS ──────────────────────────────────────────
def show_results(results):
    """Prints the diagnosis results in a readable format."""

    if not results:
        print("\n  [!] No matching specialist found for the given symptoms.")
        print("      Please consult a General Physician for an initial evaluation.\n")
        return

    print("\n" + "=" * 55)
    print("       RECOMMENDED DOCTOR(S) BASED ON YOUR SYMPTOMS")
    print("=" * 55)

    for rank, (doctor, matched, advice) in enumerate(results, start=1):
        print(f"\n  #{rank}  {doctor}")
        print(f"      Matched Symptoms : {', '.join(matched)}")
        print(f"      Advice           : {advice}")

    print("\n" + "=" * 55)
    print("  NOTE: This is an AI suggestion, NOT a medical diagnosis.")
    print("        Always consult a qualified medical professional.")
    print("=" * 55 + "\n")


# ── MAIN PROGRAM ─────────────────────────────────────────────
def main():
    """Main loop — keeps running until the user types 'exit'."""

    print("\n" + "=" * 55)
    print("     MEDICAL EXPERT SYSTEM — Doctor Recommendation")
    print("=" * 55)
    print("  Enter your symptoms separated by commas or spaces.")
    print("  Type 'help' to see all recognizable symptoms.")
    print("  Type 'exit' to quit.\n")

    while True:
        # Get input from the user
        user_input = input("  Enter symptoms: ").strip()

        # Exit condition
        if user_input.lower() == "exit":
            print("\n  Thank you for using the Medical Expert System. Stay healthy!\n")
            break

        # Show all known symptoms if user types 'help'
        elif user_input.lower() == "help":
            print("\n  Recognized Symptoms:\n")
            all_symptoms = []
            for data in KNOWLEDGE_BASE.values():
                all_symptoms.extend(data["keywords"])
            # Print all symptoms as a simple comma-separated list
            print("  " + ", ".join(all_symptoms) + "\n")

        # Empty input check
        elif user_input == "":
            print("  [!] Please enter at least one symptom.\n")

        # Run the diagnosis
        else:
            results = diagnose(user_input)
            show_results(results)


# ── ENTRY POINT ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
