# factorial.py

def factorial(n: int) -> int:
    # 학생들이 이 부분을 작성해야 합니다.
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
