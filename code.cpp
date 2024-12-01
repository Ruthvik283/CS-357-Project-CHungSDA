#include <iostream>
#include <vector>
#include <array>
#include <cmath>
#include <algorithm>
#include <limits>
#include <queue>

using namespace std;
using VC_t = pair<vector<int>, vector<int>>;
using edges_t = vector<pair<int, int>>;

const double INF = numeric_limits<double>::max();

struct bipartite_matching {
    int n_left, n_right, flow = 0;
    std::vector<std::vector<int>> g;
    std::vector<int> match_from_left, match_from_right;

    bipartite_matching(int _n_left, int _n_right)
        : n_left(_n_left),
          n_right(_n_right),
          g(_n_left),
          match_from_left(_n_left, -1),
          match_from_right(_n_right, -1),
          dist(_n_left) {}

    void add(int u, int v) { g[u].push_back(v); }

    std::vector<int> dist;

    void bfs() {
        std::queue<int> q;
        for (int u = 0; u < n_left; ++u) {
            if (!~match_from_left[u])
                q.push(u), dist[u] = 0;
            else
                dist[u] = -1;
        }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto v : g[u])
                if (~match_from_right[v] && !~dist[match_from_right[v]]) {
                    dist[match_from_right[v]] = dist[u] + 1;
                    q.push(match_from_right[v]);
                }
        }
    }

    bool dfs(int u) {
        for (auto v : g[u])
            if (!~match_from_right[v]) {
                match_from_left[u] = v, match_from_right[v] = u;
                return true;
            }
        for (auto v : g[u])
            if (dist[match_from_right[v]] == dist[u] + 1 &&
                dfs(match_from_right[v])) {
                match_from_left[u] = v, match_from_right[v] = u;
                return true;
            }
        return false;
    }

    int get_max_matching() {
        while (true) {
            bfs();
            int augment = 0;
            for (int u = 0; u < n_left; ++u)
                if (!~match_from_left[u]) augment += dfs(u);
            if (!augment) break;
            flow += augment;
        }
        return flow;
    }

    std::pair<std::vector<int>, std::vector<int>> minimum_vertex_cover() {
        std::vector<int> L, R;
        for (int u = 0; u < n_left; ++u) {
            if (!~dist[u])
                L.push_back(u);
            else if (~match_from_left[u])
                R.push_back(match_from_left[u]);
        }
        return {L, R};
    }

    std::vector<std::pair<int, int>> get_edges() {
        std::vector<std::pair<int, int>> ans;
        for (int u = 0; u < n_left; ++u)
            if(match_from_left[u] != -1)
                ans.emplace_back(u, match_from_left[u]);
        return ans;
    }
};

// Function to calculate the Euclidean distance
double euclideanDistance(array<double, 3>& a, array<double, 3>& b) {
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2));
}

// Function to perform row and column reductions
void reduceMatrix(vector<vector<double>>& C) {
    int n = C.size();

    // Row reduction
    for (int i = 0; i < n; ++i) {
        double rowMin = *min_element(C[i].begin(), C[i].end());
        for (int j = 0; j < n; ++j) {
            C[i][j] -= rowMin;
        }
    }

    // Column reduction
    for (int j = 0; j < n; ++j) {
        double colMin = INF;
        for (int i = 0; i < n; ++i) {
            colMin = min(colMin, C[i][j]);
        }
        for (int i = 0; i < n; ++i) {
            C[i][j] -= colMin;
        }
    }
}

// Function to find the minimum number of lines to cover all zeros in the matrix
pair<VC_t, edges_t> coverZeros(const vector<vector<double>>& C) {
    int n = C.size();
    bipartite_matching matching(n, n);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (C[i][j] == 0) {
                matching.add(i, j);
            }
        }
    }

    int max_matching = matching.get_max_matching();
    return {matching.minimum_vertex_cover(), matching.get_edges()};
}

// Adjust the cost matrix
void adjustMatrix(vector<vector<double>>& C, vector<bool>& rowCovered, vector<bool>& colCovered) {
    int n = C.size();
    double min_uncovered_value = INF;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (!rowCovered[i] && !colCovered[j]) {
                min_uncovered_value = min(min_uncovered_value, C[i][j]);
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        if (!rowCovered[i]) {
            for (int j = 0; j < n; ++j) {
                C[i][j] -= min_uncovered_value;
            }
        }
    }

    for (int j = 0; j < n; ++j) {
        if (colCovered[j]) {
            for (int i = 0; i < n; ++i) {
                C[i][j] += min_uncovered_value;
            }
        }
    }
}

// CHungSDA Algorithm
vector<pair<int, int>> CHungSDA(vector<vector<double>>& C) {
    int n = C.size();
    vector<pair<int, int>> assignment;

    while (true) {
        vector<bool> rowCovered(n, false), colCovered(n, false);
        reduceMatrix(C);

        auto [VC_sets, edges] = coverZeros(C);
        int lines = VC_sets.first.size() + VC_sets.second.size();

        if (lines >= n) {
            // Optimal assignment found
            assignment = std::move(edges);
            break;
        }

        for (const auto& row : VC_sets.first) {
            rowCovered[row] = true;
        }

        for (const auto& col : VC_sets.second) {
            colCovered[col] = true;
        }

        adjustMatrix(C, rowCovered, colCovered);
    }

    return assignment;
}

int main() {
    freopen("input.txt", "r", stdin);
    // Input: Positions of drones, waypoints, and minimum distance
    int n;
    double deltaMin;
    cout << "Enter the number of drones/waypoints: ";
    cin >> n;

    cout << "Enter the minimum distance (delta_min): ";
    cin >> deltaMin;

    vector drones(n, array<double, 3> {});
    vector waypoints(n, array<double, 3> {});

    cout << "Enter drone positions (x y z):\n";
    for (int i = 0; i < n; ++i) {
        cin >> drones[i][0] >> drones[i][1] >> drones[i][2];
    }

    cout << "Enter waypoint positions (x y z):\n";
    for (int i = 0; i < n; ++i) {
        cin >> waypoints[i][0] >> waypoints[i][1] >> waypoints[i][2];
    }

    // Build the cost matrix
    vector<vector<double>> costMatrix(n, vector<double>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            costMatrix[i][j] = euclideanDistance(drones[i], waypoints[j]);
        }
    }

    bool isValid=1;

    vector<pair<int,int>>close_points;

    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(i!=j&&euclideanDistance(waypoints[i], waypoints[j])<deltaMin){
                close_points.push_back({i,j});
            }
        }
    }

    if(!isValid) {

        //Handling the case when constraint 2 fails
        cout<<"The following waypoints are too close: \n";
        for(auto &p:close_points){
            int i=p.first,j=p.second;
            printf("{%d,%d,%d} {%d,%d,%d}\n",waypoints[i][0],waypoints[i][1],waypoints[i][2],waypoints[j][0],waypoints[j][1],waypoints[j][2]);
        }
        return 0;
    }

    // Solve using the CHungSDA algorithm
    edges_t assignment = CHungSDA(costMatrix);

    // Output the assignment
    cout << "Optimal assignment:\n";
    for (auto& pair : assignment) {
        int i = pair.first;
        int x = drones[i][0], y=drones[i][1], z=drones[i][2];
        cout << "Drone " << pair.first<<": ("<<x<<", "<<y<<", "<<z<<") ";
        i=pair.second;
        x = waypoints[i][0], y=waypoints[i][1], z=waypoints[i][2];
        cout << " -> Waypoint " << pair.second<<": ("<<x<<", "<<y<<", "<<z<<")\n";
    }

    return 0;
}

