import csv,cgi
from jinja2 import FileSystemLoader,Environment
#import xml.dom.minidom

env = Environment(loader=FileSystemLoader('./'))

data = open('data.csv')
reader = csv.DictReader(data)

skipped_ids = ('GRA01',
'GRA02',
'GRA03',
'GRA04',
'GRA05',
'GRA06',
'GRA07',
'GRA08',
'GRA09',
'GRA10')

users =  [user for user in reader if user['ID1'] not in skipped_ids]
newusers = []
for user in users:
    newuser = {}
    for key in user.keys():
        if key == 'Photo':
            user[key] = user['Last_Name'].lower() +  user['First_Name'][:1].lower() 
        newuser[key] = unicode(cgi.escape(user[key]), errors='ignore')
    newusers.append(newuser)
template = env.get_template('content4.xml.tmpl')
output =  template.render(users=newusers)
print output

#xml = xml.dom.minidom.parse(output)
#print  xml.toprettyxml()

