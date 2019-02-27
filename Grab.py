import requests
from datetime import datetime
from datetime import timedelta

def isValidDay (x):
    if x == 1 or x == 3 or x==5:
        return True
    else:
        return False




def urlgen():
    Now = datetime.now()
    if Now.hour < 12 and isValidDay(Now.isoweekday()):
        ending = str(Now.strftime("%b")+str(Now.day))
        return ending
    else:
        while True:
            Now += timedelta(days=1)
            if isValidDay(Now.isoweekday()):
                ending = str(Now.strftime("%b") + str(Now.day))
                return ending

urlgen()
url_start = 'https://www.math.fsu.edu/~wooland/mad2104/templates/'+urlgen()+'.pdf'



response = requests.get(url_start)
if response.status_code == requests.codes.ok:
    print ("Code worked")
    with open(('C:\\Users\\User\\Desktop\\dISCRETE LECTURE TEMPLATES\\'+urlgen()+'.pdf'),'wb') as f:
        f.write(response.content)

else:
    print ("Request Failed")