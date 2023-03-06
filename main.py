import math
import random

# Define a function to check if a number is a perfect square
def is_perfect_square(n):
    """Returns True if n is a perfect square, False otherwise."""

    return int(math.sqrt(n)) ** 2 == n

# Define a function to count the number of pairs of consecutive elements in a sequence whose sum is a perfect square
def count_pairs(sequence):    
    """Returns the number of pairs of consecutive elements in sequence whose sum is a perfect square."""

    count = 0
    for i in range(len(sequence) - 1):
        if is_perfect_square(sequence[i] + sequence[i+1]):
            count += 1
    return count

# Define the GRASP algorithm to find the sequence that maximizes the number of pairs of consecutive elements whose sum is a perfect square
def grasp(sequence, max_iterations, k):
    # Set the initial best solution and score
    best_solution = sequence
    best_score = count_pairs(sequence)

    # Repeat the following for a given number of iterations
    for i in range(max_iterations):
        # Generate a new candidate solution by swapping k pairs of elements at random
        candidate_solution = sequence.copy()
        for j in range(k):
            # Choose two random indices to swap
            index1 = random.randint(0, len(sequence) - 1)
            index2 = random.randint(0, len(sequence) - 1)
            # Swap the elements at the chosen indices
            candidate_solution[index1], candidate_solution[index2] = candidate_solution[index2], candidate_solution[index1]
        
        # Calculate the score of the candidate solution
        candidate_score = count_pairs(candidate_solution)

        # If the candidate solution has a higher score than the current best solution,
        # update the best solution and score
        if candidate_score > best_score:
            best_solution = candidate_solution
            best_score = candidate_score
    
    # Return the best solution found
    return best_solution



if __name__ == '__main__':
    # Define the input sequence
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Set the algorithm parameters
    max_iterations = 1000
    k = 9

    # Call the GRASP algorithm to find the solution
    best_sequence = grasp(sequence, max_iterations, k)

    # Print the result
    print(best_sequence)