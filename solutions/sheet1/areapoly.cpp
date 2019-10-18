#include <algorithm>
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
	vector<int> x, y;

	int n;
	cin >> n;
    x.reserve(n);
    y.reserve(n);

	for (int i = 0; i < n; ++i) {
		int vx, vy;
		cin >> vx;
        cin >> vy;

		x.push_back(vx);
        y.push_back(vy);
	}

	// calc area
    float vol = 0;
    for (int i = 1; i < n; ++i) {
        vol += (x[i-1]+x[i])*(y[i-1]-y[i]);
    }
    vol += (x[n-1]+x[0])*(y[n-1]-y[0]);

	//output
    
    cout << std::fixed << std::setprecision(1) << float(vol) / 2. << endl;

	return 0;
}

