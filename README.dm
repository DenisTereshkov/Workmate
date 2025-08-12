
## Установка и запуск

1. **Требования**: Python 3.12
2. **Настройка окружения**:
   ```bash
   venv\Scripts\activate     # Windows
   ```
3. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Запуск**:
   ```bash
   python main.py -f logs/example1.log -r average
   python main.py --file logs/example1.log --report average
   ```
   Для нескольких файлов:
   ```bash
   python main.py -f logs/example1.log logs/example2.log -r average
   python main.py --file logs/example1.log logs/example2.log --report average
   ```

## Тестирование
```bash
pytest
```