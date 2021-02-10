from prettytable import prettytable

#open csv file

data_file = open("./Resources/cities.csv", 'r')

#read csv file named "cities"
data_file = data_file.readlines()


#separate the headers
l1 =data_file[0]
l1 =l1.split(',')

# headers for table 
t = PrettyTable([l1[0], l1[1]]) 

# Adding the data 
for i in range(1, len(a)) : 
    t.add_row(a[i].split(',')) 


code = t.get_html_string() 
html_file = open('Table.html', 'w') 
html_file = html_file.write(code)
