#!/usr/bin/env python2
''' Super simple way to add public keys to metadata '''

import json
import sys

users_added = 0

try:
        f = open('jumpbox.json')
        metadata = json.load(f)
except:
        print "Error loading jumpbox file."
        sys.exit(1)

while True:
        sudo_access = False
        username = raw_input("Username (<CR> if done): ")
        if username == "" : break
        sudo = raw_input("Sudo access [true/FALSE] : ")
        if sudo == "true": sudo_access = True
        public_key = raw_input("Public Key : ")
        newuser = { username : { 'sudo_access' : sudo_access , 'ssh_keys' : [ public_key ] }}
        metadata['traits']['users']['table'].update(newuser)
        users_added += 1

if users_added > 0 :
        o = open('jumpbox.json.new','w')
        o.write(json.dumps(metadata,sort_keys=True, indent=4, separators=(',',': ')))
        print "Users added: %s" % users_added
else:
        print "No users added. Exiting"



