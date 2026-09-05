import re
import csv
import json
input_log_path = 'D:/Program Files/Python/Day08/assignment/as_02/server_access.log'
output_csv_path= 'D:/Program Files/Python/Day08/assignment/as_02/access_records.csv'
output_json_path= 'D:/Program Files/Python/Day08/assignment/as_02/access_records.json'

def convert_log_file(input_log_path, output_csv_path, output_json_path):
    pattern = r"^(?P<TIMESTAMP>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (?P<USER_ID>[A-Z0-9]+) \| (?P<ENDPOINT>/[a-zA-Z0-9_/.-]+) \| (?P<STATUS_CODE>\d{3})$"
    match_list = []

    with open(input_log_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(pattern, line.strip())
            if match:
                data = match.groupdict()

                record = {
                    "timestamp": data['TIMESTAMP'],
                    "user_id": data["USER_ID"],
                    "endpoint": data["ENDPOINT"],
                    "status_code": int(data["STATUS_CODE"])
                }

                match_list.append(record)

    fieldnames = ["timestamp", "user_id", "endpoint", "status_code"]

    with open(output_csv_path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(match_list)

    with open(output_json_path, 'w', encoding='utf-8') as file:
        json.dump(match_list, file,indent=4)




def main():
    convert_log_file(input_log_path, output_csv_path, output_json_path)

main()