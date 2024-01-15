import configuration
import requests
import data

#Функция создания заказа
def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_CREATE,
                         json=data.orders_body)


#Функция запроса деталей заказа по треку
def get_orders_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDERS,
                        params={'t': track})