from domain import url_validator
from statusCode import *
from crawler import *
from database import *
# TODO automation !!! :)

if __name__ == '__main__':

    # TODO connect main database that has sus_domains
    sus_domain = input("Enter suspicious Domain")
    sus_domain = url_validator(sus_domain)
    if domain_existence(sus_domain):
        print(f'this domain "{sus_domain}" exist in database.\nwe don\'t insert it into database.')
    else:
        set_domain(sus_domain)
        set_time(sus_domain)
    data = status_checker(sus_domain)
    set_statuscode(data[0], data[1])
    if data[1] == 200:
        # TODO check if webpage has Auth-page or pay-page
        crawl_domain(sus_domain)
    else:
        print(f'This domain is unreachable now ....\n domain:{sus_domain}, status:{data[1]}')

