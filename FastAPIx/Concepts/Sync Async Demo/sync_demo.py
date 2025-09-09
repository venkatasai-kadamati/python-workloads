import time
from timeit import default_timer as timer

# time -> sleep
# timer -> counter (stopwatch)

def run_task(name: str, seconds: int) -> None:
    """Runs a task that sleeps for a given number of seconds."""
    start_time = timer()
    print(f"{name} starts at: {start_time:.2f}")
    time.sleep(seconds)
    end_time = timer()
    print(f"{name} completed at: {end_time:.2f}")

if __name__ == "__main__":
    overall_start = timer()

    run_task("Task 1", 2)
    run_task("Task 2", 1)
    run_task("Task 3", 3)

    total_time = timer() - overall_start
    print(f"Total time taken: {total_time:.2f} s")