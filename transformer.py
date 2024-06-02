import csv

def transToFile(parent_file, data_list):
    header = ["Product Name", "Description", "Manageable", "Interface", "Layer", "RRP excl GST", "Product Type"]

    with open(parent_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for data_dict in data_list:
            writer.writerow(data_dict)