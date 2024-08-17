import csv

def readCSV(file_path):
    data = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['Name']] = row
    return data
def displayReport(name, data):
    if name in data:
        report = data[name]
        print(f"\n{'-'*40}")
        print(f"Health Report for {name}".center(40))
        print(f"{'-'*40}\n")
        maxKeyLength = max(len(key) for key in report.keys())
        for key, value in report.items():
            print(f"{key.ljust(maxKeyLength)} : {value}")
        print(f"\n{'-'*40}")
    else:
        print(f"No report found for {name}. Please diagnose for a new report.")
def start():
    filePath = "C:/Users/rajur/OneDrive/Desktop/health_reports.csv"
    data = readCSV(filePath)
    name = input("Enter the name to search for reports: ")
    displayReport(name, data)
start()
