from typing import List, Dict
from utils.file_reader import read_csv_file

def parse_files(file_paths: List[str]) -> List[Dict]:
    employees = []
    for file_path in file_paths:
        employees.extend(read_csv_file(file_path))
    return employees