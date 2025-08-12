import pytest

from src.reporter import (
    parse_log_file,
    generate_report,
    average_report,
)


def test_parse_log_file(tmp_path):
    """Парсинг корректнного лог-файла."""
    test_file = tmp_path / 'test.log'
    test_file.write_text('{"url": "/test", "response_time": 0.5}')
    logs = parse_log_file([str(test_file)])
    assert len(logs) == 1
    assert logs[0]['url'] == '/test'
    assert logs[0]['response_time'] == 0.5


def test_parse_empty_log_file(tmp_path):
    """Парсинг пустого лог-файла."""
    test_file = tmp_path / 'empty.log'
    test_file.write_text('')
    with pytest.raises(ValueError):
        parse_log_file([str(test_file)])


def test_generate_report():
    """Генерирует отчет правильного типа(average)."""
    test_data = [{'url': '/test', 'response_time': 0.2}]
    headers, table = generate_report(test_data, 'average')
    assert headers == ['handler', 'total', 'avg_response_time']
    assert ('/test', 1, 0.2) in table


def test_average_report():
    """Корректно рассчитывает среднее время ответа и количество обращений."""
    test_data = [
        {'url': '/test', 'response_time': 0.2},
        {'url': '/test', 'response_time': 0.4}
    ]
    headers, table = average_report(test_data)
    assert headers == ['handler', 'total', 'avg_response_time']
    assert ('/test', 2, 0.3) in table


def test_damaged_logs_average_report():
    """Пропускает некорректные записи при расчете."""
    test_data = [
        {'url': '/damaged'},
        {'url': '/damaged', 'response_time': '0.4'},
        {'response_time': 0.4},
        {'url': '/test', 'response_time': 0.4}
    ]
    _, table = average_report(test_data)
    assert ('/test', 1, 0.4) in table


def test_wrong_report_type():
    """Вызывает ошибку при неверном типе отчета."""
    with pytest.raises(ValueError):
        generate_report([], 'wrong_type')
