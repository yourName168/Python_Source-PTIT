def has_matching_digits(number):
    # Lấy hai chữ số đầu và hai chữ số cuối của số
    first_two_digits = int(str(number)[:2])
    last_two_digits = int(str(number)[-2:])
    
    # Kiểm tra nếu hai chữ số giống nhau
    if first_two_digits == last_two_digits:
        return True
    else:
        return False

# Đọc số lượng test cases
num_tests = int(input())

# Duyệt qua từng test case
for _ in range(num_tests):
    n = int(input())  # Nhập số nguyên dương N
    
    if has_matching_digits(n):
        print("YES")
    else:
        print("NO")
