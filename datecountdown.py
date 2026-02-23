from datetime import datetime

def calculate_days_left(target_date_str):
    """
    target_date_str: "2026-03-03"
    return: 剩余天数（int）
    """
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    return (target_date - today).days
