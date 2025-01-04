# Integer type sets

#student_rollnumber={1,2,3,4,5,6,7,8}
#print("Student Roll Number",student_rollnumber)

#vowels={'a','e','i','o','u'}
#print("Set of vowels:",vowels)

#-----------------------------------------------------------------------------#

#set of mixed data types

#mixed_set={'Hello',101,-2,'Bye'}
#print('Set of mixed data types:',mixed_set)

#--------------------------------------------------------------------#

#Create empty set
#empty_set=set()
#print("data type:",type(empty_set))

#-------------------------------------------------------------------#

#Duplicate item in set

#numbers={1,2,3,4,6,8,9,4,3,6,8}
#print(numbers)

#-------------------------------------------------------------#

#Add items in set

#numbers={1,2,3,4,5,6,7,8,9}
#numbers.add(10)
#print("New set:",numbers)

#--------------------------------------------------------------#

#Update sets

#companies={"TCS","Infosys"}
#Top_companies={"Apple","Google","Amazon"}

#Update methode

#companies.update(Top_companies)
#print(companies)

#-----------------------------------------------------------#

#remove element from set

#lang={"java","python","c++"}
#removed_value=lang.discard("java")
#print(lang)
#print(len(lang))


#-----------------------------------------------------------------#

#Union of two sets

A={1,2,3,7,8}
B={4,5,6,7,8}
#print(A|B)
#print(A.union(B))

#intersection of set

#print(A&B)
#print(A.intersection(B))

#set difference

#print(A-B)
#print(B-A)

#symetric difference which gives all number except common number

#print(A^B)
