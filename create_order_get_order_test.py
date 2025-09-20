# Шипов Александр, 34-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

#   Создаем заказ


def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=data.headers)

#   Получаем заказ по трек-номеру


def get_order_from_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK + str(track),
                        headers=data.headers)


#   Выполняем запрос на получение заказа по треку


def assert_code_200():
    response_pno = create_order(data.order_body)
    track = response_pno.json()["track"]
    return get_order_from_track(track).status_code

# Тест: Проверить, что код ответа 200


def test_get_order_from_track_code_200():
    assert assert_code_200() == data.status_code_200
