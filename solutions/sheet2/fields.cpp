#include <iostream>
#include <bitset>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int r;
	cin >> r;

	vector<bitset<2000>> rows(r);

	for(int i=0; i < r; i++) {
	    string bits;
	    cin >> bits;

	    bitset<2000> cbs(bits);
	    rows.at(i) = cbs;
	}

	long long int count = 0;

	for(int a=0; a < r; a++) {
	    for(int b=a+1; b<r; b++) {
	        long long int num = (rows[a] & rows[b]).count();
	        count += (num-1)*num/2;
	    }
	}

	cout << count << endl;
	return 0;
}