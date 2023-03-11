from sortings import shaker_sort_algorithm, quicksort, merge_sort
from generator import generate_work_phone, generate_full_name, generate_email, generate_org_name
import os
import csv

def generate_csv_table(rows, filename):
    """! Generates a CSV table with random person data and writes it to a file.
    @param rows: The number of rows to generate.
    @param filename: The name of the file to write the CSV table to.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["full_name", "email", "work_phone", "org_name"])
        for i in range(rows):
            full_name = generate_full_name()
            email = generate_email(full_name)
            work_phone = generate_work_phone()
            org_name = generate_org_name()
            writer.writerow([full_name, email, work_phone, org_name])

def shaker_sort_csv(file_name):
    """! Sorts a CSV table using the shaker sort algorithm and writes the sorted data to a file.
    @param file_name: The name of the CSV file to sort.
    """
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            full_name, email, work_phone, org_name = row
            data.append(Person(full_name, email, work_phone, org_name))
    sorted_data = shaker_sort_algorithm(data)
    os.makedirs("shaker_sorted_tables", exist_ok=True)
    with open("shaker_sorted_" + file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["full_name", "email", "work_phone", "org_name"])
        for person in sorted_data:
            writer.writerow([person.full_name, person.email, person.work_phone, person.org_name])

def quick_sort_csv(file_name):
    """! Sorts a CSV table using the quicksort algorithm and writes the sorted data to a file.
    @param file_name: The name of the CSV file to sort.
    """
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            full_name, email, work_phone, org_name = row
            data.append(Person(full_name, email, work_phone, org_name))
    sorted_data = quicksort(data, 0, len(data) - 1)
    os.makedirs("quick_sorted_tables", exist_ok=True)
    with open("quick_sorted_" + file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["full_name", "email", "work_phone", "org_name"])
        for person in sorted_data:
            writer.writerow([person.full_name, person.email, person.work_phone, person.org_name])

def merge_sort_csv(file_name):
    """! Sorts a CSV table using the merge sort algorithm and writes the sorted data to a file.
    @param file_name: The name of the CSV file to sort.
    """
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            full_name, email, work_phone, org_name = row
            data.append(Person(full_name, email, work_phone, org_name))
    sorted_data = merge_sort(data)
    os.makedirs("merge_sorted_tables", exist_ok=True)
    with open("merge_sorted_" + file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["full_name", "email", "work_phone", "org_name"])
        for person in sorted_data:
            writer.writerow([person.full_name, person.email, person.work_phone, person.org_name])

