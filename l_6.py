import requests
import inspect
import sys
print(sys.excutable)
print(sys.version)
print(sys.platform)
print(sys.argv)
print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
for _ in dir(__builtins__):
    print(_)
