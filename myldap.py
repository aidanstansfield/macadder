import ldap
from config import ldap_server, base, email_suffix, allowed_ou


def auth(username, password):
    connection = ldap.initialize(ldap_server)
    try:
        connection.simple_bind_s(username+email_suffix, password)
        ldap_result = connection.search(base, ldap.SCOPE_SUBTREE, f"(&(objectClass=*)(sAMAccountName={username}))", ['cn'])
        _, data = connection.result(ldap_result, 0)
        connection.unbind_s()
        if allowed_ou in data[0][0]:
            return (True, "Successful")
        return (False, "You do not have permission to use this tool")
    except ldap.INVALID_CREDENTIALS:
        connection.unbind_s()
        return (False, "Incorrect username/password")
    except:
        connection.unbind_s()
        return (False, "Something went wrong when talking to LDAP")