#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int n;
	cin >> n;

    int field[300][300];
    int p[300];
    int t;
    int M = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int v;
            cin >> v;
            field[i][j] = v;
        }
    }

	for (int g = 0; g < n; ++g) {
	    for (int j = 0; j < n; ++j) { p[j] = 0; }
	    for (int i = g; i < n; ++i) {
            t = 0;
            for (int j = 0; j < n; ++j) {
                p[j] += field[i][j];
                t += p[j];
                if (t > M) { M = t; }
                if (t <= 0) {
                    t = 0;
                }
            }
	    }
	}

	cout << M << endl;
	return 0;
}