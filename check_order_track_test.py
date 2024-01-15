import order_request


#Получить номер трека
def get_track_order():
    response = order_request.post_new_orders()
    return response.json()['track']

#Матвеев Анатолий, 12-я когорта - Финальный проект. Инженер по тестированию плюс.
#Проверить возможность запроса деталей заказа по номеру трека
def test_order():
    track = get_track_order()
    response = order_request.get_orders_by_track(track)
    assert response.status_code == 200
