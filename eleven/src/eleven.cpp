#include <iostream>
#include <iomanip>
#include <memory>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
using namespace std;

void combo( void ) {
	vector<int> v { 1, 2, 3, 4, 5, 6, 7 };
	int x {5};
	auto mark = remove_if( v.begin(), v.end(), [x](int n) { return n<x; } );
	v.erase( mark, v.end() );
	for( int x : v ) { cout << x << ", "; }
	cout << endl;
}


struct Base {
    virtual void met( ) { }
};
struct Record : public Base{
};

void method( Base* pbase )
{
	Record* prec;

    prec = static_cast<Record*>( pbase );
    cout << "static cast prec: " << prec << endl;

    prec = dynamic_cast<Record*>( pbase );
    cout << "dynamic cast prec: " << prec << endl;
}

void casting( void )
{
	Record record;
	Base& ref = record;
    std::cout << "type of ref: " << typeid(ref).name() << std::endl;

    Base base;
    method( &base );

    // static_cast and dynamic_cast will not compile. reinterpret_cast
    // compiles fine, but runtime unpredictable
    int x = 3;
    int* pint = &x;
    double* pdouble;
    //pdouble = static_cast<double*>(pint);
    //pdouble = dynamic_cast<double*>(pint);
    pdouble = reinterpret_cast<double*>(pint);
    cout << "reinterpret cast: " << pdouble << endl;
}


void mydel( void* ptr )
{
    std::cout << "delete the ptr";
}

template< class A = std::allocator<char> >
class raw_memory
{
private:
	A m_al;
	std::unique_ptr< char, std::function<void(char*)> > m_buffer;

public:
    raw_memory( size_t size, const A& al = A() )
        :m_al(al)
        ,m_buffer( m_al.allocate(size), [this,size](char* ptr){ m_al.deallocate(ptr,size); } )
    {}
};


class A
{
public:
    char* alloc( size_t size )            { return new char[size]; }
    void free( char* ptr, int size )      { return delete[] ptr; }
};

void rawmem( )
{
	std::allocator<char> al;
    raw_memory<> raw( 42 );
}


int main( int argc, char* argv[] )
{
	combo( );
	casting( );
	rawmem( );
	return 0;
}
