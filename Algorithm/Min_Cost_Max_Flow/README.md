# Introduction
This is a implemtntation of min cost max flow by Corenel Pan
# Usage
* First, you should input the number of nodes.
* Second, input names of those nodes and its demand.
* Last, input the relationship of those nodes and weight (Stop with EOF). Especially in Powershell, you can press 'Ctrl+Z'.

# Example
    Please input the number of nodes:
    10
    Please input the name of Node  0
    a -20
    Please input the name of Node  1
    b -34
    Please input the name of Node  2
    c -16
    Please input the name of Node  3
    d -23
    Please input the name of Node  4
    e 15
    Please input the name of Node  5
    f 18
    Please input the name of Node  6
    g 7
    Please input the name of Node  7
    h 29
    Please input the name of Node  8
    i 14
    Please input the name of Node  9
    j 10
    Please input the cost of nodes (Stop with EOF):
    e a 11.7
    Please input the cost of nodes (Stop with EOF):
    f a 13.2
    Please input the cost of nodes (Stop with EOF):
    g a 18.9
    Please input the cost of nodes (Stop with EOF):
    h a 4.8
    Please input the cost of nodes (Stop with EOF):
    i a 13.0
    Please input the cost of nodes (Stop with EOF):
    j a 14.3
    Please input the cost of nodes (Stop with EOF):
    e b 15.1
    Please input the cost of nodes (Stop with EOF):
    f b 14.0
    Please input the cost of nodes (Stop with EOF):
    g b 8.4
    Please input the cost of nodes (Stop with EOF):
    h b 20.1
    Please input the cost of nodes (Stop with EOF):
    i b 15.6
    Please input the cost of nodes (Stop with EOF):
    j b 12.0
    Please input the cost of nodes (Stop with EOF):
    e c 3.2
    Please input the cost of nodes (Stop with EOF):
    f c 5.0
    Please input the cost of nodes (Stop with EOF):
    g c 9.7
    Please input the cost of nodes (Stop with EOF):
    h c 4.2
    Please input the cost of nodes (Stop with EOF):
    i c 4.8
    Please input the cost of nodes (Stop with EOF):
    j c 7.3
    Please input the cost of nodes (Stop with EOF):
    e d 4.9
    Please input the cost of nodes (Stop with EOF):
    f d 7.1
    Please input the cost of nodes (Stop with EOF):
    g d 11.7
    Please input the cost of nodes (Stop with EOF):
    h d 3.8
    Please input the cost of nodes (Stop with EOF):
    i d 6.5
    Please input the cost of nodes (Stop with EOF):
    j d 7.3
    Please input the cost of nodes (Stop with EOF):
    ^Z
    691.0
    {'a': {'e': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 20, 'j': 0}, 'c': {'e': 13, 'g': 0, 'f': 1, 'i': 2, 'h': 0, 'j': 0}, 'b': {'
    e': 0, 'g': 7, 'f': 17, 'i': 0, 'h': 0, 'j': 10}, 'e': {}, 'd': {'e': 2, 'g': 0, 'f': 0, 'i': 12, 'h': 9, 'j': 0}, 'g':
    {}, 'f': {}, 'i': {}, 'h': {}, 'j': {}}
