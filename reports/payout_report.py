import json
from reports.base_report import BaseReport


class PayoutReport(BaseReport):
    def generate(self):
        departments = {}
        report = []
        for emp in self.employees:
            dept = emp['department']
            if dept not in departments:
                departments[dept] = []
            emp['payout'] = emp['hours_worked'] * emp['hourly_rate']
            departments[dept].append(emp)
            report.append(emp)
        print(f'\t\t\t name\t\t\t hours\t\trate\t\tpayout')
        for key, val in departments.items():
            print(f'{key}')
            for em in val:
                print(f'\t\t\t {em['name']}\t\t {em['hours_worked']} \t\t{em['hourly_rate']} \t\t{em['payout']}')
        return json.dumps(report, indent=2, ensure_ascii=False)