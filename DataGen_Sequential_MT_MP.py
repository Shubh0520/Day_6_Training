import random
import operator
from datetime import datetime
from multiprocessing import Pool

# List of tuple for operations
operators = [("+", operator.add), ("-", operator.sub), ("*", operator.mul), ('/', operator.truediv)]


# Function for data generation
def data_generator():
    data_list = []
    # Random numbers
    for i in range(1, 2000):
        op, fn = random.choice(operators)
        data = {"num1": random.randint(1, 2000), "num2": random.randint(1, 2000), "operator": op}
        data_list.append(data)
    return data_list


def sequential_process():
    start_time = datetime.now()
    output = []
    data_process = data_generator()
    for val in data_process:
        result_dict = {}
        print(val)
        num1 = val['num1']
        num2 = val['num2']
        operation = val['operator']
        if '*' in operation:
            result = num1 * num2
        if "+" in operation:
            result = num1 + num2
        if "/" in operation:
            result = num1 / num2
        if "-" in operation:
            result = num1 - num2
        result_dict['num1'] = num1
        result_dict['num2'] = num2
        result_dict['result'] = result
        result_dict['operator'] = operation
        output.append(result_dict)
        return output
        end_time = datetime.now()
        print('Sequential Execution process duration is: {}'.format(end_time - start_time))


def multithreading_process():
    pass


def multiprocessing_process():
    output_obj = sequential_process()
    start_time = datetime.now()
    with Pool(processes=1) as pool:
        number = 100
        result = pool.apply_async(output_obj)
        pool = Pool(10)
    end_time = datetime.now()
    print('MultiProcessing Execution process duration is: {}'.format(end_time - start_time))


if __name__ == "__main__":
    print(data_generator())
    print(sequential_process())
    print(multiprocessing_process())
