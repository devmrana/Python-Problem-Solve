# Python version are using
import sys as s
print(s.version)
print(f'API-V . {s.version_info}')

# ---------------------
import platform
print(f'platform . {platform.python_version()}')
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))


def newfunc(*args):
    x = 0
    for i in args:
        x += i # x = x + i
    return x
result = newfunc(54,23,7)
print(result)
