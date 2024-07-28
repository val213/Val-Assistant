from mocked_information import *


def get_destination_recommendation(query):
    return destination


def get_attraction_recommendation(city):
    return attraction


def get_dining_recommendation(city):
    return dining


def get_life_tips(city):
    return life_tips


def get_local_customs(city):
    return local_customs


def get_current_date():
    return "今天"


def get_weather(location, date=""):
    if date == "":
        date = get_current_date()

    return date + "天气是" + "晴天"


def get_current_location():
    return "北京"


def get_path_recommendation(destination, start='', recommendation=False):
    return "建议通过飞机从" + start + "到" + destination + "\n以下是航班信息\n" + flight