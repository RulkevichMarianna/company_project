import json

from pydantic import BaseModel
from datetime import datetime
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
    user: dict
    created_at: datetime
    items: list


if __name__ == "__main__":
    while True:
        text = input("Введите команду SAVE, ORDER, TOTAL_PRICE или EXIT:")
        text = text.upper()
        text_list = text.split(" ")
        command = text_list[-1]
        if command == "SAVE":
            with open('input.json') as json_string:
                save = json.load(json_string)
            user = User(**save)
            created_at = str(save['createdAt'])
            item = Item(**save)
            print(user)
        if command == "ORDERS":
            def orders():
                pass
        if command == "TOTAL_PRICE":
            pass
        if command == "EXIT":
            print("Выполнен выход")
            break
