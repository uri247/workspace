#include <iostream>
#include <iomanip>
#include <memory>
#include <functional>

/*
void mydel( void* ptr )
{
    std::cout << "delete the ptr";
}
*/



class AA
{
public:
    char* alloc( size_t size )            { return new char[size]; }
    void free( char* ptr, int size )      { return delete[] ptr; }
};



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


void rawmem( void )
{
	std::allocator<char> al;
    raw_memory<> raw( 42 );
}
