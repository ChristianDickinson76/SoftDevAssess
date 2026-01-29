
customerListMonthOne = [
    "Ali", "Ben", "Ali", "Dana", "Cara", "Ben"
]

customerListMonthTwo = [
    "Ali", "Ella", "Ben", "Frank", "Cara", "Ben"
]

bookingData = [
    ("Ali", "StationA", "Weekday", 2),
    ("Ben", "StationB", "Weekend", 1),
    ("Ali", "StationA", "Weekday", 3),
    ("Cara", "StationC", "Weekday", 2),
    ("Ella", "StationB", "Weekend", 2)
]

loyalCustomers = {"Ali", "Cara"}

setMonthOne = set(customerListMonthOne)
setMonthTwo = set(customerListMonthTwo)

uniqueCustomers = setMonthTwo.union(setMonthOne)

regularCustomers = setMonthOne.intersection(setMonthTwo)
newCustomers = setMonthTwo.difference(setMonthOne)
inactiveCustomers = setMonthOne.difference(setMonthTwo)

print("Booking Records:")
for booking in bookingData:
    customer, station, dayType, hours = booking
    print(f" - {customer} | {station} | {dayType} | {hours}h")
print()

customerHours = {}

for customer, station, dayType, hours in bookingData:
    customerHours[customer] = customerHours.get(customer, 0) + hours

stationActivity = {}

for _, station, _, _ in bookingData:
    stationActivity[station] = stationActivity.get(station, 0) + 1

busiestStation = max(stationActivity, key=stationActivity.get)

customerHoursList = list(customerHours.items())
stationSet = set(stationActivity.keys())


print("Final Report\n")

print(f"Total Unique Customers This Month: {len(uniqueCustomers)}\n")

print("Regular Customers (Both Months):")
print(sorted(regularCustomers), "\n")

print("New Customers (This Month Only):")
print(sorted(newCustomers), "\n")

print("Inactive Customers (Did Not Return):")
print(sorted(inactiveCustomers), "\n")

print("Station Activity Summary:")
for station, count in stationActivity.items():
    print(f" - {station}: {count} bookings")
print()

print(f"Busiest Station: {busiestStation}\n")

print("Customer Hours Cycled:")
for customer, hours in customerHours.items():
    print(f" - {customer}: {hours} hours")
print()