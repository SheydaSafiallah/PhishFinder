import dns.resolver


def url_validator(domain):
    if ("https://" or "http://") not in domain:
        domain = "https://" + domain
    else:
        pass
    return domain
# TODO check sub-domains/Main-domain
