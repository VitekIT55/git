def date_in_future(integer):
    import datetime as dt
    if type(integer) == int:
        return (dt.datetime.now() + dt.timedelta(days=integer)).strftime("%d-%m-%Y %H:%M:%S")
    else:
        return dt.datetime.today().strftime("%d-%m-%Y %H:%M:%S")