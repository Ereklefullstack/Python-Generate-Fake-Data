from faker import Faker
import random
import pandas as pd

# Create Faker instance
fake = Faker()

# Number of records
num_records = 50000

# List to store data
data = []

# Generate fake data
for _ in range(num_records):
    record = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "job": fake.job(),
        "company": fake.company()
    }
    data.append(record)

# Create some duplicate records
num_duplicates = int(num_records * 0.1)  # 10% of records are duplicates
for _ in range(num_duplicates):
    data.append(random.choice(data))

# Create DataFrame using pandas
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("fake_data.csv", index=False)

print(f"{len(df)} Records were saved in 'fake_data.csv' file.")
