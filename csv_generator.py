'''

In the bleak midwinter
Frosty wind made moan
Earth stood hard as iron
Water like a stone
Snow had fallen
Snow on snow on snow
In the bleak midwinter
Long, long ago

'''

import csv
import random
from datetime import datetime, timedelta


def generate_csv(filename, num_rows):
    # Header row
    header = ['Id', 'Name', 'Email', 'Phone', 'Address', 'Mode', 'Date']

    # Generate random data
    data = [header]
    unique_numbers = generate_unique_numbers(50, 1, 100)
    count = 0
    phone_number = generate_unique_numbers(50, 7656895636, 9999999999)

    for _ in range(num_rows):
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        id = unique_numbers[count]
        date = generate_random_date()
        email = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
        email += '@gmail.com'
        phone = phone_number[count]
        address = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=8))
        mode = 'Online'
        row = [id, name, email, phone, address, mode, date]
        data.append(row)
        count += 1

    # Write data to CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print(f"CSV file '{filename}' has been generated successfully.")


def generate_random_date():
    start_date = datetime(2022, 5, 8)
    end_date = datetime.now()
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')


def generate_unique_numbers(num_numbers, min_value, max_value):
    if max_value - min_value < num_numbers:
        raise ValueError("Cannot generate unique numbers. Range is smaller than the number of requested numbers.")

    numbers = set()

    while len(numbers) < num_numbers:
        random_number = random.randint(min_value, max_value)
        numbers.add(random_number)

    return list(numbers)


# Usage example
filename = 'online_customers.csv'
num_rows = 50  # Number of random data rows to generate
generate_csv(filename, num_rows)
