import csv

csv_file_path = 'problem_sheet.csv'
output_file_path = 'output.csv'

# Read the first 20 lines (skiprows=20)
with open(csv_file_path, 'r') as file:
    for _ in range(20):
        next(file)

    # Now, read the rest of the file
    reader = csv.DictReader(file)
    
    # Check if 'index2' is present in the header
    if 'index2' not in reader.fieldnames:
        print("Column 'index2' not found. Check the case sensitivity and column name in your CSV file.")
        exit()

    # Store the rows in a list
    rows = list(reader)

# Create a list to store the rows for the final CSV
final_data_rows = []

# Perform operations on each string in the "index2" column
for row in rows:
    # A. Reverse the string
    reversed_string = row['index2'][::-1]

    # B. Complement the string
    complemented_string = ''.join(['A' if base == 'T' else 'T' if base == 'A' else 'G' if base == 'C' else 'C' for base in reversed_string])

    # Add the modified values to the final data list
    final_data_rows.append({'Original_index2': row['index2'], 'Reverse_complemented_index2': complemented_string})

# Write the modified rows to the final CSV file
fieldnames = ['Original_index2', 'Reverse_complemented_index2']

with open(output_file_path, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the modified rows
    writer.writerows(final_data_rows)

