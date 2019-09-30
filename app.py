#!/usr/bin/env python
from flask import Flask, session, request, render_template, url_for, redirect
import sys, re, macAdder, myldap, os
import os
from config import secret_key

app = Flask(__name__)

app.secret_key = secret_key

@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    if request.method == "POST":
        macs = request.form['macs']
        if macs == '':
            return render_template("index.html")
        macs = str(macs).lower().splitlines()
        for mac in macs:
            if not re.match("[0-9a-f]{2}([:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac):
                return render_template("index.html", result="MAC addresses provided are not in specified format")
        try:
            if request.form['action'] == 'Add':
                macAdder.add_macs(macs)
                return render_template("index.html", result="Successfully added all MAC addresses to both whitelists!")
            elif request.form['action'] == 'Remove':
                macAdder.remove_macs(macs)
                return render_template("index.html", result="Successfully removed all MAC addresses from both whitelists!")
            else:
                return render_template("index.html", result="Please choose whether to add or remove the MAC addresses")
        except:
            e = sys.exc_info()
            return render_template("index.html", result="Error adding MAC addresses", error=e)
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get("logged_in"):
        return redirect(url_for('index'))
    if request.method == "POST":
        result = auth(request.form["username"], request.form["password"])
        if result[0]:
            session["logged_in"] = True
            return redirect(url_for('index'))
        return render_template("login.html", result=result[1])
    return render_template("login.html")

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

# implement your own authentication. return (bool: success, str: message)
def auth(username, password):
    # for example, use LDAP authentication
    return myldap.auth(username, password)
