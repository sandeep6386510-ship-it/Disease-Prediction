<?php
include "db.php";

session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit;
}
?>


<!DOCTYPE html>


<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Predicted Page</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.css" />
    <link rel="stylesheet" href="css/afterlogins.css" />
    <link rel="stylesheet" href="css/output.css" />
</head>

<body>
    <header>
        <a href="Homepage.html" class="logo">
            <img src="images/ucl1.png" alt="Hospital" srcset="" />Health Companion
        </a>
        <div id="menu-bar" class="fas fa-bars"></div>
        <div class="searchbar">
            <input type="search" name="search" id="search" />
            <i class="fa-solid fa-magnifying-glass"></i>
        </div>
        <nav class="navbar">
            <a href="homepage.php">home</a>
            <a href="Homepage.php#hospitals">Hospital</a>
            <a href="index.php#review">services</a>
            <!-- <a href="#gallery">gallery</a> -->
            <a href="contactus.php">contact</a>
            <a href="bookedhospital.php">Booked Hospital</a>
            <a href="">
                <span><?php echo $_SESSION['user']['user_name']; ?></span>
            </a>
        </nav>
    </header>

    <div class="container">
        <div class="swiper">
            <div class="swiper-wrapper">
                <!-- Add your swiper content here -->
                <div class="swiper-slide"><img src="images/hos.jpg" alt=""></div>
                <div class="swiper-slide"><img src="images/hos2.jpg" alt=""></div>
                <div class="swiper-slide"><img src="images/hos3.jpg" alt=""></div>
            </div>
            <!-- Add your swiper pagination and navigation here -->
        </div>
    </div>

    <section id="contact-us">
        <span class="big-circle"></span>
        <div class="form">
            <div class="contact-info">
                <h3 class="heading">Result Here</h3>
            <?php
                ini_set('max_execution_time', 500);
                if ($_SERVER["REQUEST_METHOD"] == "POST") {
                // Retrieve input data from form fields
                $symptom1 = isset($_POST['symptom1']) ? strtolower($_POST['symptom1']) : '';
                $symptom2 = isset($_POST['symptom2']) ? strtolower($_POST['symptom2']) : '';
                $symptom3 = isset($_POST['symptom3']) ? strtolower($_POST['symptom3']) : '';
                $symptom4 = isset($_POST['symptom4']) ? strtolower($_POST['symptom4']) : '';
                $symptom5 = isset($_POST['symptom5']) ? strtolower($_POST['symptom5']) : '';
                
                // Create an array of symptom values without keys
                $symptom_values = array();
                if (!empty($symptom1)) {
                    $symptom_values[] = $symptom1;
                }
                if (!empty($symptom2)) {
                    $symptom_values[] = $symptom2;
                }
                if (!empty($symptom3)) {
                    $symptom_values[] = $symptom3;
                }
                if (!empty($symptom4)) {
                    $symptom_values[] = $symptom4;
                }
                if (!empty($symptom5)) {
                    $symptom_values[] = $symptom5;
                }
                
                // Encode the array into JSON
                $symptom_data = json_encode($symptom_values);

                // Set the Flask server URL
                $flask_server_url = 'http://127.0.0.1:5000/predict'; // Change this to match your Flask server URL

                // Initialize cURL session
                $curl = curl_init();

                // Set cURL options
                curl_setopt($curl, CURLOPT_URL, $flask_server_url);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                curl_setopt($curl, CURLOPT_POST, true);
                curl_setopt($curl, CURLOPT_POSTFIELDS, $symptom_data);
                curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

                 // Execute cURL session
                $response = curl_exec($curl);

                // Check for errors
                if ($response === false) {
                 echo "Error: " . curl_error($curl);
                } else {
                 // Output the predicted disease
                $data = json_decode($response, true);
                
                echo "<h2 class='predicted-heading'>Predicted Disease:</h2>";
                if (!empty($data['predicted_disease'])) {
                    $predicted_disease = $data['predicted_disease'];
                    echo "<p class='predicted-disease'>" . $predicted_disease . "</p>";
                } else {
                    echo "<p class='no-prediction'>No prediction available</p>";
                }

                }

    // Close cURL session
                curl_close($curl);
                }
            ?>
            </div>
        </div>
    </section>

    <div class="footer">
        <div class="inner-footer">
            <div class="footer-items">
                <h1>Website Name</h1>
                <p>Health Companion</p>
            </div>
            <div class="footer-items">
                <h3>Quick Links</h3>
                <div class="border1"></div>
                <ul>
                    <a href="homepage.php"><li>Home</li></a>
                    <a href="contactus.php"><li>Contact</li></a>
                    <a href="index.php#about"><li>About</li></a>
                </ul>
            </div>
            <div class="footer-items">
                <h3>Services</h3>
                <div class="border1"></div>
                <ul>
                    <a href="homepage.php#hospitals"><li>Hospital Booking</li></a>
                    <!-- Add more service links if needed -->
                </ul>
            </div>
            <div class="footer-items">
                <h3>Contact us</h3>
                <div class="border1"></div>
                <ul>
                    <li><i class="fa fa-map-marker" aria-hidden="true"></i>Dillibazar, KTM</li>
                    <li><i class="fa fa-phone" aria-hidden="true"></i>123456789</li>
                    <li><i class="fa fa-envelope" aria-hidden="true"></i>HealthCompanion@gmail.com</li>
                </ul>
                <div class="social-media">
                    <a href="https://www.instagram.com/"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.facebook.com/"><i class="fab fa-facebook"></i></a>
                    <a href="https://www.google.com/"><i class="fab fa-google-plus-square"></i></a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.js"></script>
    <script>
        const swiper = new Swiper('.swiper', {
            autoplay: {
                delay: 5000,
                disableOnInteraction: false
            },
            loop: true,
            // Add more swiper options if needed
        });
    </script>

</body>

</html>
