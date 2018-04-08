import sys
import requests
import whois
import datetime


def load_urls4check(path_to_file):
    with open(path_to_file) as file_object:
        return file_object.readlines()


def is_server_respond_with_200(url):
    response = requests.get(url)
    return response.status_code == 200


def get_domain_expiration_date(domain_name):
    return whois.query(domain_name).expiration_date - datetime.datetime.today()


if __name__ == '__main__':
    try:
        file_with_url = sys.argv[1]
    except IndexError:
        exit('File not passed to script.')
    except FileNotFoundError:
        exit('File not found.')

    sites = load_urls4check(file_with_url)
    for site in sites:
        site_url = site.strip()
        print('Domain:', site_url)
        print('Respond is 200:', is_server_respond_with_200(site_url))
        print('Domain expires in', get_domain_expiration_date(site_url))
        print('----------------------')
