import configuration
import requests


# Функция для создания заказа
def post_new_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + "/api/v1/orders",
        json=order_body
    )


# Функция для получения заказа по трек-номеру
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + "/api/v1/orders/track",
        params={"t": track}
    )