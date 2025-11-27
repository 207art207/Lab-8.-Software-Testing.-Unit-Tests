# LW_8
Лабораторна робота 8. Тестування програмного забезпечення. Модульні тести

### Алгоритм для проведення тестування алгоритмів
1. Необхідні бібліотеки:
```
pip install pytest coverage
```
2. Команди для запуску та сбереження результатів тестування (htmlcov/index.html):
```
coverage run -m pytest
coverage report -m
coverage html
```

## Результати покриття коду (coverage)

Звіт згенеровано `coverage.py v7.12.0`.

### Загальний підсумок
- **Total coverage: 92%**
- **Total statements:** 59
- **Missing:** 5
- **Excluded:** 0

### Покриття по файлах

| Файл         | statements | missing | excluded | coverage |
|--------------|-----------:|--------:|---------:|---------:|
| `lw_8.py`      | 37 | 5 | 0 | 86% |
| `test_lw_8.py` | 22 | 0 | 0 | 100% |
| **Total**      | **59** | **5** | **0** | **92%** |

### Покриття по функціях

| Файл     | Функція                         | statements | missing | excluded | coverage |
|----------|----------------------------------|-----------:|--------:|---------:|---------:|
| `lw_8.py` | `Algorithms.min_positive`       | 11 | 2 | 0 | 82% |
| `lw_8.py` | `Algorithms.sum_negative_only`  | 8  | 1 | 0 | 88% |
| `lw_8.py` | `Algorithms.fibonacci_n`        | 10 | 2 | 0 | 80% |
| `lw_8.py` | `Algorithms.current`            | 3  | 0 | 0 | 100% |
| `lw_8.py` | *(no function)*                 | 5  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_min_positive_ok`     | 1  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_min_positive_bad`    | 2  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_sum_negative_only_ok`| 1  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_sum_negative_only_bad`| 2 | 0 | 0 | 100% |
| `test_lw_8.py` | `test_fibonacci_ok`         | 1  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_fibonacci_bad`        | 2  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_current_ok`           | 1  | 0 | 0 | 100% |
| `test_lw_8.py` | `test_current_bad`          | 2  | 0 | 0 | 100% |
| `test_lw_8.py` | *(no function)*             | 10 | 0 | 0 | 100% |
| **Total** |                                  | **59** | **5** | **0** | **92%** |

### Покриття по класах

| Файл     | Клас          | statements | missing | excluded | coverage |
|----------|---------------|-----------:|--------:|---------:|---------:|
| `lw_8.py` | `Algorithms` | 32 | 5 | 0 | 84% |
| `lw_8.py` | *(no class)* | 5  | 0 | 0 | 100% |
| `test_lw_8.py` | *(no class)* | 22 | 0 | 0 | 100% |
| **Total** |              | **59** | **5** | **0** | **92%** |