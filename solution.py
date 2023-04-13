import pandas as pd
import numpy as np
from scipy import stats

chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(sample_control, sample_test) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha=0.08
    _, pvalue = stats.ttest_ind(sample_control, sample_test)
    return pvalue < alpha
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Ваш ответ, True или False
