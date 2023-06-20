from selenium import webdriver
from selenium.webdriver.common.by import By
from mobileApplication import *


def crawl_bundle_files(domain, bundle_container):
    # TODO implement bundle crawler later
    print(bundle_container)


def find_js_bundles(domain, links):
    js_bundle_container = []
    for link in links:
        if link.endswith(".js"):
            js_bundle_container.append(link)
    if len(js_bundle_container) > 0:
        crawl_bundle_files(domain, js_bundle_container)


def crawl_domain(domain):
    driver = webdriver.Firefox()
    driver.get(domain)
    driver.set_page_load_timeout(15)
    a_elements = driver.find_elements(By.TAG_NAME, 'a')
    link_elements = driver.find_elements(By.TAG_NAME, 'link')
    button_elements = driver.find_elements(By.TAG_NAME, 'button')
    script_elements = driver.find_elements(By.TAG_NAME, 'script')
    gathered_link = []
    for a in a_elements:
        href_a = a.get_attribute('href')
        if href_a is not None:
            gathered_link.append(href_a)

    for link in link_elements:
        href_link = link.get_attribute('href')
        if href_link is not None:
            gathered_link.append(href_link)

    for button in button_elements:
        src_button = button.get_attribute('src')
        if src_button is not None:
            gathered_link.append(src_button)

    for script in script_elements:
        src_script = script.get_attribute('src')
        if src_script is not None:
            gathered_link.append(src_script)
    driver.close()

    find_apk_link(domain, gathered_link)
    find_js_bundles(domain, gathered_link)
