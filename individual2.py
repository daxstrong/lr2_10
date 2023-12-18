#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_arguments(**kwargs):
    return len(kwargs)


# Пример использования:
arguments_count = count_arguments(name="Alice", age=30, city="London", occupation="Engineer")

print(f"Количество аргументов: {arguments_count}")
