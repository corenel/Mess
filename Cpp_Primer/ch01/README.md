# Exercise 1.6
The code is:

```
std::cout << "The sum of " << v1;
		  << " and " << v2;
		  << " is " << v1 + v2 << std:endl;
```

It's **illegal**!

GCC says:

```
ex1_6.cpp: In function ‘int main()’:
ex1_6.cpp:9:6: error: expected primary-expression before ‘<<’ token
      << " and " << v2;
      ^
ex1_6.cpp:10:6: error: expected primary-expression before ‘<<’ token
      << " is " << v1 * v2 << std::endl;
      ^
```

We can fix the bug by deleting semicolons in the first two line. Just like this:

```
std::cout << "The sum of " << v1
		  << " and " << v2
		  << " is " << v1 + v2 << std:endl;
```

ALL DONE!

# Exercise 1.7
```
	/* There are some wrong comments.
	/**/ CANNOT nest. 
	*/
```
GCC error message is 
```
ex1_7.cpp: In function ‘int main()’:
ex1_7.cpp:6:7: error: ‘CANNOT’ was not declared in this scope
  /* */ CANNOT nest. 
       ^
```

# Exercise 1.8
The original code is:

```
std::cout << "/*";
std::cout << "*/";
std::cout << /* "*/" */;
std::cout << /* "*/" /* "/*" */;
```

GCC error message is:

```
ex1_8.cpp:6:21: warning: missing terminating " character
  std::cout << /* "*/" */;
                     ^
ex1_8.cpp:6:2: error: missing terminating " character
  std::cout << /* "*/" */;
  ^
```

To correct the bug, just add a quote: 

```
std::cout << "/*";
std::cout << "*/";
std::cout << /* "*/" */";
std::cout << /* "*/" /* "/*" */;
```

And the output is:

```
/**/ */ /* 
```

# Exercise 1.12
```
int sum = 0;
for (int i = -100; i <= 100; ++i)
  sum += i;
```

Calculate sum of -100 to 100.

And the sum is 0.

# Exercise 1.14

> Compare and contrast the loops that used a for with those using a while. Are there advantages or disadvantages to using either form?

If you need a variable to increace from a number to another in the body, you should use `for` loop. If not, `while` loop.

# Exercise 1.15

> Write programs that contain the common errors discussed in the box on page 16. Familiarize yourself with the messages the compiler generates.

JUST READ IT!

# Exercise 1.17

> What happens in the program presented in this section if the input values are all equal? What if there are no duplicated values?

If the input values are all equal, the output will be only a  line to show the count of the number.

If there are no duplicated values, there are lines whose amount is just the same as amount of the numbers you input.

# Exercise 1.18

> Compile and run the program from this section giving it only equal values as input. Run it again giving it values in which no number is repeated.

```
yuthon@ubuntu:~/Github/Mess/Cpp_Primer/ch01$ ./a.out
12
12
12
12
12
12
12
12
12
12
^E
12 occurs 10times.
yuthon@ubuntu:~/Github/Mess/Cpp_Primer/ch01$ ./a.out
1
2
1 occurs 1times.
3
2 occurs 1times.
4
3 occurs 1times.
5
4 occurs 1times.
6
5 occurs 1times.
7
6 occurs 1times.
8
7 occurs 1times.
9
8 occurs 1times.
^E
9 occurs 1times.
```
