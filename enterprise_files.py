import pandas as pd
import os
from faker import Faker
import random

fake = Faker()

# =====================================================
# OUTPUT FOLDER
# =====================================================
folder_path = r"C:/Users/subas/OneDrive/Desktop/test_folder"

os.makedirs(folder_path, exist_ok=True)

# =====================================================
# DEPARTMENTS
# =====================================================
departments = [
    "Engineering",
    "Finance",
    "HR",
    "Marketing",
    "Sales",
    "Operations",
    "Data Science"
]

# =====================================================
# FUNCTION TO GENERATE DATA
# =====================================================
def generate_employee_data(num_rows):

    records = []

    for i in range(num_rows):

        record = {
            "employee_id": random.randint(1000, 9999),

            "first_name": fake.first_name(),

            "last_name": fake.last_name(),

            "email": fake.email(),

            "department": random.choice(departments),

            "salary": round(random.uniform(40000, 150000), 2),

            "city": fake.city(),

            "country": fake.country(),

            "joining_date": fake.date_between(
                start_date='-5y',
                end_date='today'
            ),

            "is_active": random.choice([True, False])
        }

        records.append(record)

    return pd.DataFrame(records)

# =====================================================
# CREATE MULTIPLE FILES
# =====================================================
files = {
    "customer_jan.csv": 100,
    "customer_feb.csv": 120,
    "customer_march.csv": 150
}

for file_name, rows in files.items():

    df = generate_employee_data(rows)

    output_path = os.path.join(folder_path, file_name)

    df.to_csv(output_path, index=False)

    print(f"Created: {output_path} ({rows} rows)")

print("\nEnterprise test files created successfully!")