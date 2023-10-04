def add_time(start, duration, day=None):
    hour, start_am_pm = start.split(" ")
    h, min = hour.split(":")
    d_h, d_min = duration.split(":")
    week_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    new_am_pm = ""
    new_hour = int(h) + int(d_h)
    new_min = int(min) + int(d_min)
    day_count = day
    week_day = ""

    if new_min > 59:
        new_hour += new_min // 60
        new_min = new_min % 60

    am_pm = new_hour // 12

    if am_pm % 2 == 0:
        new_am_pm += start_am_pm
    else:
        if start_am_pm == "AM":
            new_am_pm = "PM"
        else:
            new_am_pm = "AM"

    if (am_pm == 1 and new_am_pm == "AM") or (am_pm == 2 and new_am_pm == "AM"):
        day_count = "next day"
        if day:
            day_index = week_days.index(day.capitalize()) + 1
            week_day = week_days[day_index % 7]
    if am_pm > 2 and new_am_pm == "AM":
        day_count = str(am_pm // 2 + 1) + " days later"
        if day:
            day_index = week_days.index(day.capitalize()) + (am_pm // 2 + 1)
            week_day = week_days[day_index % 7]
    if am_pm > 2 and new_am_pm == "PM":
        day_count = str(am_pm // 2) + " days later"
        if day:
            day_index = week_days.index(day.capitalize()) + (am_pm // 2)
            week_day = week_days[day_index % 7]

    new_hour = new_hour % 12
    new_hour = 12 if new_hour == 0 else new_hour
    new_min = "0" + str(new_min) if new_min < 10 else new_min

    if not day and day_count == None:
        return print(f"{new_hour}:{new_min} {new_am_pm}")
    if not day and day_count:
        return print(f"{new_hour}:{new_min} {new_am_pm} ({day_count})")
    if day and week_day == "":
        return print(f"{new_hour}:{new_min} {new_am_pm}, {day_count}")
    if day and week_day != "":
        return print(f"{new_hour}:{new_min} {new_am_pm}, {week_day} ({day_count})")


add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 AM", "24:00", "saturDay")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "tuesday")
