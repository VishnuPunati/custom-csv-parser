import random
import string

def generate_csv(file_path, rows=10000, cols=5):
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(rows):
            row = []
            for _ in range(cols):
                value = ''.join(random.choices(string.ascii_letters, k=10))
                if random.random() < 0.2:
                    value = f'"{value}, with comma"'
                row.append(value)
            f.write(",".join(row) + "\n")

if __name__ == "__main__":
    generate_csv("test_data.csv")
