with open("practice\covid19_day_wise.csv", "r", encoding="utf-8") as f:
    data = f.readlines()

covid = {
    "date": [],
    "data": [],
    "header": [h for h in data[0].strip().split(",")[1:]]
}
for row in data[1:]:
    split_row = row.strip().split(",")
    covid["date"].append(split_row[0])
    covid["data"].append([float(n) for n in split_row[1:]])
