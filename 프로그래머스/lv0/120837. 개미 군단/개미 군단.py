def solution(hp):
    answer = 0
    
    if hp >= 5:
        if hp % 5 == 0:
            answer = hp / 5
        elif hp % 5 != 0:
            answer = hp // 5
            answer += ((hp % 5) / 3)
            if ((hp % 5) % 3) != 0 :
                answer += ((hp % 5) % 3) / 1
    else :
        answer += hp // 3
        if hp < 3 and hp % 3 != 0:
            answer += ((hp % 3) / 1)
            
    return int(answer)