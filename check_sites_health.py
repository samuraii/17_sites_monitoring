import sys
import requests
import whois
from datetime import datetime, timedelta


def load_urls4check(path_to_file):
    with open(path_to_file) as file_object:
        domains = file_object.readlines()
        return [domain.strip() for domain in domains]


def is_server_ok(url):
    response = requests.get(url)
    return response.ok


def is_domain_paid(domain, days=30):
    exp_date = whois.whois(domain).expiration_date
    time_delta = datetime.today() + timedelta(days)
    try:
        if type(exp_date) is list:
            return exp_date[0] > time_delta
        else:
            return exp_date > time_delta
    except TypeError:
        return None

def print_domain_check_results(domain):
    print('Domain', domain)
    print('Is it ok:', is_server_ok(domain))
    is_paid = is_domain_paid(domain)
    if is_paid == None:
        print('No expiration date info for this domain.')
    else:
        print('Is it paid:', is_paid)
    

if __name__ == '__main__':
    try:
        file_with_url = sys.argv[1]
        domains = load_urls4check(file_with_url)
    except IndexError:
        exit('File not passed to script.')
    except FileNotFoundError:
        exit('File not found.')

    for domain in domains:
        print_domain_check_results(domain)
        print('-'*20)
