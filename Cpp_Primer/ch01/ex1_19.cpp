#include <iostream>
int main()
{
	int upper_limit = 0, lower_limit = 0;

	std::cout << "Enter two numbers and I will print integers bewteen them: "
			  << std::endl;
	std::cin >> lower_limit >> upper_limit;

	if (lower_limit > upper_limit) {
		int temp_val = upper_limit;
		upper_limit = lower_limit;
		lower_limit = temp_val;
	}

	while (lower_limit <= upper_limit) {
		std::cout << lower_limit << std::endl;
		++lower_limit;
	}
	
	return 0;
}