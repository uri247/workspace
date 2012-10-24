#include <iostream>
#include <cstdio>
#include <tuple>
#include <array>
#include <utility>
#include <type_traits>

template<int I1> struct test1 { };
template<int I1, int I2> struct test2 { };
template<int I1, int I2, int I3> struct test3 { };

test1<1> bldind1() { return {}; }
test2<1,2> bldind2() { return {}; }
test3<1,2,3> bldind3() { return {}; }



template<int... Indices>
struct indices {
	using next = indices<Indices..., sizeof...(Indices)>;
};

template<int Size>
struct build_indices {
	using type = typename build_indices<Size-1>::type::next;
};

template<>
struct build_indices<0> {
	using type = indices<>;
};

template<typename T>
using Bare = typename std::remove_cv<typename std::remove_reference<T>::type>::type;

template<typename Tuple>
constexpr
typename build_indices<std::tuple_size<Bare<Tuple>>::value>::type
make_indices()
{
	return {};
}

template< typename Tuple, int... Indices>
std::array<
    typename std::tuple_element<0, Bare<Tuple>>::type,
    std::tuple_size<Bare<Tuple>>::value
    >
to_array( Tuple&& tuple, indices<Indices...> )
{
	return {
		{ std::get<Indices>( std::forward<Tuple>(tuple))... }
	};
}

template< typename Tuple >
auto to_array( Tuple&& tuple )
-> decltype( to_array( std::declval<Tuple>(), make_indices<Tuple>() ) )
{
	return to_array( std::forward<Tuple>(tuple), make_indices<Tuple>() );
}

void tuple2array( )
{
	std::tuple<double,double,double> tup( 1.5, 2.5, 4.5 );
	auto arr = to_array( tup );
	for( double& x : arr ) {
		std::cout << x << std::endl;
	}
}

