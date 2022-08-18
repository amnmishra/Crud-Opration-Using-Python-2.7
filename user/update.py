#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
email=cgi.FieldStorage().getvalue('id')
con=MySQLdb.connect("127.0.0.1","root","","Task2",3306)
cur=con.cursor()
query="select * from admin where email='"+email+"'"
cur.execute(query)
res=cur.fetchall()
print ("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="../css/style.css">

<style>

</style>

</head>
<body>

<div class="menu" id="mainmenu">
      <div class="brand"><a href="index.py"><b><h3>Software Service</h3></b></a></div>
      <div class="nav" style="float:right">
                  """)
print "<a href='../backend/delete.py?id="+(email)+"'>Delete Account</a>"
print("""
   
          <a href="../backend/logout.py" class="navigation">Logout</a>
          <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <img src="img/menu.png"></i>
          </a>
      </div>
    </div>
    <center>
    <div class="form">
        <h3>Update Profile</h3>
        <br>
        <form action="../backend/updatecode.py" method="post">

            <table>
            """)
for r in res:

    print "<tr><td>Name</td><td><input type='text' name='name' placeholder='Enter Your Name' value='"+r[1]+"'></td></tr>"
    print "<tr><td>Number</td><td><input type='number' name='number' placeholder='Enter Your Number' value='"+str(r[2])+"'></td></tr>"
    print "<input type='email' name='email' value='"+email+"' style='display:none;'></td></tr>"


print("""
            </table>

            <input type="submit" Value="Update" class="btn">
        </form>
    </div>
    </center>





<script>
function myFunction() {
  var x = document.getElementById("mainmenu");
  if (x.className === "menu") {
    x.className += " responsive";
  } else {
    x.className = "menu";
  }
}
</script>
</body>
</html>
""")