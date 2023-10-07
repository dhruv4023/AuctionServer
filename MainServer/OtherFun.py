from datetime import datetime

def anyDateTimeTo_datetime_Formate(date_time_str,input_format="%d-%m-%Y %H:%M:%S"):
    # Use datetime.strptime() to parse the input string into a datetime object
    return  datetime.strptime(date_time_str, input_format)