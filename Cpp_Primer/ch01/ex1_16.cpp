#include <iostream>
int main()
{
	int sum = 0, val = 0;
	while (std::cin >> val) {
		sum += val;
	}
	std::cout << "The sum of these number is " << sum << "." << std::endl;
	return 0;
}