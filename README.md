# BMI-Based Health Risk Classifier

## 1. Project Overview

The **BMI-Based Health Risk Classifier** is a simple beginner-friendly Python program related to **bioengineering and health data analysis**.

The program accepts a person's:

- Age
- Weight in kilograms
- Height in metres

It then:

1. Calculates the person's Body Mass Index (BMI).
2. Classifies the BMI into a basic category.
3. Displays a simple health suggestion.

This project demonstrates basic **computational thinking**, including input, processing, decision-making, and output.

---

## 2. Problem Statement

A person's body measurements can be used to calculate simple health-related indicators.

The problem is to create a program that takes a person's height and weight, calculates their BMI, and uses decision-making rules to place the result into a basic BMI category.

The program should provide the result in an easy-to-understand format.

---

## 3. Technologies Used

- **Python 3**
- No external libraries are required.

---

## 4. Requirements

You need:

- Python 3.8 or later
- A text editor or IDE such as:
  - VS Code
  - PyCharm
  - IDLE
  - Any Python-supported editor

---

## 5. Setup Instructions

### Step 1: Install Python

Download and install Python 3 from the official Python website if it is not already installed.

During installation on Windows, make sure to select **"Add Python to PATH"**.

### Step 2: Save the program

Save the Python code as:

```text
bmi_health_classifier.py
```

### Step 3: Open a terminal

Navigate to the folder containing the Python file.

### Step 4: Run the program

Use:

```bash
python bmi_health_classifier.py
```

On some systems, you may need:

```bash
python3 bmi_health_classifier.py
```

---

## 6. Inputs

The program asks for three inputs:

| Input | Unit | Example |
|---|---|---:|
| Age | years | 19 |
| Weight | kg | 60 |
| Height | metres | 1.65 |

The program checks that the values are positive numbers.

---

## 7. BMI Calculation

The program uses the formula:

```text
BMI = weight / height²
```

where:

- Weight is measured in kilograms.
- Height is measured in metres.

For example:

```text
Weight = 60 kg
Height = 1.65 m

BMI = 60 / (1.65 × 1.65)
BMI ≈ 22.04
```

The program would classify this result as **Normal weight** using the basic categories built into the program.

---

## 8. BMI Categories Used

The program uses these simple adult BMI ranges:

| BMI | Category |
|---:|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| 30.0 or above | Obesity |

---

## 9. Outputs

The program displays:

- Age
- Calculated BMI
- BMI category
- A simple health suggestion

---

## 10. Example Usage

### Example Input

```text
=============================================
     BMI-BASED HEALTH RISK CLASSIFIER
=============================================
Enter your age (years): 19
Enter your weight (kg): 60
Enter your height (metres): 1.65
```

### Example Output

```text
----- RESULT -----
Age: 19 years
BMI: 22.04
Category: Normal weight
Suggestion: Your BMI is in the normal range. Maintain a balanced diet and regular physical activity.
------------------
```

---

## 11. How the Program Works

The program follows four main steps:

### Step 1 — Input

The user enters their age, weight, and height.

### Step 2 — Processing

The program calculates BMI using:

```text
BMI = weight / height²
```

### Step 3 — Decision Making

The program uses `if`, `elif`, and `else` statements to determine the BMI category.

### Step 4 — Output

The calculated BMI, category, and suggestion are displayed to the user.

### Simple Flow

```text
Start
  ↓
Enter age, weight and height
  ↓
Calculate BMI
  ↓
Check BMI range
  ↓
Assign category
  ↓
Display result and suggestion
  ↓
End
```

---

## 12. Computational Thinking Concepts

This project demonstrates:

### Decomposition
The problem is divided into smaller tasks:

- Get user information
- Calculate BMI
- Classify BMI
- Display a suggestion

### Pattern Recognition
BMI values can be grouped into different ranges.

### Abstraction
Only useful information such as height and weight is used for the BMI calculation.

### Algorithmic Thinking
The program follows a fixed sequence of instructions to produce the result.

---

## 13. Limitations

This program is intended for **educational purposes only**.

Important limitations include:

1. BMI is a screening measure, not a medical diagnosis.
2. BMI does not directly measure body fat.
3. It does not account for muscle mass, bone density, or body composition.
4. The simple categories used here are not suitable for every person or population.
5. BMI interpretation can differ for children, teenagers, pregnant people, athletes, and some ethnic/population groups.
6. Age is collected for demonstration but is not used to modify the BMI category.
7. The program should not be used to make medical decisions.

For real health assessment, a qualified healthcare professional should be consulted.

---

## 14. Possible Future Improvements

The project could be expanded by adding:

- A graphical user interface (GUI)
- BMI history and data storage
- Charts showing BMI changes over time
- More detailed health-related inputs
- Age- and sex-specific reference data where appropriate
- CSV/database storage
- Personalized but medically reviewed recommendations

---

## 15. Project Structure

```text
bmi_health_risk_classifier/
│
├── bmi_health_classifier.py
└── README.md
```

---

## 16. License

This project is created for educational and academic purposes.
