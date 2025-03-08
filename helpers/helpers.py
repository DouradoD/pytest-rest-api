import json
import time

def execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Function Name: {func.__name__}| Execution time: {end_time - start_time} seconds')
    return wrapper

def get_json_value(path):
    with open(path, 'r', encoding="utf8") as file:
        return json.load(file)