def canForm(source: str, target: str) -> str:
    source = source.lower()  # Convert to lowercase
    target = target.lower()  # Convert target to lowercase as well
    
    # Create a dictionary to count occurrences of each character in the source
    source_counts = {}
    
    for char in source:
        if char in source_counts:
            source_counts[char] += 1
        else:
            source_counts[char] = 1
    
    # Check if each character in the target can be formed from the source
    for char in target:
        if char not in source_counts or source_counts[char] == 0:
            return "no"  # If any character is missing or used up, return "no"
        source_counts[char] -= 1  # Decrease the count of the used character
    
    return "yes"
