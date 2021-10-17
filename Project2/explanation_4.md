## Problem 4 : Active Directory

### Reasoning for choosing data sturctures and/or algorithms

**Breadth First Search** is the key algorithm for searching all names in the current group and sub groups. If the target name does not exist in the current group, then the algorithm visits a sub-group one by one and keeps searching it, until no more group is left to visit.

### Time Complexity

O(users) - All users should be visited at least once to confirm the target name belongs to the given group.

### Space Complexity

O(groups) - In the worst case, `group_ls` list can contains all existing groups.
