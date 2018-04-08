# Sites Monitoring Utility

Script allows to monitor sites. It checks if the status code is 200 and reports the time left till domain expiration. 

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
Respond is 200: True
Domain expires in 175 days, 3:43:41.036310
----------------------
Domain: https://www.google.ru
Respond is 200: True
Domain expires in 330 days, 3:43:40.027355
----------------------
Domain: http://www.phyz-math.ru
Respond is 200: True
Domain expires in 196 days, 1:44:42.107101
----------------------
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
