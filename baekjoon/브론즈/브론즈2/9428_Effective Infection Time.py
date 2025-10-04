def calculate_eit(inf_month, inf_year, strike_month, strike_year):
    eit = 0.0

    if inf_year == strike_year:
        months_passed = strike_month - inf_month
        total_months = 13 - inf_month
        eit += 0.5 * (months_passed / total_months)
    else:
        # 감염 연도는 무조건 0.5 EIT
        eit += 0.5

        # 중간 연도들
        eit += strike_year - inf_year - 1

        # 공격 연도 월 계산
        eit += (strike_month - 1) / 12

    return f"{eit:.4f}"


for _ in range(int(input())):
    inf_m, inf_y = map(int, input().split())
    strike_m, strike_y = map(int, input().split())
    print(calculate_eit(inf_m, inf_y, strike_m, strike_y))

