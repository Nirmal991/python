import csv
import json
input_csv_path = 'D:/Program Files/Python/Day08/assignment/as_01/students.csv'
output_json_path = 'D:/Program Files/Python/Day08/assignment/as_01/summary.json'

def process_student_records(input_csv_path, output_json_path):
    total_students = 0
    total_score = 0
    average_score = 0
    top_scorer = None
    course_counts = {}
    with open(input_csv_path, 'r', encoding='utf-8') as f1:
        reader = csv.DictReader(f1)
        for row in reader:

            name = row['name']
            course = row['course']
            score = float(row['score'])

            total_students += 1
            total_score += score

            if top_scorer is None or score > top_scorer["score"]:
                top_scorer = {
                    "name": name,
                    "score": score
                }

            course_counts[course] = course_counts.get(course,0) + 1

        average_score = total_score / total_students

        summary = {
            "total_students": total_students,
            "average_score": average_score,
            "top_score": top_scorer,
            "course_count": course_counts
        }

        with open(output_json_path, 'w', encoding='utf-8') as f1:
            json.dump(summary, f1, indent=4)
                 
        # print(total_students)
            

def main():
    process_student_records(input_csv_path,output_json_path)

main()
