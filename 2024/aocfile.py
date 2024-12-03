import argparse
import importlib
import days
import days.day1

parser = argparse.ArgumentParser()
# parser.add_argument("filename", help="The file to read")
parser.add_argument("-d", "--day", help="The day of the advent calendar")
parser.add_argument("--days_up_to", help="run all days up to the given number")
args = parser.parse_args()
input = args.day
alldays = args.days_up_to
if input:
    print("Day" + input + "of Advent of Code 2024")
    with open("inputs/day" + input + ".txt", "r") as fileinput:
        data = fileinput.readlines()
    currentday = "days.day" + input
    day = importlib.import_module(currentday)
    day.run(data)

if alldays:
    for i in range(1, int(alldays) + 1):
        print("Day " + str(i) + " of Advent of code 2024")
        with open("inputs/day" + str(i) + ".txt", "r") as fileinput:
            data = fileinput.readlines()
            currentday = "days.day" + str(i)
            day = importlib.import_module(currentday)
            day.run(data)


# days.day1.run(data)
