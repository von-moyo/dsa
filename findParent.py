def findParent(processNumber):
    currentProcess = 1
    nextProcess = 2  # Process 1 spawns process 2

    # Iterate over each process starting from process 1
    while True:
        # The number of children the current process spawns is equal to its process number
        childrenCount = currentProcess

        # The children range is from nextProcess to nextProcess + childrenCount - 1
        if processNumber >= nextProcess and processNumber < nextProcess + childrenCount:
            return currentProcess

        # Move to the next process
        nextProcess += childrenCount
        currentProcess += 1

# Example usage:
print(findParent(6))  # Output: 3