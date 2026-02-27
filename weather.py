import requests
from datetime import datetime, timedelta
from collections import Counter
from weathermap import weather_map

LOCATIONS = {
    # 中国城市
    "wuhan": {"lat": 30.58333, "lon": 114.26667, "tz": "Asia/Shanghai", "name": "武汉"},
    "beijing": {"lat": 39.9042, "lon": 116.4074, "tz": "Asia/Shanghai", "name": "北京"},
    "shanghai": {"lat": 31.2304, "lon": 121.4737, "tz": "Asia/Shanghai", "name": "上海"},
    "guangzhou": {"lat": 23.1291, "lon": 113.2644, "tz": "Asia/Shanghai", "name": "广州"},
    "shenzhen": {"lat": 22.5431, "lon": 114.0579, "tz": "Asia/Shanghai", "name": "深圳"},
    "chengdu": {"lat": 30.6570, "lon": 104.0658, "tz": "Asia/Shanghai", "name": "成都"},
    "hongkong": {"lat": 22.3193, "lon": 114.1694, "tz": "Asia/Hong_Kong", "name": "香港"},
    
    # 国际城市
    "la": {"lat": 34.0522, "lon": -118.2437, "tz": "America/Los_Angeles", "name": "洛杉矶"},
    "tokyo": {"lat": 35.6895, "lon": 139.6917, "tz": "Asia/Tokyo", "name": "东京"},
    "london": {"lat": 51.5074, "lon": -0.1278, "tz": "Europe/London", "name": "伦敦"},
    "newyork": {"lat": 40.7128, "lon": -74.0060, "tz": "America/New_York", "name": "纽约"},
    "paris": {"lat": 48.8566, "lon": 2.3522, "tz": "Europe/Paris", "name": "巴黎"},
    "sydney": {"lat": -33.8688, "lon": 151.2093, "tz": "Australia/Sydney", "name": "悉尼"},
    "singapore": {"lat": 1.3521, "lon": 103.8198, "tz": "Asia/Singapore", "name": "新加坡"},
    "dubai": {"lat": 25.2048, "lon": 55.2708, "tz": "Asia/Dubai", "name": "迪拜"}
}

def get_day_night_single_code(lat,lon,timezone):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "weathercode",
        "timezone": timezone
    }

    data = requests.get(url,params=params).json()

    times = data["hourly"]["time"]
    codes = data["hourly"]["weathercode"]

    today = datetime.now().date()
    weatherresults = []

    for i in range(5):
        day = today + timedelta(days=i)

        day_codes = []
        night_codes = []

        for t, code in zip(times, codes):
            dt = datetime.fromisoformat(t)

            if dt.date() == day:
                if 6 <= dt.hour < 18:
                    day_codes.append(code)
                else:
                    night_codes.append(code)

        # 取出现次数最多的 weathercode
        day_code = Counter(day_codes).most_common(1)[0][0] if day_codes else None
        night_code = Counter(night_codes).most_common(1)[0][0] if night_codes else None

        weatherresults.append({
            "date": str(day),
            "day_weather": weather_map[day_code],
            "night_weather": weather_map[night_code]
        })

    return weatherresults