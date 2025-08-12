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
        nargs='+',
        help='Путь к лог файлу(файлам).'
    )
    parser.add_argument(
        '-r',
        '--report',
        required=True,
        choices=['average', ],
        help='Тип отчета (по умолчанию: average)'
    )
    return parser.parse_args()


def parse_log_file(file_paths):
    log_data = []
    for path in file_paths:
        with open(path, 'r') as f:
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
    report = defaultdict(lambda: {
        'total': 0,
        'sum_time': 0.0,
        'avg_time': 0.0
    })
    for row in log_data:
        url = row['url']
        report[url]['total'] += 1
        report[url]['sum_time'] += row['response_time']
        report[url]['avg_time'] = round(
            report[url]['sum_time'] / report[url]['total'],
            3
        )
    headers = ['handler', 'total', 'avg_response_time']
    table = [(
        url,
        report[url]['total'],
        report[url]['avg_time']
    ) for url in report]
    return headers, table
