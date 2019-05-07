from datetime import datetime, timedelta
from util.colors import color
from fonts.fonts import bold, regular
from icons.icons import icon_array
import util.local as Local

screen_height = 384

def calculateDuration(start, end, current):
    current_date = datetime.strptime(current, "%Y-%m-%d")
    start_date = datetime.strptime(start['dateTime'], "%Y-%m-%dT%H:%M:%S%z")
    end_date = datetime.strptime(end['dateTime'], "%Y-%m-%dT%H:%M:%S%z")
    if (current_date + timedelta(days=1)).date() <= end_date.date():
        duration = 'Ganzen Tag'
    else:
        if start_date.date() >= current_date.date():
            duration = '%(start)s - %(end)s' % {'start': start_date.strftime('%H:%M'), 'end': end_date.strftime('%H:%M')}
        else:
            duration = '%(u)s %(e)s' % {'u': Local.until, 'e': end_date.strftime('%H:%M')}
    return duration

def calculateDate(current):
    current_date = datetime.strptime(current, "%Y-%m-%d")
    if current_date.date() == datetime.today().date():
        date = Local.today
        day = ''
    else:
        date = Local.month_names[current_date.month - 1]
        day = str(current_date.day)
    return (date, day)

def calculateSummary(draw, summary):
    w, h = draw.textsize(summary, bold(14))
    while w > 230:
        summary = '%s...' % summary[:-4]
        w, h = draw.textsize(summary, bold(14))
    return summary

def drawAppointments(image, draw, current_date, appointments, y_start=14, colors=[0, 0, 0, 0, 0]):
    date, day = calculateDate(current_date)
    if y_start + draw.textsize(date, regular())[1] + draw.textsize(day, regular())[1] + 17 > screen_height:
        return screen_height
    w, h = draw.textsize(date, regular())
    w_today, h_today = draw.textsize(Local.today, regular())
    draw.text((15 + w_today - w, y_start), date, color(1), regular())
    w_l, h_l = draw.textsize(day, regular())
    draw.text((15 + w_today - w_l, y_start + h + 2), day, color(1), regular())

    for i, appointment in enumerate(appointments):
        duration = calculateDuration(appointment['start'], appointment['end'], current_date)
        if y_start + 15 + (i * 40) + draw.textsize(duration, regular())[1] > screen_height:
            break
        if int(appointment['colorId']) in colors:
            index = colors.index(int(appointment['colorId']))
            image.paste(icon_array[index], (55, y_start - 1 + (i * 40)))
        draw.text((75, y_start - 2 + (i * 40)), calculateSummary(draw, appointment['summary']), color(1), bold(14))
        draw.text((75, y_start + 15 + (i * 40)), duration, color(1), regular())
    return y_start + len(appointments) * 40 + 5