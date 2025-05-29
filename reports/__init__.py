from reports.payout_report import PayoutReport

REPORTS = {
    'payout': PayoutReport,
}

def get_report_class(report_name: str):
    if report_name not in REPORTS:
        raise ValueError(f"Unknown report type: {report_name}")
    return REPORTS[report_name]