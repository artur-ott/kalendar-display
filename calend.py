from fonts.fonts import regular
from util.local import month_names, weekdays_names
from util.colors import color
from datetime import datetime, timedelta
from calendar import monthrange

months_bounds = {
    'position': [
        (344, 134),
        (368, 134),
        (388, 134),
        (414, 134),
        (436, 134),
        (461, 134),
        (485, 134),
        (506, 134),
        (533, 134),
        (553, 134),
        (575, 134),
        (601, 134)
    ],
    'rectangle': [
        [(341, 135), (365, 147)],
        [(363, 135), (387, 147)],
        [(386, 135), (410, 147)],
        [(410, 135), (434, 147)],
        [(433, 135), (457, 147)],
        [(458, 135), (482, 147)],
        [(481, 135), (503, 147)],
        [(505, 135), (529, 147)],
        [(529, 135), (549, 147)],
        [(551, 135), (572, 147)],
        [(574, 135), (598, 147)],
        [(599, 135), (620, 147)]
    ]
}

weekdays_bounds = [
    (343, 161),
    (390, 161),
    (433, 161),
    (471, 161),
    (517, 161),
    (559, 161),
    (601, 161)
]

days_position = {
    'x-offset': 4,
    'x': [
        347,
        390,
        433,
        475,
        518,
        560,
        603
    ],
    'y': [
        186,
        219,
        252,
        285,
        318,
        351,
    ]
}

def draw_calendar_months(draw):
    today = datetime.today()
    draw.text((571, 91), str(today.year), color(0), regular(24))
    for i, month in enumerate(month_names):
        col = 0
        if i == today.month - 1:
            col = 1
            draw.rectangle(months_bounds['rectangle'][i], color(0))
        draw.text(months_bounds['position'][i], month, color(col), regular(9))

def draw_calendar_weekdays(draw):
    for i, weekday in enumerate(weekdays_names):
        draw.text(weekdays_bounds[i], weekday, color(0), regular(13))

def draw_days(draw):
    today = datetime.today()
    first = today.replace(day=1)
    last = today.replace(day=monthrange(today.year, today.month)[1])
    weeks = last.isocalendar()[1] - first.isocalendar()[1] + 1

    if weeks > 4:
        next_date = (first - timedelta(first.weekday()))
    else:
        next_date = (first - timedelta(first.weekday() + 7))
    for y in range(0, 6):
        for x in range(0, 7):
            if next_date.day >= 10:
                x_pos = days_position['x'][x]
            else:
                x_pos = days_position['x'][x] + days_position['x-offset']
            col = 0
            if next_date.date() == today.date():
                draw.ellipse([
                    (days_position['x'][x] - 5, days_position['y'][y] - 2),
                    (days_position['x'][x] + 18, days_position['y'][y] + 21)
                ], color(0))
                col = 1
            
            draw.text((x_pos, days_position['y'][y]), str(next_date.day), color(col), regular(13))
            next_date += timedelta(1)

def draw_everything(draw):
    draw_calendar_months(draw)
    draw_calendar_weekdays(draw)
    draw_days(draw)