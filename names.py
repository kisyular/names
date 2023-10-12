import random
import csv
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()


# Function to generate a random ID
def generate_id():
    letters = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=3)).upper()
    numbers = "".join(random.choices("0123456789", k=5))
    return f"{letters}{numbers}"


# Function to generate a random date in the range 2022-01-01 to 2023-12-31 (excluding weekends)
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)

    while True:
        random_date = start_date + timedelta(
            days=random.randint(0, (end_date - start_date).days)
        )
        # Check if the generated date is a weekday (Monday to Friday)
        if random_date.weekday() < 5:
            return random_date.strftime("%Y-%m-%d")


# Data generation
data = []
students_per_date = {}  # Dictionary to track students per date

for i in range(10000):
    id = generate_id()
    surname = fake.last_name()
    first_name = fake.first_name()
    name = f"{surname} {first_name}"
    date_of_admission = generate_random_date()

    # Update students per date
    students_per_date[date_of_admission] = (
        students_per_date.get(date_of_admission, 0) + 1
    )

    # Probability distribution for county
    county_choices = ["Nairobi", "Kiambu", "Kajiado", "Nakuru", "Makueni"]
    county_probabilities = [0.446, 0.245, 0.058, 0.1034, 0.1476]

    # Generate county based on the defined probabilities
    county = random.choices(county_choices, weights=county_probabilities, k=1)[0]

    # Probability distribution for location
    location_choices = ["Urban", "Sub-Urban", "Rural"]
    location_probabilities = [0.6545, 0.2235, 0.1220]

    # Generate location based on the defined probabilities
    location = random.choices(location_choices, weights=location_probabilities, k=1)[0]

    # Probability distribution for gender
    gender_choices = ["Male", "Female"]
    gender_probabilities = [
        0.3951,
        0.6049,
    ]  # Corresponding to 39% Male and 60.49% Female

    # Generate gender based on the defined probabilities
    gender = random.choices(gender_choices, weights=gender_probabilities, k=1)[0]
    grade = random.randint(1, 8)
    fees = grade * 1000
    fees_paid = random.randint(0, fees)
    fees_arrears = fees - fees_paid

    data.append(
        [
            id,
            name,
            date_of_admission,
            gender,
            grade,
            county,
            location,
            fees,
            fees_paid,
            fees_arrears,
            students_per_date[date_of_admission],
        ]
    )

# Write to CSV
with open("student_records.csv", "w", newline="") as csvfile:
    fieldnames = [
        "Id",
        "Name",
        "Date of Admission",
        "Gender",
        "Grade",
        "County",
        "Location",
        "Fees",
        "Fees Paid",
        "Fees Arrears",
        "Students per Date",
    ]
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(data)

print("Data generated and saved to student_records.csv.")
