#include <iostream>
#include <type_traits>


template <typename T>
struct identity {
	//using type = T;
	typedef T type;
};

template <typename T>
struct is_positive_for_unsigned {
	static bool positive( T x ) { return true; }
};


template <typename T>
typename std::enable_if< std::is_signed<T>::value, bool >::type positive( T& x ) {
	return x > 0;
}

template <typename T>
typename std::enable_if< std::is_unsigned<T>::value, bool >::type positive( T& x ) {
	return true;
}


/*
template <typename T>
struct is_positive_for_signed {
	static bool positive( T x ) { return x > 0; }
};

template <typename T>
using is_positive = typename std::conditional< std::is_signed<T>::value,
		is_positive_for_signed<T>, is_positive_for_unsigned<T> >::type;


template< typename T >
bool positive( T x ) {
    return is_positive<T>::positive( x );
}
*/


/*
template <typename T>
struct is_positive {
    typedef std::conditional< std::is_signed<T>::value,
    		is_positive_for_signed<T>, is_positive_for_unsigned<T> > type;
    static bool positive( T x ) { return type::positive(x); }
};
*/


void moretraits( unsigned input )
{
	int x = input;
	unsigned y = input;
	bool xpos, ypos;

    xpos = positive(x);
    ypos = positive(y);
	std::cout << "x is positive? " << ( xpos ? "yes" : "no" ) << std::endl;
	std::cout << "y is positive? " << ( ypos ? "yes" : "no" ) << std::endl;

    xpos = x>0;
    ypos = y>0;
	std::cout << "x is positive? " << ( xpos ? "yes" : "no" ) << std::endl;
	std::cout << "y is positive? " << ( ypos ? "yes" : "no" ) << std::endl;


}
