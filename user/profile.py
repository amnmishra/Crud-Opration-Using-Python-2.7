#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
email=cgi.FieldStorage().getvalue('id')
if email=='':
    print "<script>alert('Error');window.location.href='../index.py';</script>"
con=MySQLdb.connect("127.0.0.1","root","","Task2",3306)
cur=con.cursor()
query="select * from admin where email='"+email+"'"
cur.execute(query)
res=cur.fetchall()
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
print "<a href='../backend/delete.py?id="+(email)+"'>Delete Account</a>"
print "<a href='contactmanagement.py?id="+(email)+"' >Contact Management</a>"
print("""
    
          <a href="../backend/logout.py" class="navigation">Logout</a>
          <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <img src="img/menu.png"></i>
          </a>
      </div>
    </div>
<center>
    <div class="form">
        <h3>Profile</h3>
        <br>
            <table>
               
               
               """)
for r in res:
    print "<tr><td>Name</td><td>" + r[1] + "</td></tr>"
    print "<tr><td>Number</td><td>" + str(r[2]) + "</td></tr>"
    print "<tr><td>E-mail</td><td>" + str(r[3]) + "</td></tr>"
    print "<tr><td>Password</td><td>" + str(r[4]) + "</td></tr>"
    print "<tr><td>Registration Date</td><td>" + str(r[5]) + "</td></tr>"
print("""
               
               
                
            </table>
            
            """)
print "<button><a href='update.py?id="+(email)+"'>Update Profile</a></button>"
print("""
    
         
    </div>
    </center>
<table>



</body>
</html>
""")