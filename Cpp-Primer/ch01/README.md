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
