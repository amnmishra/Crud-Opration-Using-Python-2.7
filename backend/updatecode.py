#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","Task2",3306)
cur=con.cursor()
data=cgi.FieldStorage()
name=data.getvalue('name')
#print name
email=data.getvalue('email')
#print email
number=data.getvalue('number')
#print number

query="update admin set name='"+name+"',number='"+number+"' where email='"+email+"'"
#print query
n=cur.execute(query)
if n==1:
 print "<script>alert('Update Successfull');window.location.href='../user/profile.py?id="+email+"';</script>"
else:
 print "<script>alert('try again');window.location.href='../index.py'</script>"