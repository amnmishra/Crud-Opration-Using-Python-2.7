#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","Task2",3306)

data=cgi.FieldStorage()
#print w
email=data.getvalue('email')
#print e
password=data.getvalue('password')
#print p

query="select * from admin where email='"+email+"' and password='"+password+"'"
#print query
cur=con.cursor()
a=cur.execute(query)
if a==1:
	print "<script>alert('Login Successfull');window.location.href='../user/profile.py?id="+email+"';</script>"
else:
	print "<script>alert('Login Not Successfull');window.location.href='customerlogin.py';</script>"