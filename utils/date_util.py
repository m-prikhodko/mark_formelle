from datetime import datetime, timedelta


def get_day_after_tomorrow():
    day_after_tomorrow = datetime.today() + timedelta(days=2)
    day_after_tomorrow = day_after_tomorrow.replace(hour=3, minute=0, second=0, microsecond=0)
    unix_time = int(day_after_tomorrow.timestamp()) * 1000
    str_date = day_after_tomorrow.strftime('%d.%m.%Y')
    return unix_time, str_date
