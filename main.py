import argparse
from utils.parser import parse_files
from reports import get_report_class

def main():
    parser = argparse.ArgumentParser(description='Generate employee reports')
    parser.add_argument('files', nargs='+', help='CSV files with employee data')
    parser.add_argument('--report', required=True, help='Report type to generate')
    args = parser.parse_args()

    employees = parse_files(args.files)
    report_class = get_report_class(args.report)
    report = report_class(employees)
    print(report.generate())

if __name__ == '__main__':
    main()