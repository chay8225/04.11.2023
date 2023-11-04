# while True:
#     try:
#         a = int(input('A '))
#         c = 10 / a
#         # c = b / a
#     except ZeroDivisionError:
#         print('Деление на ноль запрещенно, введить а ещё раз')
#     except NameError:
#         print('Змінну ми не знаємо')
#     except ValueError:
#         print('ValueError')
#     else:
#         print('TRY - виконався')
#         break
#     finally:
#         print('Винонається завжди')
#
# print(f'C = {c}')


# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f'Sorry,we can`t work with {type(var_1)} ')
#     else:
#         return var_1
#
# first_var = '10'
# print(checker(first_var))

# class BuildingError(Exception):
#     def __str__(self):
#         return f'With so much material the house cannot be build'
# def check_material(material, limit_material):
#     if material > limit_material:
#         return 'enough material'
#     else:
#         raise BuildingError(material)
#
# material = 500
# check_material(material, 300)

import sys
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.modules)
# for name, module_path in sys.modules.items():
#     print(name, module_path)


# class Counter:
#     def __init__(self, start, stop):
#         self.j = start
#         self.j = stop
#
#     def __iter__(self):
#         self.i = self.i-1
#         return self
#
#     def __next__(self):
#         self.i += self.i
#         if self.i > self.j-1:
#             raise StopIteration
#         return self.i
#
# count = Counter(5, 10)
# for i in count:
#     print(i)