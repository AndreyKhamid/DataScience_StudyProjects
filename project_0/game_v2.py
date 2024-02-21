"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
# Импорт библиотеки nampy.
import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число с уникальными условиями увеличения и уменьшения числа
    до того, пока оно не станет равным загаданному. 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # Запускаем счетчик и выбираем рандомное число.
    count = 0
    predict = np.random.randint(1, 101)
    
    # Пока загаданное число не равно рандомному при условиях >/< увеличиваем или уменьшаем последнее.
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 5
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    # Фиксируем сид для воспроизводимости.
    np.random.seed(1)
    # Загадали список чисел.
    random_array = np.random.randint(1, 101, size=(1000))
    
    # Формируем список попыток для угадывания каждого числа из списка выше.
    for number in random_array:
        count_ls.append(random_predict(number))
    # Получаем среднее значение из списка попыток угадывания
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)