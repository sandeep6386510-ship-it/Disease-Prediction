<?php
include 'db.php';
?>

<!DOCTYPE html>
<html lang="en">


<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" href="images/ucl1.png" type="image/x-icon">
  <title>Landing Page</title>

  <!-- font owesome link -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css"
        integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- liniking css -->
  <link rel="stylesheet" href="css/afterlogins.css">
  <link rel="stylesheet"  href="css/style.css">
</head>

<body>

<!-- header section starts  -->
<header>
  <!-- logo and name on left side -->

  <a href="#" class="logo"><img src="images/ucl1.png" alt="Health Mania" srcset="">Health Companion</a>

  <div id="menu-bar" class="fas fa-bars"></div>

  <!-- navigation bar starts -->
  <nav class="navbar">
    <a href="Homepage.php">home</a>
    <a href="#about">about</a>
    <a href="#review">services</a>
    <a href="#foot">contact</a>
    <a href="login.php">Login</a>
  </nav>

  <!-- navigation bar completed -->

</header>

<!-- header section ends -->

<!-- home section starts -->
<section class="home" id="home">
  <div class="content">
    <h3>Come and be healthy with us. Predict, book, and thrive!</h3>
    <p>Experience proactive health management with us. Our system predicts illnesses and streamlines hospital bookings, ensuring timely care. Take charge of your well-being effortlessly. Welcome to a world where staying healthy is simple. Predict, book, and embrace a healthier you!</p>
    <a href="#about" class="btn">know more</a>
  </div>
  <div class="image">
    <img src="images/one.png" alt="Health Mate">
  </div>
</section>
<!-- home section comes to end -->

<!-- about section start -->
<section class="about" id="about">
  <h1 class="heading">About <span>us</span></h1>
  <div class="whole">
    <div class="img-container">
    <img src="images/k.png" alt="Health Mate">
    </div>
    <div class="description">
      <h3>What is  Health Companion?</h3>
      <P>Health Companion is your personalized health assistant, dedicated to keeping you at your best. By harnessing the power of advanced algorithms and medical expertise, Health Mate empowers you to predict potential diseases, allowing for early intervention and preventive measures. Moreover, with our intuitive hospital booking feature, you can effortlessly schedule appointments and access medical care when you need it most, ensuring peace of mind and timely attention to your health needs.</P>
      <P>Experience the future of healthcare with Health Companion – where predictive analytics meets convenient healthcare access. Take charge of your well-being like never before and embark on a journey towards a healthier, happier you. Join Health Mate today and unlock a world of proactive health management at your fingertips.</P>
    </div>
  </div>
</section>
<!-- about section ends -->
<section class="review" id="review">

  <h1 class="heading"> What we <span>provide?</span> </h1>

  <div class="box-container">

    <div class="box">
      <img src="images/hospital.jpg" alt="">
      <h3></h3>

      <p> Health Companion simplifies hospital booking by seamlessly connecting you with available slots in nearby hospitals. With just a few taps, you can browse through a list of hospitals, check their availability in real-time, and secure your appointment instantly. Skip the queues and uncertainty – With Health Companion, accessing quality healthcare is as easy as booking a ride. Take control of your health journey today.
      </p>
    </div>
    <div class="box">
      <img src="images/pred.jpg" alt="">
      <h3></h3>

      <p> Health Companion revolutionizes healthcare by predicting diseases from symptoms. By inputting your symptoms into our intuitive interface, our sophisticated algorithms analyze the data and generate potential disease predictions. This proactive approach allows for early intervention, enabling you to seek timely medical attention and make informed decisions about your health. With Health Mate, you can stay ahead of illnesses, leading to better health outcomes and improved quality of life.</p>
    </div>
    <div class="box">
      <img src="images/contactus.jpg" alt="">
      <h3></h3>

      <p> We understand that you may have questions or feedback about our
        platform and services, which is why we have a dedicated contact us service to help you out.
        Our customer support team is always ready to assist you with any questions or
        concerns you may have, and we encourage you to reach out to us if you need any assistance
        or have any feedback about our services.
      </p>
    </div>

  </div>

</section>

<!-- review section ends -->

<!-- hsopitals -->
<section id="hospitals">
  <h1>Here are the currently popular  hospitals</h1>

  <div class="all-hospitals">
    <div class="indiviudal-hospital">
      <img src="images/medi.jpg" alt="">
      <h2>Medicity</h2>
      <p>Medicity Hospital in Nepal is a leading healthcare institution renowned for its cutting-edge facilities and expert medical care. Situated in Kathmandu, it houses a diverse team of skilled professionals dedicated to providing comprehensive healthcare services. From routine check-ups to specialized treatments, Medicity Hospital offers personalized care tailored to each patient's needs. With state-of-the-art technology and a patient-centric approach, it ensures top-quality medical treatment in a compassionate environment. As a trusted healthcare provider, Medicity Hospital continues to uphold its commitment to excellence, setting benchmarks in healthcare delivery across Nepal.




</p>
    </div>
    <div class="indiviudal-hospital">
      <img src="images/grande.jpg" alt="">
      <h2>Grande</h2>
      <p>Grande Hospital is a prominent healthcare facility located in Kathmandu, Nepal, renowned for its exceptional medical services and compassionate patient care. With a team of dedicated healthcare professionals, including specialists and support staff, Grande Hospital offers a wide range of medical treatments and services. Equipped with modern technology and advanced infrastructure, the hospital provides comprehensive healthcare solutions to address various medical needs, from routine check-ups to complex surgeries. Patients at Grande Hospital experience personalized care in a comfortable and nurturing environment, ensuring their well-being throughout their medical journey. Committed to excellence and innovation, Grande Hospital continues to be a trusted healthcare destination, delivering superior medical care to the community it serves.</p>
    </div>
    <div class="indiviudal-hospital">
      <img src="images/norvic.jpg" alt="">
      <h2>Norvic</h2>
      <p>Norvic Hospital, situated in Kathmandu, Nepal, stands as a pillar of exceptional medical care and innovation in the region. With a team of highly skilled medical professionals and state-of-the-art facilities, Norvic Hospital offers a comprehensive range of healthcare services, from primary care to specialized treatments and surgeries. Patients benefit from personalized attention and compassionate care, ensuring their comfort and well-being throughout their medical journey. Equipped with cutting-edge technology and modern infrastructure, Norvic Hospital maintains high standards of excellence in healthcare delivery, earning trust and recognition from patients and medical professionals alike. Committed to advancing healthcare standards, Norvic Hospital continues to set benchmarks in quality and innovation, making it a leading healthcare institution in Nepal.</p>
    </div>
  </div>
</section>



<!-- footer -->

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
        <a href="#about"><li>About</li></a>
      </ul>
    </div>

    <!--  for some other links -->
    <div class="footer-items">
      <h3>Services</h3>
      <div class="border1"></div>  <!--for the underline -->
      <ul>
        <a href="login.php"><li>Hospital Booking</li></a>
        <a href="login.php"><li>Hospital Booking</li></a>
        <a href="login.php"><li>Hospital Booking</li></a>
        <a href="login.php"><li>Hospital Booking</li></a>
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