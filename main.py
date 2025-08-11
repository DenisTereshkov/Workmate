from src.reporter import generate_report, parse_args, parse_log_file


def main():
    args = parse_args()
    log_data = parse_log_file(args.file)
    generate_report(log_data, args.report)


if __name__ == '__main__':
    main()
