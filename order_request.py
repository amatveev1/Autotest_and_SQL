import configuration
import requests
import data
import random
import datetime

import order_request

#Списки данных для рандомизатора
firstName_list = ["Иван", "Петр", "Максимилиан", "Самокат", "Рудольф", "Потап", "Бурдюк", "Саня", "Андрей", "Скейтер", "Питер","Джейсон", "Васюган", "Брюс", "Суздаль"]
lastName_list = ["Петров", "Сидоров", "Дизель", "Лопата", "Фруктовый", "Ягодный", "Самокатов", "Стэтхем", "Типуганов", "Чанган", "Муромскый"]
address_list = ["Волоколамское ш., 1-2", "Новинская пл., 2 с.34", "Мурашковая ул, д45", "Восстания пл., 2", "Будущее, д.21", "Джими-Чо, д.21", "Джековая стрит, с.21", "Вазовская ул., д.4 с.21", "Петровский б-р., д.34, к.1", "Васюковский б-р., д.34, к.1"]
phone_number_list = ["+7 800 355 35 35", "+7 234 333 35 35", "+7 111 223 35 35", "+7 234 111 35 35", "+7 777 111 35 35", "+7 777 123 35 35", "+7 134 123 35 35", "+7 999 123 35 35", "+7 999 123 00 00", "+7 999 444 00 00", "+7 999 555 00 00"]


#Рандомизаторы значений параметров body заказа
def random_firstName():
   return random.choice(firstName_list)

def random_lastName():
   return random.choice(lastName_list)

def random_adress():
    return random.choice(address_list)

def random_station():
    return random.randint(0,224)

def random_phone():
    return random.choice(phone_number_list)

def random_rent():
    return  random.randint(1,7)

#Сгенерировать рандомную дату начиная с дня, следующего за сегодняшним
def random_date():
    n = random.randint(1,365)
    future_date = datetime.date.today() + datetime.timedelta(days=n)
    return future_date.strftime('%Y,%m,%d') #Если не формат строки - будет ошибка запроса на создание заказа - не получим трек-номер, не сможем выполнить основную проверку.
# эта функция меняет значения в body
def get_user_body():
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.orders_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = random_firstName()
    current_body["lastName"] = random_lastName()
    current_body["address"] = random_adress()
    current_body["metroStation"] = random_station()
    current_body["phone"] = random_phone()
    current_body["rentTime"] = random_rent()
    current_body["deliveryDate"] = random_date()
    # возвращается новый словарь со сгенерированными рандомными значениями
    return current_body


#Функция создания заказа
def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_CREATE,
                         json=order_request.get_user_body())


#Функция запроса деталей заказа по треку
def get_orders_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDERS,
                        params={'t': track})