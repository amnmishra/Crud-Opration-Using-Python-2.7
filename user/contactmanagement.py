#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi, MySQLdb

email = cgi.FieldStorage().getvalue('id')
if email == '':
    print "<script>alert('Error');window.location.href='../index.py';</script>"
con = MySQLdb.connect("127.0.0.1", "root", "", "Task2", 3306)
cur = con.cursor()
query = "select * from admin where email='" + email + "'"
cur.execute(query)
res = cur.fetchall()
print("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="../css/style.css">

</head>
<body>
<div class="menu" id="mainmenu">
      <div class="brand"><a href="index.py"><b><h3>Software Service</h3></b></a></div>
      <div class="nav" style="float:right">
                  """)
print "<a href='../backend/delete.py?id=" + (email) + "'>Delete Account</a>"
print "<a href='contactmanagement.py?id="+(email)+"' >Contact Management</a>"
print("""

          <a href="../backend/logout.py" class="navigation">Logout</a>
          <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <img src="img/menu.png"></i>
          </a>
      </div>
    </div>

        <h3>Contact Management</h3>
        <br>
            <table border="2px">

<tr><td>Name</td><td>Number</td><td>E-mail</td><td>Massage</td><td>Contact Date</td></td>
               """)
query = "select * from contact"
cur.execute(query)
res = cur.fetchall()
for r in res:

    print "<tr><td>" + r[1] + "</td><td>" + str(r[2]) + "</td><td>" + str(r[2]) + "</td><td>" + str(r[4]) + "</td><td>" + str(r[5]) + "</td></tr>"

print("""



            </table>





</body>
</html>
""")