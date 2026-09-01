def get_sum_avg_of_ints(first_num, *nums) -> tuple:
    nums = (first_num, *nums)

    nums = [int(n) for n in nums
            if type(n) in (int, float) or 
            type(n) is str and n.isnumeric()]

    s = sum(nums)
    a = s/len(nums)
    return s, a

total, avg = get_sum_avg_of_ints(123, '456', 49, 2.9, 'asd', '23.45', 689, '443')
print(f'{total=}')
print(f'{avg=}')

total, avg = get_sum_avg_of_ints(123)
print(f'{total=}')
print(f'{avg=}')