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

//	for(int s = 0; s < n; s++) {
//	    vector<int> dist(n, MAX_VAL);
//	    dist[s] = 0;
//
//	    for(int j = 0; j < n; j++) {
//	        int u = j;
//	        for(auto v : edges_i[u]) {
//	            if(dist[u] + dist_mat[u][v] < dist[v]) {
//	                dist[v] = dist[u] + dist_mat[u][v];
//	            }
//	        }
//	    }
//	    icd.push_back(dist);
//	}
//
//	dist_mat = icd;

	// slink

	// just walk over all edges because they have smallest distance

	vector<int> nearest_vertex(n, 0);
	vector<int> nearest_distance(n, MAX_VAL);

	for(int i = 0; i < n; i++) {
	    int minpos = 0;
	    int minval = MAX_VAL;
	    for(int j = 0; j < n; j++) {
	        if(i != j && dist_mat[i][j] < minval) {
	            minval = dist_mat[i][j];
	            minpos = j;
	        }
	    }
	    nearest_vertex[i] = minpos;
	    nearest_distance[i] = minval;
	}

	for(int r = 0; r < n-k; r++) {
	    // find min pair
	    auto miniter = min_element(nearest_distance.begin(), nearest_distance.end());
	    int i = distance(nearest_distance.begin(), miniter);
	    int j = nearest_vertex[i];

	    // merge i,j into i
	    int new_nvert = -1;
	    int new_ndist = MAX_VAL;
	    for(int k = 0; k < n; k++) {
	        dist_mat[i][k] = dist_mat[k][i] = min(dist_mat[i][k], dist_mat[j][k]);
	        dist_mat[j][k] = dist_mat[k][j] = MAX_VAL;

	        if(i != k && j != k && dist_mat[i][k] < new_ndist){
	            new_ndist = dist_mat[i][k];
	            new_nvert = k;
	        }

	        if(nearest_vertex[k] == j) {
	            nearest_vertex[k] = i;
	        }
	    }
	    nearest_vertex[i] = new_nvert;
	    nearest_distance[i] = new_ndist;

	    dist_mat[i][j] = MAX_VAL;
	    nearest_vertex[j] = -1;
	    nearest_distance[j] = MAX_VAL;
	}

	int minval = MAX_VAL;
	for(int k = 0; k < n; k++) {
	    if(nearest_distance[k] < minval) {
	        minval = nearest_distance[k];
	    }
	}
	cout << minval << endl;
    return 0;
}