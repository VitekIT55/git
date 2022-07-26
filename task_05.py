def date_in_future(integer):
    import datetime as dt
    if type(integer) == float:
        return dt.datetime.today().strftime("%d-%m-%Y %H:%M:%S")
    integer = int(integer[0])
    return (dt.datetime.now() + dt.timedelta(days=integer)).strftime("%d-%m-%Y %H:%M:%S")