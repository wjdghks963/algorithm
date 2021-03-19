top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()
        print(len(heights))
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))