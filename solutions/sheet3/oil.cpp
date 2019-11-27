#include <iostream>
#include <vector>
#include <array>
#include <iomanip>

using namespace std;

int main()
{
    array<array<int, 301>, 301> field;
    array<array<int, 301>, 301> maxfield;
//    int field[301][301];
//    int maxfield[301][301];
	int n;
	cin >> n;

	int minval = 100*300*300;
	int maxval = -100*300*300;

    // we can integrate the values while reading
	for (int i = 0; i < n+1; ++i) {
	    for (int j = 0; j < n+1; ++j) {
	        if (i == 0 || j == 0) {
	            field[i][j] = 0;
	        }
	        else {
                int v;
                cin >> v;
                if (v < minval) {
                    minval = v;
                }
                if (v > maxval) {
                    maxval = v;
                }
                field[i][j] = v + field[i-1][j] + field[i][j-1] - field[i-1][j-1];
            }
	    }
	}

	// make a map of max values right & below position
	for (int i = n; i >= 0; --i) {
	    for (int j = n; j >= 0; --j) {
	        maxfield[i][j] = field[i-1][j-1] + field[i][j] - field[i-1][j] - field[i][j-1];
	        if (i < n && maxfield[i+1][j] > maxfield[i][j]) {
	            maxfield[i][j] = maxfield[i+1][j];
	        }
	        if (j < n && maxfield[i][j+1] > maxfield[i][j]) {
	            maxfield[i][j] = maxfield[i][j+1];
	        }
//	        cout << i << "," << j << " " << maxfield[i][j] << endl;
	    }
	}

    int max_augmented = 0;
	int val = 0;
	int maxprofit = -100*300*300;
	for (int i1 = 1; i1 < n+1; ++i1) {
	    max_augmented = maxfield[i1][1];
        if (maxprofit > max_augmented && max_augmented <= 0) { break; }

	    for (int j1 = 1; j1 < n+1; ++j1) {
//	        max_augmented = maxfield[i1][j1];
//	        if (maxprofit > max_augmented && max_augmented <= 0) { break; }

	        for (int i2 = i1; i2 < n+1; ++i2) {
	            for (int j2 = j1; j2 < n+1; ++j2) {
                    max_augmented = max(maxfield[i2][j1], maxfield[i1][j2]);
//                    if (maxprofit > max_augmented && max_augmented <= 0) {
//                        cout << maxprofit << endl;
//                        return 0;
//                    }

	                val = field[i1-1][j1-1] + field[i2][j2] - field[i1-1][j2] - field[i2][j1-1];
	                if (val > maxprofit) {
	                    maxprofit = val;
	                }
//	                max_augmented = val + maxfield[i2][j2]*(n-i2+1)*(n-j2+1) + maxfield[i1][j2] * (i2-i1+1) * (n-j2+1) + maxfield[i2][j1] * (n-i2+1) *(j2-j1+1);
//	                if (max_augmented <= maxprofit) { break; }

	            }
	        }
	    }
	}
	cout << maxprofit << endl;
	return 0;
}

