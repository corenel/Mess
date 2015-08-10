#include <iostream>
#include "Sales_item.h"

int main()
{
	Sales_item item_1, item_2;

	std::cin >> item_1 >> item_2;
	if (item_1.isbn() == item_2.isbn())
	{
		std::cout << item_1 + item_2 << std::endl;
	}
	else
	{
		std::cerr << "Data must refer to same ISBN." << std::endl;
	}

	return 0;
}