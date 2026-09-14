def format_report(items, title):
    result = title + "\n"
    for i in items:
        result = result + "- " + str(i) + "\n"
    return result


def parse_csv_line(line):
    parts = line.split(",")
    d = {}
    d["a"] = parts[0]
    d["b"] = parts[1]
    d["c"] = parts[2]
    return d
