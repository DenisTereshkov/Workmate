from src.reporter import (
    generate_report,
    parse_args,
    parse_log_file,
    print_report
)


def main():
    args = parse_args()
    log_data = parse_log_file(args.file)
    report_headers, report_data = generate_report(log_data, args.report)
    print_report(report_headers, report_data)


if __name__ == '__main__':
    main()
