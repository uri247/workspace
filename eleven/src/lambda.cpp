#include <iostream>
#include <ostream>
#include <iomanip>
#include <functional>
#include <vector>
#include <algorithm>

template<typename T>
std::ostream& operator<< ( std::ostream& os, std::vector<T> const& col )
{
	bool first = true;

	for( auto& i : col ) {
		if( first ) first = false; else os << ", ";
		os << i;
	}
	return os;
}

void lambda( void )
{
	std::vector<int> v { -20, 10, 40, -50, -30 };

	std::cout << "unsorted\n" << v << std::endl;

	std::sort( v.begin(), v.end(), [](int x, int y) { return x < y; } );
	std::cout << "regular sort\n" << v << std::endl;

	std::sort( v.begin(), v.end(), [](int x, int y) { return abs(x) < abs(y); } );
	std::cout << "absolute sort\n" << v << std::endl;
}
