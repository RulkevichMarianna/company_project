import json

from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    login: str
    fullname: str
    order: list = None


class Item(BaseModel):
    id: UUID
    name: str
    price: int


class Order(BaseModel):
    user: User
    created_at: str
    items: list[Item]


if __name__ == "__main__":
    while True:
        text = input("Введите команду SAVE, ORDER, TOTAL_PRICE или EXIT:")
        text = text.upper()
        text_list = text.split(" ")
        command = text_list[-1]
        if command == "SAVE":
            with open('input.json') as json_string:
                save = json.load(json_string)
                order = Order(**save)
                user_login = order.user.login
                print(user_login)
                print("Данные сохранены")
        if command == "ORDERS":
            user = order.user
            for item in user:
                if item == "superLogin":
                    new_dict = { }
                pass
        if command == "TOTAL_PRICE":
            pass
        if command == "EXIT":
            print("Выполнен выход")
            break
