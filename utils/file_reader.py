from typing import List, Dict
import re


def read_csv_file(file_path: str) -> List[Dict]:
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(',')]
    rate_keys = {'hourly_rate', 'rate', 'salary'}
    rate_header = None

    for header in headers:
        if header in rate_keys:
            rate_header = header
            break

    if not rate_header:
        raise ValueError("No valid rate column found in CSV")

    employees = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        if len(values) != len(headers):
            continue

        employee = dict(zip(headers, values))
        employee['hourly_rate'] = float(employee[rate_header])
        employee['hours_worked'] = float(employee['hours_worked'])
        employee['id'] = int(employee['id'])
        employees.append(employee)

    return employees