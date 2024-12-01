import argparse
import importlib
import days
import days.day1

parser = argparse.ArgumentParser()
# parser.add_argument("filename", help="The file to read")
parser.add_argument("-d", "--day", help="The day of the advent calendar")
args = parser.parse_args()
input = args.day


with open("inputs/day" + input + ".txt", "r") as fileinput:
    data = fileinput.readlines()
currentday = "days.day" + input
day = importlib.import_module(currentday)

day.run(data)

# days.day1.run(data)
