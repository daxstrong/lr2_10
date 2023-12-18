#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmonic_mean(*args):
    if not args:
        return None

    return len(args) / sum(1 / arg for arg in args)


if __name__ == "__main__":
    arguments = [float(i) for i in input("Введите числа: ").split()]

    result = harmonic_mean(*arguments)
    if result is None:
        print("Список аргументов пуст, среднее гармоническое не может быть вычислено.")
    else:
        print(f"Среднее гармоническое: {result}")
