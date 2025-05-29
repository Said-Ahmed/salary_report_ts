from reports.payout_report import PayoutReport


def test_payout_report_generation():
    employees = [
        {'id': 1, 'name': 'Alice', 'department': 'Marketing',
         'hours_worked': 160, 'hourly_rate': 50},
        {'id': 2, 'name': 'Bob', 'department': 'Design',
         'hours_worked': 150, 'hourly_rate': 40}
    ]

    report = PayoutReport(employees)
    result = report.generate()

    assert "1,Alice,Marketing,8000" in result
    assert "2,Bob,Design,6000" in result
    assert "Total payout,14000" in result