#include <iostream>
int main()
{
	int upper_limit = 0, lower_limit = 0;

	std::cout << "Enter two numbers (lower and upper) and I will print integers bewteen them: "
			  << std::endl;
	std::cin >> lower_limit >> upper_limit;

	int temp_val = lower_limit;
	while (temp_val <= upper_limit) {
		std::cout << temp_val << std::endl;
		++temp_val;
	}
	
	return 0;
}