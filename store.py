import requests


def get_categories():
    res_categories = requests.get("https://api.escuelajs.co/api/v1/categories")
    categories = res_categories.json()
    return categories

