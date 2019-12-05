#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <tuple>
#include <time.h>
#include <stdlib.h>
#include <cmath>
#include <valarray>
using namespace std;

typedef long long int int_type;
typedef tuple<int,int_type> indexed_int_type;

bool readIntoInt(vector<int_type>& point){

    int_type val;
    point.clear();

    string read;
    getline(cin, read); //can only read, if lines separate inputs
    read.erase(remove(read.begin(), read.end(), '.'), read.end());
    stringstream ss;
    ss << read;

    while(ss >> val){
        point.push_back(val);
    }

    if(point.size() == 0){
        return false;
    }

    return true;
}

bool tupleCompare(indexed_int_type left, indexed_int_type right){
    return get<1>(left) < get<1>(right);
}

int_type squaredDistance(vector<int_type>& vec) {
    valarray<int_type> vec_vals(vec.data(), vec.size());
    return pow(vec_vals, (long long int)2).sum();
}

void extractCandidates(vector<indexed_int_type>& centers, int_type point, vector<int>& candidates, int_type range){

    candidates.clear();
    indexed_int_type tmp = make_tuple(0, point);
    auto up_it = upper_bound(centers.begin(), centers.end(), tmp, tupleCompare);
    auto down_it = up_it;

    auto bound=range+point;
    while(up_it != centers.end()){
        if(std::get<1>(*up_it) <= bound){
            candidates.push_back(std::get<0>(*up_it));
            up_it++;
        }else{
            break;
        }
    }

    bound=point-range;
    while (down_it != centers.begin()){
        down_it--;
        if(std::get<1>(*down_it) >= bound){
            candidates.push_back(std::get<0>(*down_it));
        }else{
            break;
        }
    }

    //cout << "Number of candidates found: " << candidates.size() << "\n";

}

bool checkCandidate(vector<int_type>& candidate, vector<int_type>& point, int dimensions, int_type squaredRange, int ref){

    int_type currentSquaredDist = 0;
    int_type help;

    // check ref coordinate first
//    currentSquaredDist = candidate[ref] - point[ref];
//    currentSquaredDist += help * help;
//    if(currentSquaredDist > squaredRange) {
//        return false;
//    }

    for(int i = 0; i < dimensions; i++){
//        if(i != ref) {
            help = candidate[i] - point[i];
            currentSquaredDist += help * help;
            if(currentSquaredDist > squaredRange){
                return false;
            }
//        }
    }

    //cout << "Valid candidate found. \n";

    return true;
}

int main(){

    int dimensions;
    int_type range;
    bool flag;
    int index = 0;

    srand(time(0));
    cin >> dimensions;
    int ref = rand() % dimensions; //Dimension used to reduce candidates

    vector<int_type> point;
    indexed_int_type center;
    vector<vector<int_type>> centers;
    vector<int_type> centerDistances;
    vector<int> candidates;
    vector<indexed_int_type> dim1Sorted;

    point.resize(dimensions);

    int_type currentDistance;

    readIntoInt(point);
    range = point[0];
    int_type squaredRange = range * range;

    // currentDistance = sqrt(squaredDistance(point));

    while(!cin.eof()){

        if(!readIntoInt(point)){
            continue;
        }
        currentDistance = sqrt(squaredDistance(point));
        extractCandidates(dim1Sorted, point[ref], candidates, range);

        for(auto it : candidates){
            if(abs(centerDistances[it] - currentDistance) > range - 1) {
                continue;
            }
            flag = checkCandidate(centers[it], point, dimensions, squaredRange, ref);
            if(flag){
                break;
            }
        }

        if(!flag){
            center = make_tuple(index, point[ref]);
            centers.push_back(point);
            centerDistances.push_back(currentDistance);
            index++;
            dim1Sorted.insert(upper_bound(dim1Sorted.begin(), dim1Sorted.end(), center, tupleCompare), center);
        }

        flag = false;

        //cout << "Current number of centers: " << index << "\n";
        
    }

    cout << index;

    return 0;
}
