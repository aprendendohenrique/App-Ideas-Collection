import json
import csv
import ast
import io
from csv import DictReader
from json import JSONDecodeError


class Converter:
    """A JSON to CSV Converter"""


    @classmethod
    def json_to_csv(cls, file_path, csv_name):
        with open(file_path) as file:
            json_file = json.load(file)

        with open(csv_name, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=json_file[0])

            writer.writeheader()

            for block in json_file:
                writer.writerow(block)


    @classmethod
    def csv_to_json(cls, file_path, json_name):
        with open(file_path) as file:
            csv_file = csv.DictReader(file)
            content = Converter._format_csv_file(csv_file)

        with open(json_name, "w") as json_file:
            json.dump(content, json_file, indent=4)


    @classmethod
    def _format_csv_file(cls, csv_file):
        content = []

        for line in csv_file:
            for key, value in line.items():
                if isinstance(value, str):
                    try:
                        line[key] = int(value)
                    except ValueError:
                        try:
                            line[key] = float(value)
                        except ValueError:
                            pass

                    if value == "True" or value == "true":
                        line[key] = True
                    elif value == "False" or value == "false":
                        line[key] = False

                    elif value.startswith(("[", "{")):
                        line[key] = ast.literal_eval(value)

            content.append(line)

        return content


    @classmethod
    def text_json_to_csv(cls, text):
        if text.startswith("["):
            try:
                data = json.loads(text)
            except JSONDecodeError:
                return None
            else:
                headers = data[0].keys()

                output = io.StringIO()

                writer = csv.DictWriter(output, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)

                return output.getvalue()
        return None


    @classmethod
    def text_csv_to_json(cls, text):
        data = text.split("\n")
        if len(data) > 2 and not data[0].startswith("["):
            data = csv.DictReader(data)
            content = Converter._format_csv_file(data)

            output = io.StringIO()

            json.dump(content, output, indent=4)

            return output.getvalue()
        return None


if __name__ == "__main__":
    Converter.json_to_csv("original.json", "pirate.csv")
    Converter.csv_to_json("pirate.csv", "pirate.json")
