#!/usr/bin/env python
import psycopg2
DB_NAME = "news"


# 1. query for Most popular three articles of all time are?
qrr1 = ''' SELECT title, views FROM articleswhoarepopular INNER JOIN articles ON
    articles.slug = articleswhoarepopular.slug ORDER BY views desc LIMIT 3; '''

# 2. query for Most popular article authors of all time are?
qrr2 = '''
    SELECT auth.name, count(l.id) as count
    FROM articles arti JOIN log l ON l.path = concat('/article/', arti.slug)
    JOIN authors auth
    ON auth.id = arti.author
    GROUP BY auth.name
    ORDER BY count DESC
    LIMIT 4;'''

# 3. query for Days on which more than 1% of requests lead to errors?
qrr3 = '''  select * from fail where error > 1; '''

# connecting the database


def connection(db_name):
    try:
        cun = psycopg2.connect(database=DB_NAME)
        cll = cun.cursor()
        return cun, cll
    except Exception as error:
        print(error)
# executing the required queries


def qrr_res(qrr):
    cun, cll = connection(DB_NAME)
    cll.execute(qrr)
    result = cll.fetchall()
    cun.close()
    return result

# returns query result


req_1 = "\n1.The 3 most popular articles of all time are:\n"
print(req_1)


def print_qrr_res(qrr_res):
    if(qrr1):
        res1 = qrr_res(qrr1)
        for res in res1:
            print ('\t' + str(res[0]) + ' ---> ' + str(res[1]) + ' views')
    else:
        print('this is not my first query')

if __name__ == "__main__":
    print_qrr_res(qrr_res)

req_2 = """\n2. The most popular article authors of all time are:\n"""
print(req_2)


def print_qrr_res2(qrr_res):
    try:
        res2 = qrr_res(qrr2)
        if (res2):
            for res in res2:
                print ('\t' + str(res[0]) + ' ---> ' + str(res[1]) + ' views')
        elif():
            print("this is not my second query")
        else:
            print("no such query")
    except Exception as e:
        raise e

print_qrr_res2(qrr_res)

req_3 = """\n3. Days with more than 1% of request that
lead to an error:\n"""
print(req_3)


def print_qrr_res3(qrr_res):
    if(qrr3):
        res3 = qrr_res(qrr3)
        for res in res3:
            print ('\t' + str(res3[0][0]) + ' ---> ' + str(res3[0][1]) + ' % ')
    else:
        print('this is not my error query')

if __name__ == "__main__":
    print_qrr_res3(qrr_res)
