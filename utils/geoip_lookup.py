import requests

def lookup_geoip(ip_address):

    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url)

    data = response.json()

    return {
        "country": data.get("country"),
        "country_code": data.get("countryCode"),
        "region": data.get("regionName"),
        "city": data.get("city"),
        "latitude": data.get("lat"),
        "longitude": data.get("lon"),
        "isp": data.get("isp"),
        "organization": data.get("org")
    }