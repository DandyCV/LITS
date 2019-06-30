import re

time1 = '11:59'
time2 = '23:59'
date = '27/06/2019'
email = 'KhD4747@gmai.com'

pattern_time1 = re.compile(r'([01][01]|[0]\d)\:[0-5]\d')
pattern_time2 = re.compile(r'[01]\d|[2][0-3]\:[0-5]\d')
pattern_date = re.compile(r'([012]\d|[3][01])/([0]\d|[1][012])/[12]\d{3}')
pattern_email = re.compile(r'\w+@\w+\.\w+')


print(
    pattern_time1.match(time1).group(),
    pattern_time2.match(time2).group(),
    pattern_date.match(date).group(),
    pattern_email.match(email).group()
)