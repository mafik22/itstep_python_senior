list = ["a","b","c"]
a = int(input("Введіть індекс елемента"))
try:
    a >= 0 and a < len(list)
    print("Елемент за введеним індексом:", list[a])
except IndexError:
    print("Невірний індекс")