//Mutating Algorithms - 2004 C. S. Germany

//Mutating sequence algorithms perform operations that change elements in a sequence.
//An example is fill().  Filling the elements in a sequence with a given value changes them:

//---------------------------------------------------------------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//---------------------------------------------------------------------------------------------------------------------------

template<class T>

//---------------------------------------------------------------------------------------------------------------------------

class PrintMe
{
public:
	void operator()(const T & t)
	{
		cout << t << " ";
	}
};

//---------------------------------------------------------------------------------------------------------------------------

int main()
{
	PrintMe<int>	PrintThis;
	vector<int>	vInt(10);
	fill(vInt.begin(), vInt.begin() + 5, 1);
	fill(vInt.begin() + 5, vInt.end(), 2);
	for_each(vInt.begin(), vInt.end(), PrintThis);
	cout << "\n\n";
	return 0;
}

//---------------------------------------------------------------------------------------------------------------------------









