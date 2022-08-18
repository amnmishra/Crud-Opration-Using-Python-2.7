#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","Task2",3306)
cur=con.cursor()
data=cgi.FieldStorage()
name=data.getvalue('name')
#print name
number=data.getvalue('number')
#print number
email=data.getvalue('email')
#print email
password=data.getvalue('password')
#print msg
q="insert into admin(name,number,email,password,CurDate) values('"+name+"','"+number+"','"+email+"','"+password+"',sysdate())"
#print q
n=cur.execute(q)
if n==1:
 print "<script>alert('Registration Succesfull');window.location.href='../index.py';</script>"
else:
 print "<script>alert('try again');window.location.href='../contact'</script>"