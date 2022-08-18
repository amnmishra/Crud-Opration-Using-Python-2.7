#!C:\Python27\python.exe
print("Content-Type:text/html\n\n")
print ("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/style.css">

<style>

</style>

</head>
<body>
    <div class="menu" id="mainmenu">
      <div class="brand"><a href="index.py"><b><h3>Software Service</h3></b></a></div>
      <div class="nav" style="float:right">
          <a href="index.py" class="navigation">Home</a>
          <a href="about.py" class="navigation">About</a>
          <a href="contact.py" class="navigation">Contact</a>
          <a href="registration.py" class="navigation">Registration</a>
          <a href="login.py" class="navigation">Login</a>
          <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <img src="img/menu.png"></i>
          </a>
      </div>
    </div>
    <div class="cover">
        <img src="img/cover.jpg">
    </div>

    <center>
    <div class="login">
        <h3>Login Form</h3>
        <br>
        <form action="backend/logcode.py" method="post">

            <table>
                <tr>
                    <td>Email</td><td><input type="email" name="email" placeholder="Enter Your Name"></td>
                </tr>
              <tr>
                    <td>Password</td><td><input type="password" name="password" placeholder="Enter Your Name"></td>
                </tr>

            </table>

            <input type="submit" Value="Submit" class="btn">
        </form>
    </div>
    </center>




<div class="footer">

<center><p>Copyrights &copy 2022. Design & Developed By : Aman Mishra</p></center>

</div>
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