#include <iostream>
#include <iomanip>
#include <utility>


void fn( int&& n ) { std::cout << "rvalue fn, n=" << n << std::endl; n = 0; }
void fn( int& n ) { std::cout << "lvalue fn, n=" << n << std::endl; }

template< class T >
void wrap( T&& t )
{
	std::cout << "bare - ";
	fn( t );
	std::cout << "fwd - ";
	fn( std::forward<T>( t ) );
}

void deducing( )
{
	int i=1;
	int& k = i;
	fn( k );
}



void do_util( )
{
	deducing( );
}
