#max
#min
#round
# create own function

computers = {
"msi_rtxa5000_price": 4199.35,
"gigabyte_aero_price":4295.54,
"razer_blade15_price":3696.99,
"asus_zephyrus_m16_price":1849.79,
"asus_ROG":1249.99,
"asus_chromebook":99.00
}

print(max(computers.values()))
print(min(computers.values()))
for computer in computers.values():
    print(round(computer))

# avg = (sum of all the values) / (number of values)

add = sum(computers.values())
print(add)
summy = computers.__len__()
print(summy)

math = add / summy
print(math)