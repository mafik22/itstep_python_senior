import warnings
print(f"NameError - {type(NameError)}-{issubclass(NameError, BaseException)}")
a = 1
b = 0
try:
    a / b
except ZeroDivisionError:
    print("На нуль ділити не можна")
try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("Файл не знайдено")
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("warning, no code here", SyntaxWarning)
try:
    warnings.warn("Warning, module not import", ImportWarning)
except:
    print("Warning processed")

