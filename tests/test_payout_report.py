import pytest
from reports.payout_report import PayoutReport
import json


@pytest.fixture
def sample_employees():
    return [
        {'id': 1, 'name': 'Alice', 'department': 'Marketing',
         'hours_worked': 160, 'hourly_rate': 50},
        {'id': 2, 'name': 'Bob', 'department': 'Design',
         'hours_worked': 150, 'hourly_rate': 40},
        {'id': 3, 'name': 'Carol', 'department': 'Design',
         'hours_worked': 170, 'hourly_rate': 60}
    ]


def test_payout_report_generate_json(sample_employees):
    """Тестируем JSON-вывод"""
    report = PayoutReport(sample_employees)
    result = report.generate()

    parsed = json.loads(result)
    assert len(parsed) == 3
    assert parsed[0]['payout'] == 8000
    assert parsed[1]['payout'] == 6000


def test_payout_report_empty_input():
    """Тестируем пустой список сотрудников"""
    report = PayoutReport([])
    result = report.generate()
    assert json.loads(result) == []