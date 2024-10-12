""" Qasim Hussain - Algorithm 2
Pseudocode
1. Function: find_preferred_starting_city(city_distances, fuel, mpg)
    Input:
        - city_distances: an array of distances between consecutive cities
        - fuel: an array of available fuel at each city
        - mpg: miles per gallon the car can travel with 1 unit of fuel
    Output:
        - index of the preferred starting city

2. Initialize variables:
    - n = length of city_distances (number of cities)
    - total_fuel_needed = 0
    - total_fuel_available = 0
    - current_fuel = 0
    - start_city = 0

3. Iterate through each city (index i from 0 to n-1):
    - fuel_from_city_i = fuel[i] * mpg (total miles the car can drive from fuel at city i)
    - fuel_needed_to_next_city = city_distances[i] (miles needed to reach the next city)
    - current_fuel = current_fuel + fuel_from_city_i - fuel_needed_to_next_city
    - If current_fuel < 0:
        - Set start_city = i + 1 (we cannot start from this city, so move to the next one)
        - Reset current_fuel to 0
    - total_fuel_needed = total_fuel_needed + fuel_needed_to_next_city
    - total_fuel_available = total_fuel_available + fuel_from_city_i

4. If total_fuel_available < total_fuel_needed:
    - Return -1 (no valid starting city exists, but the problem guarantees one)

5. Return start_city

Explanation: We need to find the city where we can start and visit all cities, returning to the starting city with enough fuel.

Greedy approach: Traverse through each city and track the fuel availability and fuel requirements. If at any point the car doesn't have enough fuel to proceed, mark the next city as a potential starting point. Once the loop finishes, the last start_city will be the valid starting city.

Time Complexity: The algorithm iterates through all the cities exactly once, making it an O(n) algorithm, where n is the number of cities. Since the document requires the efficiency class, this is O(n).
"""

def find_preferred_starting_city(city_distances, fuel, mpg):
    n = len(city_distances)
    total_fuel_needed = 0
    total_fuel_available = 0
    current_fuel = 0
    start_city = 0

    for i in range(n):
        # Calculate the miles the car can travel from the fuel at city i
        fuel_from_city_i = fuel[i] * mpg
        # Calculate the distance to the next city
        fuel_needed_to_next_city = city_distances[i]

        # Update current fuel after moving to the next city
        current_fuel += fuel_from_city_i - fuel_needed_to_next_city

        # If current fuel is negative, we cannot start from this city
        if current_fuel < 0:
            start_city = i + 1
            current_fuel = 0

        # Track total fuel availability and total fuel needed
        total_fuel_needed += fuel_needed_to_next_city
        total_fuel_available += fuel_from_city_i

    # If the total available fuel is less than the total needed, return -1 (no valid starting point)
    if total_fuel_available < total_fuel_needed:
        return -1

    # Return the preferred starting city
    return start_city

# Sample Input
city_distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# Call the function
preferred_starting_city = find_preferred_starting_city(city_distances, fuel, mpg)
print(f"The preferred starting city is city {preferred_starting_city}")