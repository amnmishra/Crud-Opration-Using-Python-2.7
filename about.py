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
        <h3>Our Company</h3><br>
        <p>
<ul>
    <li>Fresh Ideas</li>
</ul>        
Our capability is in providing innovative tech solutions for business thoughts according to your perception. Starting from a flexible and convenient layout to the multipurpose settlement of structures, we have an enhanced accumulation of designs that accommodate your creative endeavors.
<ul>
    <li>Unique Designs</li>
</ul>
Our design structure supports the key methodology of the people in business by featuring the knowledge and motivation of the plan to accomplish special desires and objectives.
<ul>
    <li>Organized Implementation</li>
</ul>

Organized Implementation is the most conspicuous procedure of incorporating a recently developed technically specialized software solution for a business where the standardized MVC format is followed which intensely relies upon the architecture of the solution. Our methodology is to make the created programming software adaptable, bug-free and smooth so that it supports all the platforms.
<ul>
    <li>Target-Oriented Solution</li>
</ul>

Our aim is to design and develop software solutions according to the set of objectives you follow in your business. As a software development company, our entire focus is on deploying software solutions that resemble the business approach.
        
        
        
        
        
        
        
        
        
        
        </p>
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