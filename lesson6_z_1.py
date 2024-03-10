a,b=map(int,input().split())
try:
    a or b != 0
    a/b
except ZeroDivisionError:
    print("Не можна ділити на 0")