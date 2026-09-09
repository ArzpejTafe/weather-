import math

series_titles = [
    "Maximum temperature (Degree C)",
    "Minimum temperature (Degree C)",
    "Rainfall amount (millimetres)"
]


# -------------------------
# Statistics Functions
# -------------------------

def is_nonnull(x):
    return x is not None


def mean(in_series):

    in_series = filter(is_nonnull, in_series)

    series_sum = 0
    count = 0

    for item in in_series:
        series_sum += item
        count += 1

    if count == 0:
        return 0

    return series_sum / count


def variance(in_series):
    avg = mean(in_series)

    total = 0

    for value in in_series:
        total += (value - avg) ** 2

    return total / len(in_series)


def standard_deviation(in_series):
    return math.sqrt(variance(in_series))


def data_range(in_series):
    return max(in_series) - min(in_series)


def interquartile_range(in_series):

    data = sorted(in_series)

    q1_index = len(data) // 4
    q3_index = (len(data) * 3) // 4

    q1 = data[q1_index]
    q3 = data[q3_index]

    return q3 - q1


# -------------------------
# Date Filtering
# -------------------------

def filter_series(
    year_series,
    month_series,
    day_series,
    data_series,
    max_date=None,
    min_date=None
):

    filtered = []

    for i in range(len(data_series)):

        current_date = (
            int(year_series[i]),
            int(month_series[i]),
            int(day_series[i])
        )

        if min_date and current_date < min_date:
            continue

        if max_date and current_date > max_date:
            continue

        filtered.append(data_series[i])

    return filtered


# -------------------------
# Read CSV File
# -------------------------

def read_csv(file, default_value=0):

    data_table = {}

    with open(file) as f:
        lines = f.readlines()

    lines = [line.strip().split(',') for line in lines]

    for i in range(len(lines[0])):

        data_table[lines[0][i]] = [
            default_value if len(line[i]) == 0
            else float(line[i])
            if line[i].replace('.', '', 1).isdigit()
            else line[i]
            for line in lines[1:]
        ]

    return data_table


# -------------------------
# User Menu Functions
# -------------------------

def get_user_choice(options):

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    choice = input("Enter choice: ")

    if choice.lower() == "exit":
        return None

    return options[int(choice) - 1]


# -------------------------
# Main Menu
# -------------------------

def menu(data_table):

    while True:

        print("\nSelect Data Series")
        choice = get_user_choice(series_titles)

        if choice is None:
            print("Goodbye")
            break

        series = data_table[choice]

        print("\nSelect Statistic")

        stats = {
            "1": "Mean",
            "2": "Variance",
            "3": "Standard Deviation",
            "4": "Range",
            "5": "IQR"
        }

        for key, value in stats.items():
            print(f"{key}. {value}")

        stat_choice = input("Choice: ")

        if stat_choice == "1":
            print("Mean =", mean(series))

        elif stat_choice == "2":
            print("Variance =", variance(series))

        elif stat_choice == "3":
            print("Standard Deviation =", standard_deviation(series))

        elif stat_choice == "4":
            print("Range =", data_range(series))

        elif stat_choice == "5":
            print("IQR =", interquartile_range(series))

        else:
            print("Invalid option")


# -------------------------
# Temperature Range Feature
# -------------------------
def add_temperature_range(data_table):

    max_temp = data_table["Maximum temperature (Degree C)"]
    min_temp = data_table["Minimum temperature (Degree C)"]

    temp_range = []

    for i in range(len(max_temp)):

        try:
            max_value = float(max_temp[i])
            min_value = float(min_temp[i])

            temp_range.append(max_value - min_value)

        except:
            temp_range.append(0)

    data_table["Temperature Range"] = temp_range

#njhh
# -------------------------
#   ogram Start
# -------------------------
data = read_csv(r"C:\Users\20170213\Documents\session8\weather\weather.csv")


add_temperature_range(data)

menu(data)