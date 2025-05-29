import os
import pytest
from utils.file_reader import read_csv_file


@pytest.fixture
def sample_csv(tmp_path):
    content = """id,email,name,department,hours_worked,rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40"""

    file_path = tmp_path / "test.csv"
    file_path.write_text(content)
    return file_path


def test_read_csv_file(sample_csv):
    employees = read_csv_file(sample_csv)
    assert len(employees) == 2
    assert employees[0]['name'] == 'Alice Johnson'
    assert employees[0]['hourly_rate'] == 50.0
    assert employees[1]['hours_worked'] == 150.0