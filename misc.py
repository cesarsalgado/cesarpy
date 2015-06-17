import datetime

def get_current_date_and_time_str():
    return datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
