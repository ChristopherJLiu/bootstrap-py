#system imports
import os
import sys

#local imports
import api


print(" Python version: " + sys.version)
print("\n Hello - "+ os.environ['SERVICE_DESC'])

print("\n\n\n"+ os.environ['SERVICE_NAME'] + " service started")

api.init()

