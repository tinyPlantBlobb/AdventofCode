import argparse
import importlib

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="The file to read")
parser.add_argument("-d", "--day", help="The day of the advent calendar")
args = parser.parse_args()
input = args.day

with open("day" + input + ".txt", "r") as fileinput:
    data = fileinput.readlines()
day = importlib.import_module("day" + input, "days")
day.run(data)
