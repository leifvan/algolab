#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdlib.h>
#include <random>

using namespace std;

typedef float coord_type;

struct Point
{
    coord_type x;
    coord_type y;

    Point(coord_type xv, coord_type yv) : x(xv), y(yv) {}
    Point() : x(0.), y(0.) {}
};

typedef vector<Point> Polygon;


int orientation(const Point p1, const Point p2, const Point p3)
{
    coord_type val = (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y);
    return val > 0 ? 1 : -1;
}

bool linesIntersect(const Point p1, const Point p2, const Point q1, const Point q2)
{
    int o1 = orientation(p1, p2, q1);
    int o2 = orientation(p1, p2, q2);
    if(o1 != o2)
    {
        int o3 = orientation(q1, q2, p1);
        int o4 = orientation(q1, q2, p2);
        return o3 != o4;
    }

    return 0;
}


int pointInPolygon(const Point p1, const Polygon &polygon)
{
    int c = 0;
    int n = polygon.size();
    Point p2 = Point(11, p1.y);
    for(int i = 0; i <= n; i++) {
        Point q1 = polygon[i];
        Point q2 = polygon[(i+1)%n];
        if(linesIntersect(q1,q2,p1,p2)) { c++; }
    }

    return c % 2 == 1;
}


bool pointInAllPolygons(const Point p, const vector<Polygon> &polygons)
{
    for(auto polygon : polygons)
    {
        if(!pointInPolygon(p, polygon)) {return false;}
    }
    return true;
}

coord_type polygonVolume(const Polygon polygon)
{
    coord_type sum = 0;
    int n = polygon.size();
    for(int i = 0; i <= n; i++)
    {
        Point p1 = polygon[i];
        Point p2 = polygon[(i+1)%n];
        sum += (p1.x + p2.x) * (p1.y - p2.y);
    }
    return 0.5 * sum;
}


int main()
{
    int n;
	cin >> n;

    vector<Polygon> polygons;
    coord_type minX, minY;
    coord_type maxX, maxY;
    minX = minY = 0;
    maxX = maxY = 10;

    // read polygons and find smallest common bounding box
    for(int i = 0; i < n; i++)
    {
        int ki;
        cin >> ki;

        coord_type pminX, pminY;
        coord_type pmaxX, pmaxY;
        pminX = pminY = 10;
        pmaxX = pmaxY = 0;

        vector<Point> polygon;
        for(int j=0; j < ki; j++)
        {
            coord_type vx, vy;
            cin >> vx;
            cin >> vy;
            polygon.push_back(Point(vx,vy));
            pminX = min(pminX, vx);
            pminY = min(pminY, vy);
            pmaxX = max(pmaxX, vx);
            pmaxY = max(pmaxY, vy);
        }
        polygons.push_back(polygon);
        minX = max(minX, pminX);
        minY = max(minY, pminY);
        maxX = min(maxX, pmaxX);
        maxY = min(maxY, pmaxY);
    }

    // sort polygons by size to improve early stopping
    sort(polygons.begin(), polygons.end(), [](Polygon p1, Polygon p2) {return polygonVolume(p1) > polygonVolume(p2); });

    int numSamples = 800000;
    int numHits = 0;

    coord_type bbArea = (maxX-minX) * (maxY-minY);

    // set up rng
    random_device rd;
    mt19937_64 engine(rd());
    uniform_real_distribution<coord_type> distX(minX,maxX);
    uniform_real_distribution<coord_type> distY(minY,maxY);

    // approximate area with monte carlo
    for(int i = 0; i < numSamples; i++)
    {
        Point s(distX(engine), distY(engine));
        if(pointInAllPolygons(s, polygons)) {numHits++;}
    }

    coord_type area = bbArea * (coord_type(numHits) / coord_type(numSamples));
    cout << fixed << setprecision(2) << area << endl;
    return 0;
}