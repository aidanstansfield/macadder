# You will need to change all of the following configuration variables to suit your needs

# flask config
secret_key = b'\x97\xd39Rf.l\xcb\xc5\x96eo\xc0=\xe5\x11' # generate with os.urandom(16)

# macAdder config
# unifi
unifi_controller_url = "unifi.exampledomain.com"
unifi_username = "admin"
unifi_password = "password"
unifi_port = 443
wlan_name = "My-WLAN"
wlan_id = "132f418163d07083353fcc47"

# cisco
cisco_ECDSAKey = b'AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEvfx1o5FqWM9hBEmFhsEtznpgX1HuHwT/nxdzLE028b7qXKyNyjWBLg4zzJVJyezUIqxTP0dKmuJqAZOMfau1Q=' # example key from the web
cisco_ip = '10.10.10.10'
cisco_username = 'admin'
cisco_password = 'password'

# ldap config, if you want to use alternative authentication ignore this
ldap_server = "ldap://domaincontroller1.exampledomain.com"
base = "dc=exampledomain,dc=com"
email_suffix = "@exampledomain.com"
allowed_ou = 'OU=Admin Accounts'