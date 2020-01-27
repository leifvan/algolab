#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdlib.h>
#include <random>
#include <tuple>

using namespace std;

int MAX_VAL = 100000;


tuple<int, int> find_triu_min(const vector<vector<int>> &mat) {
    int min_val = MAX_VAL;
    int min_i, min_j;
    for(int i = 0; i < (int)mat.size(); i++) {
        for(int j = i+1; j < (int)mat[i].size(); j++) {
            if(mat[i][j] < min_val) {
                min_val = mat[i][j];
                min_i = i;
                min_j = j;
            }
        }
    }
    return tuple<int, int>(min_i, min_j);
}

int main()
{
    int n, k, m;
	cin >> n;
	cin >> k;
	cin >> m;


	vector<vector<int>> dist_mat;
	vector<vector<int>> icd;

	vector<vector<int>> edges_i;

	for(int k = 0; k < n; k++) {
        vector<int> row(n, MAX_VAL);
        dist_mat.push_back(row);
        dist_mat[k][k] = 0;
        vector<int> edges;
        edges_i.push_back(edges);
	}

	for(int k = 0; k < m; k++) {
	    int i, j, w;
	    cin >> i;
	    cin >> j;
	    cin >> w;
	    dist_mat[i][j] = dist_mat[j][i] = w;
	    edges_i[i].push_back(j);
	    edges_i[j].push_back(i);
	}


	// dijkstra

	for(int s = 0; s < n; s++) {
	    vector<int> dist(n, MAX_VAL);
	    dist[s] = 0;
        vector<int> queue;
	    for(int k = 0; k < n; k++) {queue.push_back(k);}

	    sort(queue.begin(), queue.end(), [&dist](int v1, int v2){return dist[v1] < dist[v2];});

	    while(!queue.empty()) {
	        int u = queue.back();
	        queue.pop_back();
	        for(auto v : edges_i[u]) {
	            if(dist[u] + dist_mat[u][v] < dist[v]) {
	                dist[v] = dist[u] + dist_mat[u][v];
	                sort(queue.begin(), queue.end(), [&dist](int v1, int v2){return dist[v1] < dist[v2];});
	            }
	        }
	    }

	    icd.push_back(dist);
	}

    for(int r = 0; r < n-k; r++) {
        // find clusters with minimal dist
        tuple<int, int> coords = find_triu_min(icd);
        int i = get<0>(coords);
        int j = get<1>(coords);

        for(int k = 0; k < (int)icd.size(); k++) {
            icd[i][k] = icd[k][i] = min(icd[i][k], icd[j][k]);
        }

        for(int k = 0; k < (int)icd.size(); k++) {
            icd[k].erase(icd[k].begin() + j);
        }
        icd.erase(icd.begin() + j);
    }
    tuple<int, int> coords = find_triu_min(icd);
    int i = get<0>(coords);
    int j = get<1>(coords);
    cout << icd[i][j] << endl;
    return 0;
}