#Найти суммарную стоимость билетов по каждому классу
#обслуживания (поле Pclass).
#1. Survived — обозначает, выжил данный пассажир или нет (0 для умерших, 1 для выживших);
#2. Pclass — класс пассажира (1 — высший, 2 — средний, 3 — низший);
#3. Name — имя;
#4. Sex — пол;
#5. Age — возраст;
#6. SibSp — количество братьев, сестер, сводных братьев, сводных сестер, супругов на борту
#титаника;
#7. Parch — количество родителей, детей (в том числе приемных) на борту титаника;
#8. Ticket — номер билета;
#9. Fare — плата за проезд;
#10. Cabin — каюта;
#11. Embarked — порт посадки (C — Шербур; Q — Квинстаун; S — Саутгемптон).

#import csv
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np


def info_ticket(a):
    with open('data.csv', 'r') as file:
        v = 0
        s = 0
        e = 0
        for line in file:
            data = line.split(',')
            if data[2] == '1' and data[5] == a:
                v += float(data[10])
            elif data[2] == '2' and data[5] == a:
                s += float(data[10])
            elif data[2] == '3' and data[5] == a:
                e += float(data[10])
    return v, s, e


def graf(v, s, e):
    X = ['VIP', 'Стандарт', 'Эконом']
    arr_x = [v, s, e]
    X_axis = np.arange(len(X))
    plt.bar(X_axis - 0.0, arr_x, 0.6)
    plt.xticks(X_axis, X)
    plt.xlabel("Билет")
    plt.ylabel("Выручка")
    plt.title("Суммарная стоимость билетов по каждому классу")
    plt.show()
    return st.pyplot(plt)


st.image('titanik.jpg')
st.title("Данные пасажиров Титаника")
st.subheader("Задание: Найти суммарную стоимость билетов пассажиров указанного пола по каждому классу обслуживания.")
st.header("Решение:")
choice = st.selectbox('Суммарная стоимость билетов по каждому классу',
                      ['Всех проданных билетов', 'Проданных для мужчин', 'Проданных для женщин'])
if choice == 'Всех проданных билетов':
    with open('data.csv', 'r') as file:
        v = 0
        s = 0
        e = 0
        for line in file:
            data = line.split(',')
            if data[2] == '1':
                v += float(data[10])
            elif data[2] == '2':
                s += float(data[10])
            elif data[2] == '3':
                e += float(data[10])
    st.table({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                      '\"среднего(стандартного)\" класса',
                                                      '\"низший(эконом)\" класса'],
              'Кол-во': [round(v, 2), round(s, 2), round(e, 2)]})
    graf(v, s, e)

elif choice == 'Проданных для мужчин':
    v, s, e = info_ticket('male')
    st.table({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                      '\"среднего(стандартного)\" класса',
                                                      '\"низший(эконом)\" класса'],
              'Кол-во': [round(v, 2), round(s, 2), round(e, 2)]})
    graf(v, s, e)
elif choice == 'Проданных для женщин':
    v, s, e = info_ticket('female')
    st.table({'Сумма полученная от продажи билетов': ['\"высшего(VIP)\" класса',
                                                      '\"среднего(стандартного)\" класса',
                                                      '\"низший(эконом)\" класса'],
              'Кол-во': [round(v, 2), round(s, 2), round(e, 2)]})
    graf(v, s, e)
