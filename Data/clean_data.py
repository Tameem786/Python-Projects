import json as js
from pydoc import cli
from xml import dom
import pandas as pd
import csv
from urllib.parse import urlparse
import math 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

svclassifier_linear = SVC(kernel='linear', C=1.0)
svclassifier_RBF = SVC(kernel='rbf', C=1.0, gamma=0.2634335)
svclassifier_polynomial = SVC(kernel='poly', C=0.25, degree=3)

data = pd.read_csv(r'D:\zamanPyEnv\Python\Data\\domainListFrecencSVM.csv')

X = data.drop('Labelling', axis=1)
y = data['Labelling']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40)

# print(X_test)

svclassifier_polynomial.fit(X_train, y_train)
y_pred = svclassifier_polynomial.predict(X_test)
cm1 = confusion_matrix(y_test,y_pred)
# total1=sum(sum(cm1))
# print(cm1[0,1])
# Accuracy = (cm1[0,0]+cm1[1,1])/total1
# Specificity = cm1[0,0]/(cm1[0,0]+cm1[0,1])
# Sensitivity = cm1[1,1]/(cm1[1,0]+cm1[1,1])
# print(Accuracy, Specificity, Sensitivity)
print(classification_report(y_test,y_pred))
# Y = round(math.log(2) / 30, 5)
print(cm1)

# print((-1) * Y * float('273287'))

# Current_Visit_value = []

# def current_visit_value(visit_type_points, visit_age):
#     return int(visit_type_points) * math.exp((-1) * Y * int(visit_age))


# df = pd.read_csv(r'D:\zamanPyEnv\Python\Data\\domainList.csv')

# clients = df['client'].tolist()
# clients_unique = list(dict.fromkeys(clients))
# index = 0
# for i in clients_unique:
#     for j in range(index, index+clients.count(i)):
#         Current_Visit_value.append(current_visit_value(df['Visit Count'][j], df['Difference'][j]))
#     index = index + clients.count(i)

# print(len(Current_Visit_value))

# df['Current Visit Value'] = Current_Visit_value

# df.to_csv(r'D:\zamanPyEnv\Python\Data\\domainList.csv', index=False)


# df_domain = pd.read_csv(r'D:\zamanPyEnv\Python\Data\\client5_domain_visit.csv')
# df_url = pd.read_csv(r'D:\zamanPyEnv\Python\Data\\client_url_list.csv')

# df_url.drop_duplicates()

# df_url.to_csv(r'D:\zamanPyEnv\Python\Data\\client1_url_domain.csv')

# domains = []
# urls = []
# clean_url = []
# domains_checked = []

# for i in range(len(df_domain['Domain'])):
#     domains.append(df_domain['Domain'][i])

# for i in range(len(df_url['Client5 Url'])):
#     domain = urlparse(df_url['Client5 Url'][i]).netloc
#     if(domains.count(domain) > 0):
#         continue
#     else:
#         domains.append(domain)
#         urls.append(df_url['Client5 Url'][i])



# rows = zip(urls, domains)

# with open("D:\zamanPyEnv\Python\Data\\client5_url_domain.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(("Url", "Domain"))
#     for row in rows:
#         writer.writerow(row)
    

# for i in range(len(domains)):
#     if domains_checked.count(domains[i]) > 0:
#         continue
#     for j in range(len(urls)):
#         if urls[j].count(domains[i]) > 0:
#             clean_url.append(urls[j])
#             domains_checked.append(domains[i])
#             break

# print(len(domains))
# print(len(urls))
# from pysafebrowsing import SafeBrowsing

# KEY = "AIzaSyDw4hqjU0WPVkCk26K_Zwa2Ln8juJy4GLo"

# s = SafeBrowsing(KEY)
# r = s.lookup_urls(['http://malware.testing.google.test/testing/malware/'])
# print(r)


# urls = []
# clients = []
# client1_urls = []
# client2_urls = []
# client3_urls = []
# client4_urls = []
# client5_urls = []

# df = pd.read_csv(r'D:\zamanPyEnv\Python\Data\\clients.csv')

# for i in range(len(df['Client Id'])):
#     clients.append(df['Client Id'][i])


# with open('D:\zamanPyEnv\Python\Data\BrowserHistory.json', 'r', encoding='utf-8') as file:
#     data = js.loads(file.read())

#     for i in data['Browser History']:
#         if(i['client_id'] == clients[0] and len(client1_urls) < 200):
#             client1_urls.append(i['url'])
#         if(i['client_id'] == clients[1] and len(client2_urls) < 200):
#             client2_urls.append(i['url'])
#         if(i['client_id'] == clients[2] and len(client3_urls) < 200):
#             client3_urls.append(i['url'])
#         if(i['client_id'] == clients[3] and len(client4_urls) < 200):
#             client4_urls.append(i['url'])
#         if(i['client_id'] == clients[4] and len(client5_urls) < 200):
#             client5_urls.append(i['url'])
        

# file.close()


# urls = list(dict.fromkeys(urls))

# client1_urls = list(dict.fromkeys(client1_urls))
# client2_urls = list(dict.fromkeys(client2_urls))
# client3_urls = list(dict.fromkeys(client3_urls))
# client4_urls = list(dict.fromkeys(client4_urls))
# client5_urls = list(dict.fromkeys(client5_urls))
# client5_urls_security_level = []
# client5_urls.remove("chrome://newtab/")
# for i in client5_urls:
#     try:
#         r = s.lookup_urls([i])
#         client5_urls_security_level.append(r[i]['malicious'])
#     except:
#         continue

# rows = zip(client1_urls, client2_urls, client3_urls, client4_urls, client5_urls)

# with open("D:\zamanPyEnv\Python\Data\\client_url_list.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(("Client1 Url", "Client2 Url", "Client3 Url", "Client4 Url", "Client5 Url"))
#     for row in rows:
#         writer.writerow(row)









# from tracemalloc import DomainFilter
# from distutils.command.clean import clean
# import pandas as pd
# import csv

# df = pd.read_csv(r'D:\zamanPyEnv\Python\Data\\output.csv')

# new_df = df.dropna()

# new_df.to_csv(r'D:\zamanPyEnv\Python\Data\\output.csv', index=False)

# clients = []
# client1_domains = []
# client2_domains = []
# client3_domains = []
# client4_domains = []
# client5_domains = []

# for i in range(len(df['client'])):
#     clients.append(df['client'][i])

# clients = list(dict.fromkeys(clients))

# users = ["User 1", "User 2", "User 3", "User 4", "User 5"]
# rows = zip(users, clients)

# with open("D:\zamanPyEnv\Python\Data\\clients.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(("Client", "Client Id"))
#     for row in rows:
#         writer.writerow(row)

# print(clients)



# for i in range(len(df['client'])):
#     if(df['client'][i] == clients[0]):
#         client1_domains.append(df['domain'][i])
#     if(df['client'][i] == clients[1]):
#         client2_domains.append(df['domain'][i])
#     if(df['client'][i] == clients[2]):
#         client3_domains.append(df['domain'][i])
#     if(df['client'][i] == clients[3]):
#         client4_domains.append(df['domain'][i])
#     if(df['client'][i] == clients[4]):
#         client5_domains.append(df['domain'][i])

# print(len(client1_domains))
# print(len(client2_domains))
# print(len(client3_domains))
# print(len(client4_domains))
# print(len(client5_domains))

# client5_domain_clean = list(dict.fromkeys(client5_domains))

# client5_doamin_vitied = []

# for i in client5_domain_clean:
#     client5_doamin_vitied.append(client5_domains.count(i))
    
# rows = zip(client5_domain_clean, client5_doamin_vitied)

# with open("D:\zamanPyEnv\Python\Data\\client5_domain_visit.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(("Domain", "Time Visited"))
#     for row in rows:
#         writer.writerow(row)

# clean_list = list(dict.fromkeys(x))

# df_new = pd.DataFrame(clean_list)
# df_new.to_csv(r'D:\zamanPyEnv\Python\Data\\domainList.csv', index=False)

# print(len(clean_list))




