#include <iostream>
#include <utility>

struct A
{
    A( int&& n ) { std::cout << "rvalue constructor, n=" << n << "\n"; }
    A( int& n ) { std::cout << "lvalue constructor, n=" << n << "\n"; }
};

template< class T >
void foo( T&& t )
{
	A a( t );
}

void do_util( )
{
    foo( 2 );
    int i = 3;
    foo( i );
}
