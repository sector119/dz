# 3.Написати програму для опрацювання файлу з даними про аеропорт Остін (Austin).
#
# Використовуючи matplotlib та numpy i pandas, дайте відповіді на наступні питання:
#     a)скільки рейсів до кожного місця призначення було здійснено за день та за місяць
#     b)скільки разів літав кожен літак
#     c)яка середня затримка рейсу за місяць, у певне місце призначення та по днях
#     d)макс та мін тривалість польоту
#     e)макста мін відхилення запланованого часу польоту від фактичного
#     f)чи існує залежність між часом затримки вильоту та тривалістю польоту

import pandas as pd
import numpy as np


def populate_columns(row):
    row['month'], row['day'], row['year'] = row['Date'].split('/')
    row['duration_diff'] = float(row['Scheduled Elapsed Time(Minutes)']) - float(row['Actual Elapsed Time(Minutes)'])

    return row


df = pd.read_csv('austin.csv',
                 encoding='utf-8',
                 sep=',',
                 header=0
                 )

df = df.assign(
    day=None,
    month=None,
    year=None,
    duration_diff=None
)

df = df.apply(populate_columns, axis=1)

# A кільки рейсів до кожного місця призначення було здійснено за день та за місяць

df_a_day = df[
    ['Destination Airport', 'year', 'month', 'day']
].groupby(
    ['Destination Airport', 'year', 'month', 'day'],
    dropna=True
).size(
).reset_index(
    name='size'
).query(
    'size > 1'
)

print(df_a_day)

df_a_month = df[
    ['Destination Airport', 'year', 'month']
].groupby(
    ['Destination Airport', 'year', 'month'],
    dropna=True
).size(
).reset_index(
    name='size'
).query(
    'size > 1'
)

print(df_a_month)

# B скільки разів літав кожен літак
df_b = df[
    ['Tail Number']
].groupby(
    ['Tail Number'],
    dropna=True
).size(
).reset_index(
    name='size'
).query(
    'size > 1'
)

print(df_b)

# C яка середня затримка рейсу за місяць, у певне місце призначення та по днях
df_c_month = df[
    ['Tail Number', 'year', 'month', 'Departure Delay(Minutes)']
].groupby(
    ['Tail Number', 'year', 'month'],
    dropna=True
).mean()

print(df_c_month)

df_c_day = df[
    ['Tail Number', 'year', 'month', 'day', 'Departure Delay(Minutes)']
].groupby(
    ['Tail Number', 'year', 'month', 'day'],
    dropna=True
).mean()

print(df_c_day)

df_c_airport = df[
    ['Tail Number', 'Destination Airport', 'Departure Delay(Minutes)']
].groupby(
    ['Tail Number', 'Destination Airport'],
    dropna=True
).mean()

print(df_c_airport)

# D макс та мін тривалість польоту
df_duration_max_min = df[
    ['Tail Number', 'Actual Elapsed Time(Minutes)']
].groupby(
    ['Tail Number'],
    dropna=True
).agg({'Actual Elapsed Time(Minutes)': [np.max, np.min]})

print(df_duration_max_min)

# E макс та мін відхилення запланованого часу польоту від фактичного
df_duration_diff_max_min = df[
    ['Tail Number', 'duration_dev']
].groupby(
    ['Tail Number'],
    dropna=True
).agg({'duration_dev': [np.max, np.min]})

print(df_duration_diff_max_min)
