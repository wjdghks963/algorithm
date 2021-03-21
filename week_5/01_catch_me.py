from collections import deque

c = 11
b = 2

# c의 위치 변화
# c는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1 만큼 움직임
# 즉 증가하는 속도가 1초마다 1씩 증가함


# b의 위치 변화는
# b - 1, b + 1, 2 * b

# 모든 경우의 수 다 나열 > BFS
# 규치적 > 배열, 자유자재 > 딕셔너리

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]

    while cony_loc > 200000:
        cony_loc += time  # 시간만큼 +1 +2 +3 +4 ...
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1
            new_position = current_position - 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!