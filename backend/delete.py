#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
email=cgi.FieldStorage().getvalue('id')
#print email
con=MySQLdb.connect("127.0.0.1","root","","Task2",3306)
cur=con.cursor()

query="delete from admin where email='"+email+"'"

n=cur.execute(query)
if n==1:
 email=''
 print "<script>alert('Delete Your Account');window.location.href='../index.py;</script>"
else:
 print "<script>alert('try again');window.location.href='../index.py'</script>"