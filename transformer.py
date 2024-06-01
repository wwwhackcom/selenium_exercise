import csv

def transToFile(parent_file, child_file, data):
    with open(parent_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0])

    with open(child_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[1])