def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    positive = [r for r in ratings if r >= 4]
    percentage = (len(positive) / len(ratings)) * 100
    return f"Positive Feedback: {round(percentage, 2)}%"
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(calculate_positive_feedback_percentage(ratings))

