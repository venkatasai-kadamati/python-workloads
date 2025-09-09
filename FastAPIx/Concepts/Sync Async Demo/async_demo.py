from timeit import default_timer as timer
import asyncio
# time -> sleep
# timer -> counter (stopwatch)
# in sync: time.sleep() = in async: await asyncio.sleep(seconds)

'''
Learnings for async implementation, the following steps are standard
1. asyncio.run(main()) -> begin the event loop
2. await asyncio.gather(list of tasks) -> add tasks into the event loop
'''
async def run_task(name: str, seconds: int) -> None:
    """Runs a task that sleeps for a given number of seconds."""
    start_time = timer()
    print(f"{name} starts at: {start_time:.2f}")

    # change 1: time.sleep is blocking, so we need to use await asyncio.sleep
    await asyncio.sleep(seconds)
    end_time = timer()
    print(f"{name} completed at: {end_time:.2f}")

# assume this whole as an event loop
async def main():
    overall_start = timer()

    # change 2: we need to gather all async tasks in the event loop first
    await asyncio.gather(
    run_task("Task 1", 2),
    run_task("Task 2", 1),
    run_task("Task 3", 3),
    )

    total_time = timer() - overall_start
    print(f"Total time taken: {total_time:.2f} s")

# starts/runs the event loop
asyncio.run(main())