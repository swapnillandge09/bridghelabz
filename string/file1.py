# f = open("demo.txt","r")
# data = f.read()
# #line1 = f.readline()
# #line2 = f.readline()
# #print(line1)
# #print(line2)
# print(data)
# print(type(data))    
# f.close()  
import csv

# # Data to be written to the CSV file
# data = [
#     ['Name', 'Age', 'City'],
#     ['Shubh', 28, 'Delhi'],
#     ['Alex', 22, 'New York'],
#     ['Mia', 32, 'London']
# ]

# # Write data to a CSV file
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

data = [
    ['name','age','city'],
    ['sam',22,'pune'],
    ['ram',33,'mumbai'],
    ['jon',23,'nashik']
]
with open('sample.csv','w', newline='') as file:
    writer= csv.writer(file)
    writer.writerows(data)

data1 = [
    ['name','age','city'],
    ['sam',22,'pune'],
    ['ram',33,'mumbai'],
    ['jon',23,'nashik']
]
with open("output.csv",'a',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data1)    