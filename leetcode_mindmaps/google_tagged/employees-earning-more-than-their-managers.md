# Employees Earning More Than Their Managers

**Problem Link:** [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

**Category:** Google tagged

## Problem Understanding
- Input: `Employee` table (id, name, salary, managerId).
- Output: Names of employees earning more than their manager.

## Approach

### Self Join
- **Idea**: Join table with itself. One copy as `Employee`, one as `Manager`.
- **Condition**: `e.managerId = m.id` AND `e.salary > m.salary`.
- **Query**:
  ```sql
  SELECT e.name as Employee
  FROM Employee e
  JOIN Employee m ON e.managerId = m.id
  WHERE e.salary > m.salary
  ```

### Subquery (WHERE clause)
- **Idea**: Select from two tables effectively (Cartesian product filtered).
- **Query**:
  ```sql
  SELECT e.name as Employee
  FROM Employee e, Employee m
  WHERE e.managerId = m.id AND e.salary > m.salary
  ```

## Implementation
- **SQL**:
  ```sql
  SELECT e.name AS Employee
  FROM Employee e
  INNER JOIN Employee m ON e.managerId = m.id
  WHERE e.salary > m.salary;
  ```

## Complexity Analysis
- **Time**: O(N) (with index on id)
- **Space**: O(N)

## Key Patterns
- **Self Join**: Comparing rows within same table.
