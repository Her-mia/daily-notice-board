from datetime import datetime, timedelta

# 默认目标时间：当前时间 + 1 小时
target_time = datetime.now() + timedelta(hours=1)

def get_target_time():
    return target_time

def set_target_time(new_time: datetime):
    global target_time
    target_time = new_time
