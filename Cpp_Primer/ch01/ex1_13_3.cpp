#include <iostream>
int main()
{
	int upper_limit = 0, lower_limit = 0;

	std::cout << "Enter two numbers (lower and upper) and I will print integers bewteen them: "
			  << std::endl;
	std::cin >> lower_limit >> upper_limit;

	for (int i = lower_limit; i <= upper_limit; ++i) {
		std::cout << i << std::endl;
	}
	return 0;
}