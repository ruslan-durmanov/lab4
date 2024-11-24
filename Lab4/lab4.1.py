# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    output_data = {}
    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file)
        data_to_transfer = []
        for row in reader:
            data_to_transfer.append(row)
    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(data_to_transfer, output_file, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
