# Шипов Александр, 34-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import create_order

# Тест: Проверить, что код ответа 200


def test_get_order_from_track_code_200():
    assert create_order.assert_code_200() == data.status_code_200
