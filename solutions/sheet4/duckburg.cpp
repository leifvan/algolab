#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;


float cc(const vector<int> &x, const int i, const int j, const vector<int> &prefix_sums)
{
    float m_ij = (j+i)/2;
    int fm_ij = floor(m_ij);
    float mu_ij = (x[fm_ij] + x[ceil(fm_ij)]) / 2;
    return (2*fm_ij - i - j + 1)*mu_ij - 2*prefix_sums[fm_ij+1] + prefix_sums[i] + prefix_sums[j+1];
}

int main()
{
    int k, n;
    cin >> k;
	cin >> n;

    vector<int> x(n,0);
    vector<int> prefix_sums(n+1,0);

    for(int i = 0; i < n; i++) { cin >> x[i]; }

    sort(x.begin(), x.end());

    for(int i = 0; i < n; i++)
    {
        cin >> x[i];
        for(int j = i; j < n; j++) {
            prefix_sums[j+1] += x[i];
        }
    }

    vector<float> lastD(n,0);
    vector<float> curD(n,0);

    for(int m = 0; m < n; m++) {
        lastD[m] = cc(x, 0, m, prefix_sums);
    }

    for(int i = 1; i < k; i++) {
        for(int m = 1; m < n; m++) {
            float curVal;
            float minVal = 10000*n;
            for(int j = 1; j < min(m+1,n); j++) {
                curVal = lastD[j-1] + cc(x, j, m, prefix_sums);
                if(curVal < minVal) { minVal = curVal; }
            }
            curD[m] = minVal;
        }
        curD[0] = 0;
        for(int m = 0; m < n; m++) { lastD[m] = curD[m]; }
    }

    int result = 25 * n - lastD[n-1];
    cout << result << endl;
	return 0;
}