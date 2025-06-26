while 1:
    flight, num = input().split()
    if flight == "#":
        exit()
    
    seats = int(num)  # 현재 예약된 좌석 수

    while 1:
        action, x_str = input().split()

        if action == "X":
            break
        x = int(x_str)
        
        if action == "B":
            # 예약: 68좌석 초과하지 않으면 반영
            if seats + x <= 68:
                seats += x
        elif action == "C":
            # 취소: 현재 예약된 좌석보다 많지 않으면 반영
            if x <= seats:
                seats -= x

    print(flight, seats)
