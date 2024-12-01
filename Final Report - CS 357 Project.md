### 1. **Problem Statement and Formulation**

**Objective**:  
The goal is to assign drones to waypoints in a light show such that the overall cost (e.g., fuel usage, time, or distance traveled) is minimized while ensuring each drone gets one unique waypoint.

**Problem Description**:  
A drone light show involves a large number of drones moving in synchronization to form predefined shapes. Each drone needs to be assigned to a unique waypoint in the desired shape. Assigning drones inefficiently leads to higher energy consumption, delays, or even collisions.

**Mathematical Formulation**:

- Let $n$ be the number of drones and waypoints.
- Define a cost matrix $C$, where $C[i][j]$ represents the cost (distance or time) for assigning drone $i$ to waypoint $j$.
- The problem is to find an assignment matrix $X$ such that:
    - $X[i][j]=1$ if drone $i$ is assigned to waypoint $j$, otherwise $X[i][j] = 0$.
    - Each row and column of $X$ has exactly one '$1$' (one assignment per drone and waypoint).
    - The total cost $\sum_{i=1}^{n}\sum_{j=1}^{n}C[i][j] \cdot X[i][j]$ is minimized.

### 2. **Introduction to the Hungarian Method and Applicability**

The Hungarian Method, also known as the Kuhn-Munkres algorithm, is an efficient algorithm to solve assignment problems.

**Core Idea**:  
The method reduces the cost matrix $C$ by subtracting row and column minima to find a zero-cost assignment, ensuring an optimal solution.

**Steps in the Hungarian Method**:

1. Subtract the smallest element of each row from all elements in that row.
2. Subtract the smallest element of each column from all elements in that column.
3. Cover all zeros in the resulting matrix using a minimum number of lines (rows or columns).
4. If the minimum number of lines equals $n$, an optimal assignment exists. Otherwise, adjust the matrix and repeat.

**Applicability**:

- Directly aligns with minimizing assignment costs (time/distance) for drones to waypoints.
- Guarantees an optimal, collision-free assignment.

### 3. **Algorithm Correctness and Our Intuition**

- **Correctness**: The Hungarian Method is optimal because it ensures the cost matrix is transformed into one where an assignment can be selected without ambiguity finally.
- **Why It Works**:
    - The reduction steps (subtracting row and column minima) preserve the relative cost differences.
    - Covering zeros ensures the assignment respects constraints while adjusting uncovered values ensures no assignments are missed.
- **Complexity**: $O(n^3)$ for an $n\times n$ cost matrix, making it feasible for real-time applications like drone shows.