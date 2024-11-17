def optimizeTikTokWatchTime(n, initialWatch, repeatWatch, m):
    # Step 1: Calculate the time for the first complete watch of all reels
    first_time_watch = sum(initialWatch[i] + repeatWatch[i] for i in range(n))
    
    # Step 2: Calculate the number of rewatch views needed
    rewatch_needed = m - n  # Since n views are done in the first watch
    
    # Step 3: Sort the rewatch times to find the fastest rewatchable reels
    sorted_rewatch_times = sorted(repeatWatch)
    
    # Step 4: Add the time of the fastest rewatchable reels
    rewatch_time = sum(sorted_rewatch_times[i] for i in range(rewatch_needed))
    
    # Total minimum time = time for first watch + time for rewatching
    return first_time_watch + rewatch_time

# Test the function with the given example
initialWatch = [1, 5, 9, 11]
repeatWatch = [2, 7, 10, 11]
m = 4

result = optimizeTikTokWatchTime(initialWatch, repeatWatch, m)
print(f"Minimum total minutes required: {result}")