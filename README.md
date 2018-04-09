# Sites Monitoring Utility

Script allows to monitor sites. It checks if the response of the server is ok (not 4\*\* or 5\*\*) and if the domain name is paid based on the information of whois service. 

# How to use

Before using script install the required packages.

```bash
pip install requirements.txt
```

To run script pass file with urls to sctipt:

```bash
python check_sites_health.py <path_to_file>
```

Output:

```bash
Domain: https://www.yandex.ru
Is it ok: True
Is is paid True
--------------------
Domain: https://www.google.com
Is it ok: True
Is is paid True
--------------------
Domain: http://phyz-math.ru
Is it ok: True
Is is paid True
--------------------
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
