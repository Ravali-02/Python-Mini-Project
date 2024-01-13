
import numpy as np
# a = np.arange(5)
# print(a <= 3)


# certificates_earned = pd.DataFrame({
#     'Certificates': [8, 2, 5, 6],
#     'Time (in months)': [16, 5, 9, 12]
# })
# names = ['Tom', 'Kris', 'Ahmad', 'Beau']
# certificates_earned['Certificates per month'] = round(
#     certificates_earned['Certificates'] /
#     certificates_earned['Time (in months)'], 2
# )


# # print(certificates_earned)
# s = pd.Series([np.nan, 1, 2, np.nan, 3])
# s = s.fillna(method='ffill')


# import csv
# __A__ = ' C:\Users\Krishna\Dropbox\IMP Doc\Clientquery.txt'
# __B__ = 'C:\Users\Krishna\Dropbox\IMP Doc\AP Portal.docx'
# __C__ ='C:\Users\Krishna\Dropbox\IMP Doc\Emailsdraft.txt'
# with open(__A__, 'r') as fp:
#     reader = csv.reader(fp, delimiter=__B__)
#     next(reader)
#     for index, values in enumerate(reader):
#         name, certs_num, months_num = values
#         print(f"{name} earned {__C__} certificates in {months_num} months")


import pandas as pd
# df = pd.read_csv("client.csv")

# b = np.array([[1.0, 2.0, 3.0], [3.0, 4.0, 5.0]])
# print(b)
# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(a)
# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()

print(b)
