#include <iostream>
#include <iomanip>
#include <utility>


void fn( int&& n ) { std::cout << "rvalue fn, n=" << n << std::endl; n = 0; }
void fn( int& n ) { std::cout << "lvalue fn, n=" << n << std::endl; }
// void fn( const int n ) { std::cout << "const fn, n=" << n << std::endl; }
// void fn( const int& n ) { std::cout << "const& fn, n=" << n << std::endl; }

template< class T >
void wrap( T&& t )
{
	std::cout << "bare - ";
	fn( t );
	std::cout << "fwd - ";
	fn( std::forward<T>( t ) );
}

void do_util( )
{
	int i=1;
	int& k = i;

	std::cout << "calling with int i:" << std::endl;
	wrap( i );

	std::cout << "calling with int& k:" << std::endl;
	wrap( k );

}
