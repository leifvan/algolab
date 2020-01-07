#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdlib.h>
#include <random>
#include <sstream>

using namespace std;

struct Query
{
    int query;
    int val;

    Query(int q, int v) : query(q), val(v) {}
    Query() : query(0), val(0) {}
};


void printQueries(const vector<Query> &queries) {
    for(auto tup : queries) {
        cout << tup.query << "," << tup.val << endl;
    }
    cout << "----" << endl;
}

int main()
{
    int n;
    cin >> n;
    cin >> ws;

    vector<string> names;
    vector<Query> queries;

    for(int i = 0; i < n; i++)
    {
        string input;
        getline(cin,input);
        stringstream input_stringstream(input);

        string name;
        int query = 0;

        int lineLength = 0;
        for(unsigned int j = 0; j < input.size(); j++) {
            if(input.at(j) == ' ') {lineLength++;}
        }

        for(int j = 0; j < lineLength; j++) {
            getline(input_stringstream, name, ' ');
            int pos = -1;
            vector<string>::iterator posIter = find(names.begin(), names.end(), name);
            if(posIter == names.end()) { // does not exist
                names.push_back(name);
                pos = names.size()-1;
            } else {
                pos = distance(names.begin(), posIter);
            }
            query |= 1 << pos;
        }

        string lastWord;
        getline(input_stringstream, lastWord, ' ');
        int val = (lastWord == "odd");
        queries.push_back(Query(query, val));
    }

    // printQueries(queries);

    int position = 1 << n;
    int j = 0;
    for(int i = 0; i < n; i++)
    {
        position >>= 1;
        j = i;
        while(!(queries.at(j).query & position) && j < n-1) {j++;}
        swap(queries.at(i), queries.at(j));
        Query tupi = queries.at(i);
        for(int j = i+1; j < n; j++) {
            Query tupj = queries.at(j);
            if(tupj.query & position) {
                queries.at(j) = Query(tupi.query ^ tupj.query, tupi.val ^ tupj.val);
            }
        }
    }

    // printQueries(queries);

    int friends = 0;
    for(int i = n-1; i > -1; i--)
    {
        Query tupi = queries.at(i);
        friends += tupi.val;
        for(int j = 0; j < i; j++)
        {
            Query tupj = queries.at(j);
            if(tupj.query & position) {
                queries.at(j).val = tupi.val ^ tupj.val;
            }
        }
        position <<= 1;
    }

    // printQueries(queries);

    cout << friends << endl;
}