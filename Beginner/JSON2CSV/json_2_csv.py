import json
import csv


class Converter:
    """A JSON to CSV Converter"""

    def __init__(self):
        with open("original.json") as file:
            json_file = json.load(file)

        with open("pirate.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=json_file[0])

            writer.writeheader()

            for block in json_file:
                writer.writerow(block)


if __name__ == "__main__":
    converter = Converter()