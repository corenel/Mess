# Introduction
This is a implemtntation of Welsh-Powell method for graph coloring by Corenel Pan
# Usage
* First, you should input the number of nodes.
* Second, input names of those nodes.
* Last, input the relationship of those nodes (Stop with EOF). Especially in Powershell, you can press 'Ctrl+Z'.

# Example
'''
PS D:\GitHub> python .\graphColoring.py
Please input the number of nodes:
8
Please input the name of Node 0
C1
Please input the name of Node 1
C2
Please input the name of Node 2
C3
Please input the name of Node 3
C4
Please input the name of Node 4
C5
Please input the name of Node 5
C6
Please input the name of Node 6
C7
Please input the name of Node 7
C8
Please input the relationship of nodes (Stop with EOF):
C1 C3
Please input the relationship of nodes (Stop with EOF):
C1 C4
Please input the relationship of nodes (Stop with EOF):
C1 C5
Please input the relationship of nodes (Stop with EOF):
C1 C7
Please input the relationship of nodes (Stop with EOF):
C1 C8
Please input the relationship of nodes (Stop with EOF):
C2 C4
Please input the relationship of nodes (Stop with EOF):
C2 C6
Please input the relationship of nodes (Stop with EOF):
C2 C7
Please input the relationship of nodes (Stop with EOF):
C3 C5
Please input the relationship of nodes (Stop with EOF):
C3 C7
Please input the relationship of nodes (Stop with EOF):
C3 C8
Please input the relationship of nodes (Stop with EOF):
C4 C7
Please input the relationship of nodes (Stop with EOF):
C5 C6
Please input the relationship of nodes (Stop with EOF):
C5 C7
Please input the relationship of nodes (Stop with EOF):
C5 C8
Please input the relationship of nodes (Stop with EOF):
^Z
Calculating the degree of node C1
The degree is 5
Calculating the degree of node C2
The degree is 3
Calculating the degree of node C3
The degree is 4
Calculating the degree of node C4
The degree is 3
Calculating the degree of node C5
The degree is 5
Calculating the degree of node C6
The degree is 2
Calculating the degree of node C7
The degree is 5
Calculating the degree of node C8
The degree is 3
Neighboor node: (name=C1, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C3, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C5, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C2, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C4, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Remianing colors are  set([1, 2, 3, 4, 5])
Chosen color for (name=C7, color=NO COLOR) is CPLOR 1
Neighboor node: (name=C1, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C3, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C6, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C8, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C7, color=CPLOR 1)
Colors: set([1, 2, 3, 4, 5])
Remianing colors are  set([2, 3, 4, 5])
Chosen color for (name=C5, color=NO COLOR) is CPLOR 2
Neighboor node: (name=C3, color=NO COLOR)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C5, color=CPLOR 2)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C4, color=NO COLOR)
Colors: set([1, 3, 4, 5])
Neighboor node: (name=C8, color=NO COLOR)
Colors: set([1, 3, 4, 5])
Neighboor node: (name=C7, color=CPLOR 1)
Colors: set([1, 3, 4, 5])
Remianing colors are  set([3, 4, 5])
Chosen color for (name=C1, color=NO COLOR) is CPLOR 3
Neighboor node: (name=C1, color=CPLOR 3)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C5, color=CPLOR 2)
Colors: set([1, 2, 4, 5])
Neighboor node: (name=C8, color=NO COLOR)
Colors: set([1, 4, 5])
Neighboor node: (name=C7, color=CPLOR 1)
Colors: set([1, 4, 5])
Remianing colors are  set([4, 5])
Chosen color for (name=C3, color=NO COLOR) is CPLOR 5
Neighboor node: (name=C1, color=CPLOR 3)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C3, color=CPLOR 5)
Colors: set([1, 2, 4, 5])
Neighboor node: (name=C5, color=CPLOR 2)
Colors: set([1, 2, 5])
Remianing colors are  set([1, 5])
Chosen color for (name=C8, color=NO COLOR) is CPLOR 1
Neighboor node: (name=C1, color=CPLOR 3)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C7, color=CPLOR 1)
Colors: set([1, 2, 4, 5])
Neighboor node: (name=C2, color=NO COLOR)
Colors: set([2, 4, 5])
Remianing colors are  set([2, 4, 5])
Chosen color for (name=C4, color=NO COLOR) is CPLOR 2
Neighboor node: (name=C7, color=CPLOR 1)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C6, color=NO COLOR)
Colors: set([2, 3, 4, 5])
Neighboor node: (name=C4, color=CPLOR 2)
Colors: set([2, 3, 4, 5])
Remianing colors are  set([3, 4, 5])
Chosen color for (name=C2, color=NO COLOR) is CPLOR 3
Neighboor node: (name=C5, color=CPLOR 2)
Colors: set([1, 2, 3, 4, 5])
Neighboor node: (name=C2, color=CPLOR 3)
Colors: set([1, 3, 4, 5])
Remianing colors are  set([1, 4, 5])
Chosen color for (name=C6, color=NO COLOR) is CPLOR 1
[(name=C8, color=CPLOR 1), (name=C3, color=CPLOR 5), (name=C2, color=CPLOR 3), (name=C1, color=CPLOR 3), (name=C7, color
=CPLOR 1), (name=C6, color=CPLOR 1), (name=C5, color=CPLOR 2), (name=C4, color=CPLOR 2)]
'''
