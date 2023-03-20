
def _script_task(script, task_data):
    exec(script, task_data)
    task_data.pop("__builtins__")
    return task_data

def script_task1(task_data):
    return _script_task("x=1", task_data)

def script_task2(task_data):
    return _script_task("y=1", task_data)

def script_task3(task_data):
    return _script_task("a=1", task_data)

def script_task4(task_data):
    return _script_task("b=1", task_data)

def run():
    task_data = {}
    task_data = script_task1(task_data)
    task_data = script_task2(task_data)
    task_data = script_task3(task_data)
    task_data = script_task4(task_data)
    return task_data

if __name__ == "__main__":
    import timeit
    print(timeit.timeit(run, number=1000)) # 0.022 - 0.046
    print(run())

