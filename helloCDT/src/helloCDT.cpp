#include <iostream>
#include <vector>
#include <string>


int main()
{
        std::vector<std::string> words;
        words.push_back( "Hello" );
        words.push_back( "world" );
        words.push_back( "!!" );

        for( vector<string>::iterator i=words.begin(); i != words.end(); ++i ) {
                cout << *i << " ";
        }
        cout << endl;
}
