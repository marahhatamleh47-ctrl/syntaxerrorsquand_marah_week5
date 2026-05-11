# logic_tools.py

def assign_badge(score):
    if 90 <= score <= 100:
        return "Elite Gold"
    elif 70 <= score < 90:
        return "Professional Silver"
    elif 50 <= score < 70:
        return "Starter Bronze"
    else:
        return "Needs Retraining"