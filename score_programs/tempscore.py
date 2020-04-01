def temperature_Score(temp):
    if temp <= 17 or temp >= 35:
        return 0
    else:
        score = ((1.975 * -((temp - 26) ** 2)) + 160) / 160
        return score

