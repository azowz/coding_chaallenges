def Decimal_places(num: str) -> int:
    if '.' in num:
        return len(num) - num.find('.') - 1
    else:
        return 0

print(Decimal_places('45.6574'))  # Output: 4