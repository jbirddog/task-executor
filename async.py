import asyncio
import time
import uvloop

from concurrent.futures import ThreadPoolExecutor

uvloop.install()
_executor = ThreadPoolExecutor(8)

def _script_task(script, task_data):
    exec(script, task_data)
    task_data.pop("__builtins__")
    #time.sleep(1)
    return task_data

def script_task1():
    _script_task("x=1", {})

def script_task2():
    _script_task("y=1", {})

def script_task3():
    _script_task("a=1", {})

def script_task4():
    _script_task("b=1", {})

async def in_thread(f):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, script_task1),
    
async def main():
    results = await asyncio.gather(
        in_thread(script_task1),
        in_thread(script_task2),
        in_thread(script_task3),
        in_thread(script_task4),
    )
    #task_data = {}
    #print(results)

def do_it():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    return
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()

if __name__ == "__main__":
    import timeit
    print(timeit.timeit(do_it, number=1000)) # 0.33 - 0.42
    #print(do_it())

    #asyncio.run(main())

