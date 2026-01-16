def calculate_reward(conversion, fatigue, cost):
    return conversion - (0.5 * fatigue) - cost
