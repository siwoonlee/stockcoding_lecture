"""
    func_timeout 예제
    pip install func_timeout
"""

import time
from func_timeout import func_timeout, FunctionTimedOut

# 실행 시간이 긴 함수 예제
def long_running_task(duration):
    print(f"Starting task for {duration} seconds...")
    time.sleep(duration)
    print("Task completed!")

try:
    # long_running_task 함수가 3초 내에 끝나지 않으면 예외 발생
    func_timeout(3, long_running_task, args=(5,))
except FunctionTimedOut:
    print("Function execution timed out!")

print("Program continues...")

func_timeout(3, long_running_task, args=(5,))
