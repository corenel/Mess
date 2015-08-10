#include <iostream>
#include "Sales_item.h"

int main()
{
	Sales_item currItem, refItem;
	int cnt = 1;

	if (std::cin >> refItem)
	{
		while (std::cin >> currItem)
		{
			if (currItem.isbn() == refItem.isbn())
			{
				++cnt;
			}
			else
			{
				std::cout << refItem.isbn() << " occurs " << cnt << " times." << std::endl;
				refItem = currItem;
				cnt = 1;
			}
		}
	}
	else
	{
		std::cerr << "Data type error." << std::endl;
		return -1;
	}

	return 0;
}