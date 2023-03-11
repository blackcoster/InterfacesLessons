#это основной файл
import dz_import

a = [1,2,6,6,3,4,5]

print(dz_import.func(a))

# #это модуль dz_import.py
#
# def func(a):
#     b = set(a)
#     if len(a)==len(b):
#         return 'уникальны'
#     else:
#         return 'не уникальны'