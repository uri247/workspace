#include <iostream>
#include <iomanip>
#include <typeinfo>

struct Base {
    virtual void met( ) { }
    virtual ~Base( ) { }
};
struct Record : public Base{
};

void method( Base* pbase )
{
	Record* prec;

    prec = static_cast<Record*>( pbase );
    std::cout << "static cast prec: " << prec << std::endl;

    prec = dynamic_cast<Record*>( pbase );
    std::cout << "dynamic cast prec: " << prec << std::endl;
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
    std::cout << "reinterpret cast: " << pdouble << std::endl;
}
