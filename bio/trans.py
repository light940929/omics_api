#!/usr/bin/env python
import os
import re
import json
from urllib2 import urlopen, Request


execfile("../../omics_pipe/parameters/default_parameters.py")
url = 'http://localhost:8000/template/1/element/'
token = 'Bearer gebTE2GUf3dSvKWJYL9GwWoGU3L6Op'
headers = {'Authorization': '%s' % token}
request = Request(url, headers=headers)
response = urlopen(request)
data = json.loads(response.read())

def addArg(default_parameters):
    for num in data:
        print "argument" + str(num['id']) + ':\t' + str(num['argument']).upper()
        print "default" + str(num['id']) + ':\t' + str(num['default'])
        wargs = str(num['argument']).upper()
        arg = str(num['default'])
        default_parameters[wargs] = arg
    return default_parameters

def delArg(default_parameters):
    for num in data:
        print "argument" + str(num['id']) + ':\t' + str(num['argument']).upper()
        print "default" + str(num['id']) + ':\t' + str(num['default'])
        wargs = str(num['argument']).upper()
        del default_parameters[wargs]
    return default_parameters

def writeDict(dict, filename):
    with open(filename, "w") as f:
        f.write('#!/usr/bin/env python' + '\n' + 'default_parameters = dict('+'\n')
        for i in dict:
            f.write(str(i) + "= \"" + str(dict[i]) + "\"" + ",\n")
        f.write(")")
        f.close()


writeDict(addArg(default_parameters), "../../omics_pipe/parameters/result.py")
