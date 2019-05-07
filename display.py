from PIL import Image, ImageDraw
from appointments import drawAppointments
from util.colors import color
from calend import draw_everything

img = Image.new('1', (640, 384), color(1))
draw = ImageDraw.Draw(img)
draw.rectangle([(0,0), (319, 384)], color(0))

y = drawAppointments(img, draw, '2019-05-03', [{
            "summary": "Run boy",
            "colorId": "11",
            "start": {
                "dateTime": "2019-05-03T10:50:00+02:00",
                "timeZone": "Europe/Berlin"
            },
            "end": {
                "dateTime": "2019-05-03T11:50:00+02:00",
                "timeZone": "Europe/Berlin"
            }
        },{
        "summary": "Test",
        "colorId": "5",
        "start": {
            "dateTime": "2019-05-02T10:00:00+02:00",
            "timeZone": "Europe/Berlin"
        },
        "end": {
            "dateTime": "2019-05-03T11:00:00+02:00",
            "timeZone": "Europe/Berlin"
        }
    }], colors = [11, 0, 5, 0, 0])

y = drawAppointments(img, draw, '2019-05-08', [{
            "summary": "Run boy",
            "colorId": "11",
            "start": {
                "dateTime": "2019-05-08T10:50:00+02:00",
                "timeZone": "Europe/Berlin"
            },
            "end": {
                "dateTime": "2019-05-08T11:50:00+02:00",
                "timeZone": "Europe/Berlin"
            }
        },{
        "summary": "Testasdadsfasdfasdfasdfasdfasdfasdfasdfasdfasd",
        "colorId": "5",
        "start": {
            "dateTime": "2019-05-03T10:00:00+02:00",
            "timeZone": "Europe/Berlin"
        },
        "end": {
            "dateTime": "2019-05-09T11:00:00+02:00",
            "timeZone": "Europe/Berlin"
        }
    }], y, colors = [11, 0, 5, 0, 0])

y = drawAppointments(img, draw, '2019-05-08', [{
            "summary": "Run boy",
            "colorId": "11",
            "start": {
                "dateTime": "2019-05-08T10:50:00+02:00",
                "timeZone": "Europe/Berlin"
            },
            "end": {
                "dateTime": "2019-05-08T11:50:00+02:00",
                "timeZone": "Europe/Berlin"
            }
        },{
        "summary": "Testasdadsfasdfasdfasdfasdfasdfasdfasdfasdfasd",
        "colorId": "5",
        "start": {
            "dateTime": "2019-05-03T10:00:00+02:00",
            "timeZone": "Europe/Berlin"
        },
        "end": {
            "dateTime": "2019-05-09T11:00:00+02:00",
            "timeZone": "Europe/Berlin"
        }
    }], y, colors = [11, 0, 5, 0, 0])

y = drawAppointments(img, draw, '2019-05-21', [
    {
        "summary": "Run boy",
        "colorId": "11",
        "start": {
            "dateTime": "2019-05-21T10:50:00+02:00",
            "timeZone": "Europe/Berlin"
        },
        "end": {
            "dateTime": "2019-05-21T11:50:00+02:00",
            "timeZone": "Europe/Berlin"
        }
    }
], y)

draw_everything(draw)

def chunks(l, n):
    n = max(1, n)
    return (int("".join(map(str, l[i:i+n])), 2) for i in range(0, len(l), n))
print(len(list(chunks(list(map(lambda x: x if x <= 1 else 1, img.convert('1').getdata())), 8))))
img.save('img.png');