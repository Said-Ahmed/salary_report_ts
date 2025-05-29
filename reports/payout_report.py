from typing import List, Dict
from reports.base_report import BaseReport


class PayoutReport(BaseReport):
    def generate(self) -> str:
        total_payout = 0
        report_lines = ["id,name,department,payout"]

        for emp in self.employees:
            payout = emp['hours_worked'] * emp['hourly_rate']
            total_payout += payout
            report_lines.append(
                f"{emp['id']},{emp['name']},{emp['department']},{payout}"
            )

        report_lines.append(f"\nTotal payout,{total_payout}")
        return "\n".join(report_lines)