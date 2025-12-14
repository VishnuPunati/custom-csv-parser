class CustomCsvReader:
    """
    Custom CSV Reader implemented from scratch.
    Acts as an iterator and streams rows one by one.
    """

    def __init__(self, file_path, delimiter=","):
        self.file = open(file_path, "r", encoding="utf-8")
        self.delimiter = delimiter

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        field = []
        in_quotes = False

        while True:
            char = self.file.read(1)

            if char == "":
                if field or row:
                    row.append("".join(field))
                    return row
                self.file.close()
                raise StopIteration

            if char == '"':
                next_char = self.file.read(1)
                if in_quotes and next_char == '"':
                    field.append('"')  # escaped quote
                else:
                    in_quotes = not in_quotes
                    if next_char:
                        self.file.seek(self.file.tell() - 1)

            elif char == self.delimiter and not in_quotes:
                row.append("".join(field))
                field = []

            elif char == "\n" and not in_quotes:
                row.append("".join(field))
                return row

            else:
                field.append(char)


class CustomCsvWriter:
    """
    Custom CSV Writer implemented from scratch.
    """

    def __init__(self, file_path, delimiter=","):
        self.file = open(file_path, "w", encoding="utf-8", newline="")
        self.delimiter = delimiter

    def write_row(self, row):
        formatted_fields = []
        for field in row:
            field = str(field)
            if any(ch in field for ch in [self.delimiter, '"', "\n"]):
                field = field.replace('"', '""')
                field = f'"{field}"'
            formatted_fields.append(field)

        self.file.write(self.delimiter.join(formatted_fields) + "\n")

    def write_all(self, rows):
        for row in rows:
            self.write_row(row)

    def close(self):
        self.file.close()
