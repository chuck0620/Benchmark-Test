from datetime import datetime
from collections import defaultdict
import json
import timeit

from competency_evaluator import get_report

def report_with_dates(startDate = datetime(1999,1,1), endDate = datetime.now()):
    file_in = open('all_game_data.json')
    data = json.load(file_in)
    full_data = {}
    #file_out = open('game_evaluation.json', 'w')
    try:
        with open('game_evaluation.json', 'x') as file_out:
            print("File created")
    except:
        with open('game_evaluation.json', 'r') as file_out:
            full_data = json.load(file_out)

    print(full_data)
    reportList = []
    rawData_list = []
    numberOfRelevantData = 0
    for i in data:
        x = datetime.strptime(data[i]['starttime'], '%y/%m/%d %H:%M')
        if x > startDate and x <= endDate:
            numberOfRelevantData += 1
    minTimeEstimated = str(numberOfRelevantData * 0.5)
    maxTimeEstimated = str(numberOfRelevantData * 5)
    print("Estimated runtime: " + minTimeEstimated + "s - " + maxTimeEstimated + "s")
    for i in data:
        x = datetime.strptime(data[i]['starttime'], '%y/%m/%d %H:%M')
        if i in full_data:
            continue
        if x > startDate and x <= endDate:
            rawData_list.append(i)
            try:
               reportList.append([get_report(data[i])])
            except:
                print("An error has occurred with analyzing raw game data: " + i)
                reportList.append("An error has occurred while evaluating this data")
    full_data = dict(zip(rawData_list, reportList))
    if len(full_data) != 0:
        with open('game_evaluation.json', 'a') as file_out:
            json.dump(full_data, file_out)

    file_in.close()

if __name__ == '__main__':
    start = timeit.default_timer()
    report_with_dates(datetime(2022,1,20), datetime(2022,1,25))
    stop = timeit.default_timer()
    print("The program took ", stop-start, "s to run")


