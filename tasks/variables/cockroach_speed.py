"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Таракан - одно из самых быстрых насекомых.
Нужно отредактировать функцию cockroach_speed, которая принимает скорость
таракана в км/ч так, чтобы она возвращала скорость таракана в см/с
(float округляем вниз)

ПРИМЕРЫ
--------------------------------------------------------------------------------
cockroach_speed(1.08) -> 30
cockroach_speed(2.13) -> 59
"""
import math


def cockroach_speed(kmh_speed: float) -> int:
    """Переводит скорость таракана из км/ч в см/с

    :param kmh_speed: скорость в км/ч

    :return: скорость в см/с
    """

    result = kmh_speed / 0.036
    result = (math.floor(result))

    return result


if __name__ == '__main__':
    speed_val = float(input('Введите скорость таракана в км/ч: '))
    print(f'Скорость таракана в см/с: {cockroach_speed(speed_val)}')
