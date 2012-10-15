#include <iostream>
#include <iomanip>
#include <memory>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>


void casting( void );
void rawmem( void );
void moretraits( unsigned int input );

void combo( void ) {
	std::vector<int> v { 1, 2, 3, 4, 5, 6, 7 };
	int x {5};
	auto mark = remove_if( v.begin(), v.end(), [x](int n) { return n<x; } );
	v.erase( mark, v.end() );
	for( int x : v ) { std::cout << x << ", "; }
	std::cout << std::endl;
}



int main( int argc, char* argv[] )
{
	combo( );
	casting( );
	rawmem( );
    moretraits( 0xfffffffe );
	return 0;
}
