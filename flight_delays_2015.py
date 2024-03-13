import csv
import matplotlib.pyplot as plt

with(open("flights.csv", encoding='iso-8859-1')) as f:
    flights = list(csv.reader(f, delimiter=","))

def visualize_by_src_airport():
    delays = {}
    for flight in flights[1:]:
        ...

def visualize_by_month():
    delays = {}
    for flight in flights[1:]:
        try:
            if int(flight[3]) > 0:
                try:
                    delays[flight[0]] = int(delays[flight[0]]) + int(flight[3])
                except KeyError:
                    delays[flight[0]] = int(flight[3])
        except:
            continue
    return list(delays.keys()), (delays.values())

xs, ys = visualize_by_month()


months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
plt.figure(figsize = (16, 6))
plt.bar(list(months.values()), ys)
# # Show plot
plt.show()