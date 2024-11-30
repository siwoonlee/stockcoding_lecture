import time
from functools import wraps

from loguru import logger
import numpy as np


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished executing {func.__name__}")
        return result
    return wrapper

@record_time
@log_execution
def main():
    for i in range(10000):
        x = np.random.rand(100)
        y = np.random.rand(100)
        z = x * y


if __name__ == "__main__":
    main()
