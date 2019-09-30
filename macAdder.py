import paramiko
import base64
from pyunifi.controller import Controller
import time
from config import *

add = 1
remove = -1
ssh = paramiko.SSHClient()
key = paramiko.ECDSAKey(data=base64.b64decode(cisco_ECDSAKey))
ssh.get_host_keys().add(cisco_ip, "ecdsa-sha2-nistp256", key)

def modify_unifi(macs, action):
    c = Controller(unifi_controller_url, unifi_username, unifi_password, port=unifi_port)
    wlans = c.get_wlan_conf()
    for wlan in wlans:
        if wlan["name"] == wlan_name and wlan["_id"] == wlan_id:
            macFilterList = wlan["mac_filter_list"]
            for mac in macs:
                if (action == add):
                    if mac not in macFilterList:
                        macFilterList.append(mac.upper())
                elif (action == remove):
                    if mac in macFilterList:
                        macFilterList.remove(mac.upper())
            newSetting = {"mac_filter_list": macFilterList}
            c._api_update("rest/wlanconf/{0}".format(wlan_id), newSetting)
            break

def modify_cisco(macs, action):
    ssh.connect(cisco_ip, username="abc", password="123") # these creds don't matter, cuz cisco ¯\_(ツ)_/¯
    conn = ssh.invoke_shell()

    #actually log in
    delay = 0.1
    run_command(conn, cisco_username, delay)
    run_command(conn, cisco_password, delay)

    # find ciscos wlan_ID for wlan_name
    out = run_command(conn, "show wlan summary", delay)
    out = str(out)
    index = out.find(wlan_name) # find wlan_name
    # move backwards to find wlan ID
    while not out[index].isdigit():
        index -= 1
    wlan = ''
    while out[index].isdigit():
        wlan = out[index] + wlan
        index -= 1
    wlan = int(wlan)
    for mac in macs:
        if (action == add):
            command = 'config macfilter add {0} {1}'.format(mac, wlan)
        elif (action == remove):
            command = 'config macfilter delete {0}'.format(mac)
        run_command(conn, command, delay)
    run_command(conn, "save config", delay)
    run_command(conn, "y", delay)
    ssh.close()

def run_command(conn, command, delay):
    while not conn.send_ready():
        time.sleep(delay)
    conn.send(command + "\n")
    while not conn.recv_ready():
        time.sleep(delay)
    return conn.recv(9999)

def add_macs(macs):
    # UniFi
    modify_unifi(macs, add)
    # Cisco
    modify_cisco(macs, add)


def remove_macs(macs):
    # UniFi
    modify_unifi(macs, remove)
    # Cisco
    modify_cisco(macs, remove)
    