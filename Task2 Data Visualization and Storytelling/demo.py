import pandas as pd
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()

# Function to generate random data
def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        city = fake.city()
        data.append([first_name, last_name, email, city])
    return data

# Specify the total number of records
total_records = 422700
batch_size = 5000  # Adjust batch size to prevent overload

# Create an empty list to store the batches
all_data = []

# Generate data in batches and append it to the list
for i in range(0, total_records, batch_size):
    batch_data = generate_random_data(batch_size)
    all_data.extend(batch_data)
    print(f"Generated {i + batch_size} records")  # Progress tracking

# Convert the data to a DataFrame
df = pd.DataFrame(all_data, columns=['FirstName', 'LastName', 'Email', 'City'])

# Save the DataFrame to a CSV file
df.to_csv('customers_data.csv', index=False)
print("Data generation complete. File saved as 'customers_data.csv'")