<?php
include "db.php";

session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit;
}

// Fetch  data from the database
$sql = "SELECT * FROM hospital";
$result = mysqli_query($conn, $sql);

// Create an array to store the fetched  data
$hospitals = [];
while ($row = mysqli_fetch_assoc($result)) {
    $hospitals[] = $row;
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="shortcut icon" href="./assets/logo_ntl.png" type="image/x-icon" />
    <title>Homepage</title>

    <!-- font awesome link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"
        integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA=="
        crossorigin="anonymous"
        referrerpolicy="no-referrer"
    />

    <!-- linking css -->
    <link rel="stylesheet" href="css/afterlogins.css" />
</head>

<body>
    <!-- header section starts -->
    <header>
        <!-- logo and name on left side -->
        <a href="#" class="logo">
            <img src="images/ucl1.png" alt="Hospital" srcset="" />Health Companion</a>
        <div id="menu-bar" class="fas fa-bars"></div>
        <div class="searchbar">
            <input type="search" name="search" id="search" />
            <i class="fa-solid fa-magnifying-glass"></i>
        </div>

        <!-- navigation bar starts -->
        <nav class="navbar">
            <a href="Homepage.php">home</a>
            <a href="#hospitals">Hospital</a>
            <a href="Index.php#review">Service</a>
            <!-- <a href="#gallery">gallery</a> -->
            <a href="Contactus.php">contact</a>
            <a href="bookedhospital.php">Booked Hospital</a>
            <a href="editprofile.php">Edit Profile</a>
            <a href="predict.php">PredictDisease</a>
            <a href="logout.php">Logout</a>
            <a href="#">
                <span text="${userdata.getName()" style="color: black;margin-left: 5px; margin-top: -15px;"></span>
            </a>
        </nav>
        <!-- navigation bar completed -->
    </header>
    <!-- header section ends -->

    <!-- home section starts -->
    <section class="home" id="home">
        <div class="content">
            <h3>Come and be healthy with us. Predict, book, and thrive!</h3>
            <p>
            Experience proactive health management with us. Our system predicts illnesses and streamlines hospital bookings, ensuring timely care. Take charge of your well-being effortlessly. Welcome to a world where staying healthy is simple. Predict, book, and embrace a healthier you!
            </p>
        </div>
        <div class="image">
            <img src="images/one.png" alt="hospital" />
        </div>
    </section>
    <!-- home section comes to an end -->

    <!-- hospital listing started -->
    <section id="hospitals">
        <h1>Here are the currently available Hospitals</h1>
        <div class="all-hospitals">
            <?php foreach ($hospitals as $hospital) : ?>
                <div class="indiviudal-hospital">
                    <img src="<?php echo $hospital['image1']; ?>" alt="<?php echo $hospital['hname']; ?>">
                    <h2><?php echo $hospital['hname']; ?></h2>
                    <p><p>Registration Price</p><?php echo $hospital['regprice']; ?></p>
                    <p><?php echo $hospital['description']; ?></p>
                    <!-- Update the href attribute below to redirect to bookfutsal.php with futsal_id as parameter -->
                    <a href="bookhospital.php?hospital_id=<?php echo $hospital['id']; ?>">Book Hospital</a>
                </div>
            <?php endforeach; ?>
        </div>
    </section>
    <!-- hsopiatl listing ends -->

    <div class="footer" id="foot">
  <div class="inner-footer">

    <!--  for company name and description -->
    <div class="footer-items">
      <h1>Website Name</h1>
      <p>Health Companion</p>
    </div>

    <!--  for quick links  -->
    <div class="footer-items">
      <h3>Quick Links</h3>
      <div class="border1"></div> <!--for the underline -->
      <ul>
        <a href="Homepage.php"><li>Home</li></a>
        <a href="Contactus.php"><li>Contact</li></a>
        <a href="index.php#about"><li>About</li></a>
      </ul>
    </div>

    <!--  for some other links -->
    <div class="footer-items">
      <h3>Services</h3>
      <div class="border1"></div>  <!--for the underline -->
      <ul>
        <a href="#hospitals"><li>Hospital Booking</li></a>
        <a href="#hospitals"><li>Hospital Booking</li></a>
        <a href="#hospitals"><li>Hospital Booking</li></a>
        <a href="#hospitals"><li>Hospital Booking</li></a>
      </ul>
    </div>

    <!--  for contact us info -->
    <div class="footer-items">
      <h3>Contact us</h3>
      <div class="border1"></div>
      <ul>
        <li><i class="fa fa-map-marker" aria-hidden="true"></i>Dillibazar, KTM</li>
        <li><i class="fa fa-phone" aria-hidden="true"></i>123456789</li>
        <li><i class="fa fa-envelope" aria-hidden="true"></i>HealthCompanion@gmail.com</li>
      </ul>

      <!--   for social links -->
      <div class="social-media">
        <a href="https://www.instagram.com/"><i class="fab fa-instagram"></i></a>
        <a href="https://www.facebook.com/"><i class="fab fa-facebook"></i></a>
        <a href="https://www.google.com/"><i class="fab fa-google-plus-square"></i></a>
      </div>
    </div>
  </div>

    <!-- scroll top button  -->
    <a href="#home" class="fas fa-angle-up" id="scroll-top"></a>

    <!-- custom js file link  -->
    <script src="js/script.js"></script>
</body>
</html>
