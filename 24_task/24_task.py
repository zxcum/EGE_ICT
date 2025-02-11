import re


def find_max_expression_length(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().strip()

    pattern = re.compile(r'((?:0|[6789]\d*)(?:[-*](?:0|[6789]\d*))*)')

    matches = pattern.findall(data)

    if matches:
        max_expression = max(matches, key=len)
        return len(max_expression), max_expression
    return 0, ""


# Запуск кода и вывод результата
filename = "24-319.txt"
result_length, result_expression = find_max_expression_length(filename)
print(result_length)
print(result_expression)