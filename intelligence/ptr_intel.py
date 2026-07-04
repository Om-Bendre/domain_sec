# analysis/ptr_intel.py

import re

# Provider signature database
# Each key is a pattern found in PTR hostnames
# Each value describes the provider and category
PROVIDER_SIGNATURES = {

    # Cloud Providers
    "amazonaws.com": {
        "provider": "Amazon Web Services",
        "category": "Cloud",
        "icon": "[AWS]"
    },
    "googleusercontent.com": {
        "provider": "Google Cloud Platform",
        "category": "Cloud",
        "icon": "[GCP]"
    },
    "cloudapp.azure.com": {
        "provider": "Microsoft Azure",
        "category": "Cloud",
        "icon": "[Azure]"
    },
    "digitalocean.com": {
        "provider": "DigitalOcean",
        "category": "Cloud",
        "icon": "[DO]"
    },
    "linode.com": {
        "provider": "Linode (Akamai)",
        "category": "Cloud",
        "icon": "[Linode]"
    },
    "vultr.com": {
        "provider": "Vultr",
        "category": "Cloud",
        "icon": "[Vultr]"
    },

    # CDN Providers
    "cloudflare.com": {
        "provider": "Cloudflare",
        "category": "CDN",
        "icon": "[CF]"
    },
    "fastly.net": {
        "provider": "Fastly",
        "category": "CDN",
        "icon": "[Fastly]"
    },
    "akamai.net": {
        "provider": "Akamai",
        "category": "CDN",
        "icon": "[Akamai]"
    },
    "akamaiedge.net": {
        "provider": "Akamai Edge",
        "category": "CDN",
        "icon": "[Akamai]"
    },

    # ISPs
    "comcast.net": {
        "provider": "Comcast",
        "category": "ISP",
        "icon": "[ISP]"
    },
    "att.net": {
        "provider": "AT&T",
        "category": "ISP",
        "icon": "[ISP]"
    },
    "verizon.net": {
        "provider": "Verizon",
        "category": "ISP",
        "icon": "[ISP]"
    },

    # Hosting
    "ovh.net": {
        "provider": "OVH",
        "category": "Hosting",
        "icon": "[OVH]"
    },
    "hetzner.com": {
        "provider": "Hetzner",
        "category": "Hosting",
        "icon": "[Hetzner]"
    },
    "hostinger.com": {
        "provider": "Hostinger",
        "category": "Hosting",
        "icon": "[Hostinger]"
    },

    # DNS / Infrastructure
    "google.com": {
        "provider": "Google",
        "category": "DNS/Infrastructure",
        "icon": "[Google]"
    },
    "1e100.net": {
        "provider": "Google Infrastructure",
        "category": "DNS/Infrastructure",
        "icon": "[Google]"
    },
    "ultradns.net": {
        "provider": "UltraDNS",
        "category": "DNS",
        "icon": "[DNS]"
    },
}


def identify_provider(ptr_hostname):
    """
    Match a PTR hostname against known provider signatures.
    Returns provider info dict or None if unrecognized.
    """
    hostname_lower = ptr_hostname.lower()

    for pattern, info in PROVIDER_SIGNATURES.items():
        if pattern in hostname_lower:
            return info

    return None


def decompose_hostname(ptr_hostname):
    """
    Attempt to extract encoded intelligence from PTR hostname structure.
    Returns a dict of extracted fields.
    """
    decomposition = {}

    # Look for IP address encoded with dashes: 54-239-28-85
    ip_dash_pattern = r'\b(\d{1,3})-(\d{1,3})-(\d{1,3})-(\d{1,3})\b'
    dash_match = re.search(ip_dash_pattern, ptr_hostname)
    if dash_match:
        encoded_ip = '.'.join(dash_match.groups())
        decomposition['encoded_ip'] = encoded_ip

    # Look for AWS region patterns: us-east-1, eu-west-2, ap-southeast-1
    region_pattern = r'\b(us|eu|ap|sa|ca|af|me)[-](east|west|north|south|central|southeast|northeast|southwest)[-]\d\b'
    region_match = re.search(region_pattern, ptr_hostname.lower())
    if region_match:
        decomposition['region'] = region_match.group(0)

    # Look for service type hints in hostname
    service_hints = {
        'mail': 'Mail Server',
        'smtp': 'Mail Server',
        'mx': 'Mail Server',
        'ns': 'Nameserver',
        'dns': 'DNS Server',
        'cdn': 'CDN Node',
        'edge': 'Edge Node',
        'proxy': 'Proxy Server',
        'vpn': 'VPN Server',
        'db': 'Database Server',
        'api': 'API Server',
    }

    hostname_lower = ptr_hostname.lower()
    for hint, service_type in service_hints.items():
        # Match as word boundary to avoid false positives
        if re.search(rf'\b{hint}\b', hostname_lower):
            decomposition['service_hint'] = service_type
            break

    return decomposition


def analyze_ptr(ptr_hostname):
    """
    Main analysis function. Takes a PTR hostname string,
    returns a structured intelligence dictionary.
    """
    result = {
        'hostname': ptr_hostname,
        'provider': None,
        'category': None,
        'icon': '',
        'encoded_ip': None,
        'region': None,
        'service_hint': None,
        'confidence': 'Unknown'
    }

    # Run provider identification
    provider_info = identify_provider(ptr_hostname)
    if provider_info:
        result['provider'] = provider_info['provider']
        result['category'] = provider_info['category']
        result['icon'] = provider_info['icon']
        result['confidence'] = 'High'

    # Run hostname decomposition
    decomposition = decompose_hostname(ptr_hostname)
    if decomposition.get('encoded_ip'):
        result['encoded_ip'] = decomposition['encoded_ip']
    if decomposition.get('region'):
        result['region'] = decomposition['region']
    if decomposition.get('service_hint'):
        result['service_hint'] = decomposition['service_hint']

    return result