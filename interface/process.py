from sqlite3 import connect
from ics import Calendar

def add_to_data(data: dict, time: 'Arrow', name: str) -> None:
    if time.year not in data:
        data[time.year] = dict()
    if time.month not in data[time.year]:
        data[time.year][time.month] = dict()
    if time.day not in data[time.year][time.month]:
        data[time.year][time.month][time.day] = list()
    data[time.year][time.month][time.day].append(name)

def process_ics(file: str) -> dict:
    data = dict()
    with open(file, encoding='utf-8') as ics_file:
        calendar = Calendar(ics_file.read())
        for event in calendar.events:
            time = event.begin.to('Asia/Taipei')
            add_to_data(data, time, event.name)
    return data

def process(file: str, success):
    data = process_ics(file)
    success()