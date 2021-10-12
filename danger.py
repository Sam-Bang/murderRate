import csv
from geopy.geocoders import Nominatim
import time
from pprint import pprint
import geocoder
import os

citylist = []
statelist = []
murderlist = []

currentDir = os.getcwd()

with open(currentDir+'\murder_2016_prelim.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    iterrow = iter(readCSV)
    next(iterrow)

    for row in iterrow: #add the city, state, and murder amounts to lists each
        citylist.append(row[0])
        statelist.append(row[1])
        murderlist.append(int(row[2]))
def bubble_sort(our_list, citylist, statelist):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                citylist[j], citylist[j+1] = citylist[j+1], citylist[j]
                statelist[j], statelist[j+1] = statelist[j+1], statelist[j]

bubble_sort(murderlist, citylist, statelist)

app = Nominatim(user_agent="tutorial")

def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)
# define your coordinates
myloc = geocoder.ip('me')
myList = myloc.latlng
latitude = myList[0]
longitude = myList[1]
# get the address info
address = get_address_by_location(latitude, longitude)
# print all returned data
print("You live in",address["address"]["city"])
city = address["address"]["city"]
citylength = len(citylist)
i = 0
found = False
while i < citylength:
    if city == citylist[i]:
        print(citylist[i],"has had", murderlist[i], "murders in 2015")
        found = True
        if i < 26:
            print(citylist[i], "is a mild danger city")
        if i >= 26 & i <= 52:
            print(citylist[i], "is a medium danger city") 
        if i > 52:
            print(citylist[i], "is a high danger city")
    i = i + 1

if found == False:
    print("You don't live in one of the top 79 murder rate cities")