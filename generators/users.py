"""Users generator"""
import csv
from datetime import datetime
import pandas as pd
from faker import Faker

fake = Faker("es_MX")


def get_users(num):
    """Generate fake users dictionary"""
    output = [
        {
            "password": "pbkdf2_sha256$216000$wozq8O9InKLO$7/3uKJ60okpykHqE//vSszKjxjxxVbLyH17pZs0BChY=",  # admin1234
            "last_login": datetime.now(),
            "is_superuser": 0,
            "username": fake.simple_profile()["username"],
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "is_staff": 0,
            "is_active": 1,
            "date_joined": datetime.now(),
        }
        for x in range(num)
    ]
    return output


def get_users_df(num=1):
    """Create users dataframe"""
    return pd.DataFrame(get_users(num))


if __name__ == "__main__":
    users = get_users_df(100)
    users.to_csv("./outputs/users.csv", sep=";", index= False, quoting=csv.QUOTE_ALL)
