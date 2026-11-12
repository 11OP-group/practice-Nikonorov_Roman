# Задача 1. Диагностика состояния здоровья

# Константы пороговых значений
TEMP_CRIT_MIN = 35.0
TEMP_NORM_MIN = 36.0
TEMP_NORM_MAX = 37.0
TEMP_CRIT_MAX = 38.0

PRESS_CRIT_MIN = 105
PRESS_NORM_MIN = 110
PRESS_NORM_MAX = 130
PRESS_CRIT_MAX = 140

PULSE_CRIT_MIN = 55
PULSE_NORM_MIN = 60
PULSE_NORM_MAX = 100
PULSE_CRIT_MAX = 110

temperature = float(input("Введите температуру (°C): "))
pressure = int(input("Введите верхнее давление: "))
pulse = int(input("Введите пульс (уд/мин): "))

# Проверка ввода на корректность (реалистичные границы)
if not (30.0 <= temperature <= 45.0 and 40 <= pressure <= 260 and 20 <= pulse <= 250):
    print("Ошибка ввода: некорректные показатели.")
else:
    # Проверка критических отклонений (хотя бы один параметр вне безопасных рамок)
    if (
        temperature < TEMP_CRIT_MIN or temperature > TEMP_CRIT_MAX
        or pressure < PRESS_CRIT_MIN or pressure > PRESS_CRIT_MAX
        or pulse < PULSE_CRIT_MIN or pulse > PULSE_CRIT_MAX
    ):
        status = "Требуется врач"
    # Проверка нормального состояния (все параметры в норме)
    elif (
        TEMP_NORM_MIN <= temperature <= TEMP_NORM_MAX
        and PRESS_NORM_MIN <= pressure <= PRESS_NORM_MAX
        and PULSE_NORM_MIN <= pulse <= PULSE_NORM_MAX
    ):
        status = "Нормальное состояние"
    # Остальные допустимые значения попадают в легкое недомогание
    else:
        status = "Легкое недомогание"

    print(f"Результат диагностики: {status}")
