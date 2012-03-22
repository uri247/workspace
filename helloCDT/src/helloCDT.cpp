#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
        vector<string> words;
        words.push_back( "Hello" );
        words.push_back( "world" );
        words.push_back( "!!" );

        for( vector<string>::iterator i=words.begin(); i != words.end(); ++i ) {
                cout << *i << " ";
        }
        cout << endl;
}
