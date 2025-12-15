# Combine Two Tables

**Problem Link:** [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

**Category:** Google tagged

## Problem Understanding
- Input: `Person` (personId, lastName, firstName), `Address` (addressId, personId, city, state).
- Output: firstName, lastName, city, state for **every** person.
- Constraint: If address is missing, report null.

## Approach

### Left Join
- **Idea**: We want **ALL** rows from `Person` regardless of match in `Address`.
- **Logic**: `Person LEFT JOIN Address`.
- **Query**:
  ```sql
  SELECT p.firstName, p.lastName, a.city, a.state
  FROM Person p
  LEFT JOIN Address a ON p.personId = a.personId
  ```

## Implementation
- **SQL**:
  ```sql
  SELECT firstName, lastName, city, state
  FROM Person
  LEFT JOIN Address ON Person.personId = Address.personId
  ```

## Complexity Analysis
- **Time**: O(N + M) (Merge join or Hash join)
- **Space**: O(N + M)

## Common Pitfalls
- **Inner Join**: Would exclude people without address. Problem asks for "regardless if there is an address".

## Key Patterns
- **Left Join**: Retain all rows from left table.
