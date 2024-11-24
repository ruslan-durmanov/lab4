import json


# TODO решите задачу


def task(file_input):
    final_sum = 0
    with open(file_input, 'r') as file_r:
        data = json.load(file_r)
    for line in data:
        final_sum += line['score'] * line['weight']
    return round(final_sum, 3)


print(task(r'input.json'))
