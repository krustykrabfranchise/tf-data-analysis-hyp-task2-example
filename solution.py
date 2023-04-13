import pandas as pd
import numpy as np
import scipy as sp


chat_id = 6064443932 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return sp.stats.anderson_ksamp([x, y]).pvalue < 0.03
