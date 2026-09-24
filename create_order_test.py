# Людмила Крейдер, 47-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Тест: создание заказа и получение заказа по его трек-номеру
def test_create_order_get_order_by_track():

    # Создаём новый заказ
    order_response = sender_stand_request.post_new_order(data.order_body)

    # Проверяем, что заказ успешно создан
    assert order_response.status_code == 201

    # Получаем трек-номер созданного заказа
    track = order_response.json()["track"]

    # Получаем заказ по трек-номеру
    get_response = sender_stand_request.get_order_by_track(track)

    # Проверяем, что сервер вернул код 200
    assert get_response.status_code == 200