import requests
from datetime import datetime, timedelta
from collections import Counter

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
            "day_code": day_code,
            "night_code": night_code
        })

    return weatherresults