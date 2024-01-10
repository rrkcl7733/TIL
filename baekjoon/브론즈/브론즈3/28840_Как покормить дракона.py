from datetime import datetime, timedelta


a = datetime.strptime(input(), "%H:%M")
b = datetime.strptime(input(), "%H:%M")
b = b + timedelta(days=1) - a
h, r = divmod(b.days * (24 * 60 * 60) + b.seconds, 3600)
m, _ = divmod(r, 60)
print(f'{h:02d}:{m:02d}')
