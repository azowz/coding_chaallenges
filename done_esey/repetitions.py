def repetitions(s: str) -> int:
    if not s:
        return 0
    
    max_count = 1
    current_count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # Compare current character with the previous one
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1  # Reset count if characters are different
    
    return max_count
