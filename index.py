#!C:\Python27\python.exe
print("Content-Type:text/html\n\n")
print ("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/style.css">
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
    <div class="mid">
        <h3>We Are Here to Make Your Idea</h3><br>
        <p>Our Company offers the web development, wordpress development, mobile app development and digital marketing. We are a team who expertise in exploring ideas and developing the tailored digital product for your business strategies. Our team uses the correct strategy, right sources, experiences and tools to deploy your idea into a great application for mobile and web applications that are beyond your thinking and imagination.</p>
    </div>
    <div class="mid">
        <h3>What We Do?</h3><br>
        <p>Our Company is not just Software Development or Web development company in Lucknow, we are a digital agency that believes in innovative, quality delivery within the time with Brand Development. We just focus only on Research, Innovation, and Customization and we always focus on performance by following these three keynotes. We understand the actual requirement and expectation of business and our motive is to deliver the real value for the money within the time by filling the needs of clients. We have a dedicated team for each segment of the web development and designing. Ekana Technologies having a team of those people who follow web designing and development as a passion.
<br>
Our Company offers all kinds of custom web development, eCommerce Development,  WordPress development, WordPress fixing, mobile app development, and digital marketing services for individuals and small to large scale companies.
<br>
We always sharp our skills by learning the latest and trending technologies & methodologies. Be a prominent part of the web development industry, our objective is to deliver the high-end solution with high performance and an extreme level of security.</p>
    </div>



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