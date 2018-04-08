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


def get_domain_expiration_date(domain):
    return whois.query(domain).expiration_date - datetime.datetime.today()


if __name__ == '__main__':
    try:
        file_with_url = sys.argv[1]
    except IndexError:
        exit('File not passed to script.')
    except FileNotFoundError:
        exit('File not found.')

    domains = load_urls4check(file_with_url)
    for domain in domains:
        print('Domain:', domain)
        print('Domain is ok:', is_domain_ok(domain))
        print('Domain expires in', get_domain_expiration_date(domain))
        print('-'*20)
