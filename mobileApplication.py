from database import *
import requests


def find_apk_link(domain, links):
    applications = []
    for link in links:
        if '.apk' in link:
            applications.append(link)
    if len(applications) > 0:
        existence = "Found"
        mobile_app_exist(domain, existence)
        for application in applications:
            set_application(domain, application)
            download_application(domain, application)
    else:
        existence = "Not-Found"
        mobile_app_exist(domain, existence)


# TODO download Application and save it to /application/sus-domain-name/application

def download_application(domain, application):
    r = requests.get(application, allow_redirects=True)
    print("app is downloading...")
    open(f'/home/shey/Desktop/PhishFinder/applications/{domain}', 'wb').write(r.content)
