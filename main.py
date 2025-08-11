import argparse
import json


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
    with open(file_path, 'r') as f:
        return json.load(f)


def generate_report(log_data):
    ...


def average_report():
    ...


def main():
    args = parse_args()
    log_data = parse_log_file(args.file)
    ...


if __name__ == '__main__':
    main()
