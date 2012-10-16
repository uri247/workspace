#include <iostream>
#include <vector>
#include <string>


int main()
{
        std::vector<std::string> words;
        words.push_back( "Hello" );
        words.push_back( "world" );
        words.push_back( "!!" );

        for( auto& s : words ) {
                std::cout << s << " ";
        }
        std::cout << std::endl;
}
