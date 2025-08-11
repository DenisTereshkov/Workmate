import argparse
import json
from collections import defaultdict

from tabulate import tabulate


def parse_args():
    parser = argparse.ArgumentParser(
        description='Читает лог файд и генерирует отчет.'
    )
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        help='Путь к лог файлу.'
    )
    parser.add_argument(
        '-r',
        '--report',
        choices=['average', ],
        default='average',
        help='Тип отчета (по умолчанию: average)'
    )
    return parser.parse_args()


def parse_log_file(file_path):
    log_data = []
    with open(file_path, 'r') as f:
        for row in f:
            log_data.append(json.loads(row))
    return log_data


def generate_report(log_data, report_type):
    if report_type == 'average':
        return average_report(log_data)
    else:
        raise ValueError(f'Неизвестный тип отчета: {report_type}')


def print_report(headers, table_data):
    print(tabulate(
        table_data,
        headers=headers,
        tablefmt='grid',
        showindex=True)
    )


def average_report(log_data):
    report = defaultdict(lambda: {'total': 0, 'sum_time': 0.0, 'avg_time': 0.0})
    for row in log_data:
        url = row['url']
        report[url]['total'] += 1
        report[url]['sum_time'] += row['response_time']
        report[url]['avg_time'] = round(
            report[url]['sum_time'] / report[url]['total'],
            3
        )
    headers = ['handler', 'total', 'avg_response_time']
    table = [(url, report[url]['total'], report[url]['avg_time']) for url in report]

    print_report(headers, table)


def main():
    args = parse_args()
    log_data = parse_log_file(args.file)
    generate_report(log_data, args.report)


if __name__ == '__main__':
    main()
