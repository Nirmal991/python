import re
class Patient:
    _patient_counter = 0

    @staticmethod
    def validate_dob_format(dob_str):

        pattern = re.match(
            pattern=r"^\d{4}-\d{2}-\d{2}$", string=dob_str
        )
        if pattern is None:
            return False
        return True

    def __init__(self, name: str, dob: str):
        if not Patient.validate_dob_format(dob):
            raise ValueError(
                f"Invalid date of birth format"
            )
        Patient._patient_counter += 1
        self.patient_id = f"PAT-{1000 + Patient._patient_counter}"

        self.name = name
        self.dob = dob

    @classmethod
    def get_total_patients(cls):
        return cls._patient_counter

# 1. Valid Registration
p1 = Patient("Arham Khan", "1999-05-15")
print(p1.patient_id)  # Output: PAT-1001

# 2. Invalid DOB registration (throws ValueError)
try:
    p2 = Patient("Lisa", "2026-08-24")
except ValueError as e:
    print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

print(Patient.get_total_patients())  # Output: 1
    