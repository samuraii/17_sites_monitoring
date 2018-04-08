import sys
import requests
import whois
import datetime


def load_urls4check(path_to_file):
    with open(path_to_file) as file_object:
        domains = file_object.readlines()
        return [domain.strip() for domain in domains]


def is_domain_ok(url):
    response = requests.get(url)
    return response.ok


def domain_is_paid_30_days_or_more(domain, days=30):
    exp_date = whois.query(domain).expiration_date
    return datetime.datetime.today() + datetime.timedelta(days) <= exp_date


if __name__ == '__main__':
    try:
        file_with_url = sys.argv[1]
    except IndexError:
        exit('File not passed to script.')
    domains = load_urls4check(file_with_url)
    for domain in domains:
        print('Domain:', domain)
        print('It is ok:', is_domain_ok(domain))
        print('It is paid >= 30 days:', domain_is_paid_30_days_or_more(domain))
        print('-'*20)
