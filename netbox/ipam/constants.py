# IP address families
AF_CHOICES = (
    (4, 'IPv4'),
    (6, 'IPv6'),
)

# IP address roles
IPADDRESS_ROLE_LOOPBACK = 10
IPADDRESS_ROLE_SECONDARY = 20
IPADDRESS_ROLE_ANYCAST = 30
IPADDRESS_ROLE_VIP = 40
IPADDRESS_ROLE_VRRP = 41
IPADDRESS_ROLE_HSRP = 42
IPADDRESS_ROLE_GLBP = 43
IPADDRESS_ROLE_CARP = 44
IPADDRESS_ROLE_CHOICES = (
    (IPADDRESS_ROLE_LOOPBACK, 'Loopback'),
    (IPADDRESS_ROLE_SECONDARY, 'Secondary'),
    (IPADDRESS_ROLE_ANYCAST, 'Anycast'),
    (IPADDRESS_ROLE_VIP, 'VIP'),
    (IPADDRESS_ROLE_VRRP, 'VRRP'),
    (IPADDRESS_ROLE_HSRP, 'HSRP'),
    (IPADDRESS_ROLE_GLBP, 'GLBP'),
    (IPADDRESS_ROLE_CARP, 'CARP'),
)

IPADDRESS_ROLES_NONUNIQUE = (
    # IPAddress roles which are exempt from unique address enforcement
    IPADDRESS_ROLE_ANYCAST,
    IPADDRESS_ROLE_VIP,
    IPADDRESS_ROLE_VRRP,
    IPADDRESS_ROLE_HSRP,
    IPADDRESS_ROLE_GLBP,
    IPADDRESS_ROLE_CARP,
)

# VLAN statuses
VLAN_STATUS_ACTIVE = 1
VLAN_STATUS_RESERVED = 2
VLAN_STATUS_DEPRECATED = 3
VLAN_STATUS_CHOICES = (
    (VLAN_STATUS_ACTIVE, 'Active'),
    (VLAN_STATUS_RESERVED, 'Reserved'),
    (VLAN_STATUS_DEPRECATED, 'Deprecated')
)

# Bootstrap CSS classes
STATUS_CHOICE_CLASSES = {
    0: 'default',
    1: 'primary',
    2: 'info',
    3: 'danger',
    4: 'warning',
    5: 'success',
}
ROLE_CHOICE_CLASSES = {
    10: 'default',
    20: 'primary',
    30: 'warning',
    40: 'success',
    41: 'success',
    42: 'success',
    43: 'success',
    44: 'success',
}

# IP protocols (for services)
IP_PROTOCOL_TCP = 6
IP_PROTOCOL_UDP = 17
IP_PROTOCOL_CHOICES = (
    (IP_PROTOCOL_TCP, 'TCP'),
    (IP_PROTOCOL_UDP, 'UDP'),
)
