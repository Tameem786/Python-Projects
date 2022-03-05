import json
import pandas as pd
import tldextract


info = []


def get_domain(x):
    if x.startswith('chrome-extension://'):
        return "chrome_extension"
    domain = tldextract.extract(x)[1]
    sub_domain = tldextract.extract(x)[0]
    if domain == "google":
        if sub_domain=="www":
            return "google_search"
        else:
            return sub_domain + "." + domain
    return domain


with open('BrowserHistory.json', encoding='utf-8') as file:
    data = json.load(file)    

# print('time_usec', 'time_usec2', 'PST_time', 'month', 'hour', 'day_of_week') / range=28873
for i in range(28873):
    user = get_domain(data['Browser History'][i]['client_id'])
    ##user_id = user 
    ##if user == '33md0GbyPONeFeGeZopZPQ==':
    ##    print("user1")
    url = get_domain(data['Browser History'][i]['url'])
    page_transition = get_domain(data['Browser History'][i]['page_transition'])
    page_title = get_domain(data['Browser History'][i]['title'])
    time_usec = data['Browser History'][i]['time_usec']
    time_usec2 = pd.to_datetime(time_usec, unit='us', utc=True)
    pst_time = time_usec2.tz_convert('America/Vancouver')
    month = pst_time.month
    hour = pst_time.hour
    day = pst_time.day_name()
    ##weekday = pst_time(lambda x: "Y" if x.weekday()<5 else "N")
    info.append([user, time_usec, time_usec2, pst_time, month, hour, day, url, page_transition, page_title])
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
df = pd.DataFrame(info, columns=['client', 'time_usec', 'time_usec2', 'PST_time', 'month', 'hour', 'day_of_week', 'domain', 'page_transition', 'page_title'])
df.to_csv (r'C:\Users\LENOVO\Desktop\dataset\browsing_history.csv', index = False, header=True)
print(df)

