with open("/home/shrirang/test.csv") as fd:
    csv_dict = { line.strip(): line.strip() for line in fd.readlines() }

print csv_dict


