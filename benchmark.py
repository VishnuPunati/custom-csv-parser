import csv
import timeit
from custom_csv import CustomCsvReader, CustomCsvWriter

TEST_FILE = "test_data.csv"
OUTPUT_FILE = "output.csv"

def custom_read():
    reader = CustomCsvReader(TEST_FILE)
    for _ in reader:
        pass

def standard_read():
    with open(TEST_FILE, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for _ in reader:
            pass

def custom_write():
    writer = CustomCsvWriter(OUTPUT_FILE)
    writer.write_all([["a", "b", "c", "d", "e"]] * 10000)
    writer.close()

def standard_write():
    with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([["a", "b", "c", "d", "e"]] * 10000)

if __name__ == "__main__":
    print("Custom Read:", timeit.timeit(custom_read, number=3))
    print("CSV Read:", timeit.timeit(standard_read, number=3))
    print("Custom Write:", timeit.timeit(custom_write, number=3))
    print("CSV Write:", timeit.timeit(standard_write, number=3))
