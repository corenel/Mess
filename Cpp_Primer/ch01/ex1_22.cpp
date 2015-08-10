#include <iostream>
#include "Sales_item.h"

int main()
{
	Sales_item total;

	if (std::cin >> total)
	{
		Sales_item item;

		while (std::cin >> item)
		{
			if (item.isbn() == total.isbn())
				total += item;
			else
			{
				std::cout << total << std::endl;
				total = item;
			}
		}
		std::cout << total << std::endl;
	}
	else
	{
		std::cerr << "Data type error." << std::endl;
		return -1;
	}

	return 0;
}