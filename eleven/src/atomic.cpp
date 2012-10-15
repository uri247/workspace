#include <thread>
#include <iostream>
#include <chrono>

void oob( void )
{
    //std::this_thread::sleep_for( std::chrono::seconds(2) );
}

void atomic( void )
{
    //std::thread(oob).detach();


}
