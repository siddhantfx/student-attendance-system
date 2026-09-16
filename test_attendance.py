def calculate_percentage(pdays, tdays):
    if tdays== 0:
        return 0
    return (pdays/tdays) * 100

result= calculate_percentage(3, 4)
assert result == 75.0, "Math error: Expected 75.0"

zero_result = calculate_percentage(0, 0)
assert zero_result == 0, "Math error: Expected 0"
print("All tests passed successfully!")
