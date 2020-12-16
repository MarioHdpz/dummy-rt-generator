"""Users generator"""

import csv
import json
import random
import datetime

import pandas as pd
from faker import Faker

fake = Faker("es_MX")


def get_transactions(num):
    """Generate fake transactions dictionary"""
    genders = ["m", "f"]

    transactions = []
    for x in range(num):
        latitude, longitude, place, _, _ = fake.local_latlng(
            country_code="MX", coords_only=False
        )
        transactions.append(
            {
                "date": fake.date_time_between(start_date="-30d", end_date="+30d"),
                "gender": random.choice(genders),
                "platform_id": 1,
                "duration": random.randint(10, 360),
                "latitude": latitude,
                "longitude": longitude,
                "geostamp": json.dumps({"place": place}),
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now(),
                "shop_id": random.randint(1, 4),
                "user_id": random.randint(1, 100),
                "status": "terminada",
            }
        )

    return transactions, tickets, address, pictures


def get_transactions_df(num=1):
    """Create users dataframe"""
    return pd.DataFrame(get_transactions(num))


if __name__ == "__main__":
    transactions = get_transactions_df(1000)
    transactions.to_csv(
        "./outputs/transactions.csv", sep=";", index=False, quoting=csv.QUOTE_ALL
    )
