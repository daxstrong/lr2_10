#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_after_max(*args):
    if not args:
        return None

    max_arg = max(args)
    max_index = args.index(max_arg)

    if max_index == len(args) - 1:
        return None  # Если максимальный аргумент находится в конце списка

    return sum(args[max_index + 1:])


# Пример использования:
arguments = [3, 7, 2, 8, 5, 2]
result = sum_after_max(*arguments)

if result is None:
    print("Список аргументов пуст или максимальный аргумент находится в конце списка.")
else:
    print(f"Сумма аргументов после максимального: {result}")
