import requests
import csv

loop = 1
while loop:
    product = raw_input('product id = ')

    url = 'https://tiki.vn/ajax/reviews?product_id=' + product + '&limit=100&sort=thank_count|desc,customer|all,stars|all&_=1496629681035'

    r = requests.get(url)

    data = r.json()['data']

    print 'length = ', len(data)

    with open('test.csv', 'a+') as fp:
        a = csv.writer(fp, delimiter=',', quotechar='|')
        for row in data:
            if row['rating'] > 3:
                a.writerow([1 ,row['content'].encode('utf-8').replace('\n', ' ').replace('\r', '')])
            else:
                a.writerow([-1 ,row['content'].encode('utf-8').replace('\n', ' ').replace('\r', '')])
        fp.close()

    loop = bool(int(raw_input('Continue , press 1, stop press 0 : ')))

print 'BYE BYE'