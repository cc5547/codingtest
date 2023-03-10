def solution(order):
    answer = 0
    order_list = list(str(order))

    for i in range(len(order_list)):
        if "3" == order_list[i] : 
            answer += 1
        elif "6" == order_list[i]:
            answer += 1
        elif "9" == order_list[i]:
            answer += 1
        else :pass
    return answer