"""
BMI-Based Health Risk Classifier
A beginner-friendly bioengineering/computational-thinking project.

Note:
BMI is only a simple screening measure. It is not a medical diagnosis.
"""

def calculate_bmi(weight, height):
    """Calculate BMI from weight in kg and height in metres."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return a basic BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def get_health_message(category):
    """Return a simple suggestion based on the BMI category."""
    messages = {
        "Underweight": "Consider discussing your diet and overall health with a qualified professional.",
        "Normal weight": "Your BMI is in the normal range. Maintain a balanced diet and regular physical activity.",
        "Overweight": "Consider a balanced diet and regular physical activity. A healthcare professional can provide personalized advice.",
        "Obesity": "Consider speaking with a healthcare professional for personalized guidance on healthy weight management."
    }
    return messages[category]


def main():
    print("=" * 45)
    print("     BMI-BASED HEALTH RISK CLASSIFIER")
    print("=" * 45)

    try:
        age = int(input("Enter your age (years): "))
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (metres): "))

        if age <= 0 or weight <= 0 or height <= 0:
            print("\nPlease enter positive values only.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        message = get_health_message(category)

        print("\n----- RESULT -----")
        print(f"Age: {age} years")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print(f"Suggestion: {message}")
        print("------------------")

    except ValueError:
        print("\nInvalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()
