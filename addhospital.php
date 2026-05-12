<?php
include 'db.php';

session_start();
if (isset($_SESSION['user'])) {
    if ($_SESSION["user"]['user_email'] != "admin@admin.com") {
        header('Location: homepage.php');
    }
} else {
    header('Location: homepage.php');
}

if (isset($_SESSION['user'])) {
    if ($_SESSION["user"]['user_email'] != "admin@admin.com") {
        header('Location: homepage.php');
    }
} else {
    header('Location: homepage.php');
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $hname = $_POST["hname"];
    $regprice = $_POST["regprice"];
    $hcontact = $_POST["hcontact"];
    $hlocation = $_POST["hlocation"];
    $description = $_POST["description"];

    $uploadDir = "uploads/";
    $image3 = uploadImage($_FILES["image3"], $uploadDir);
    $image1 = uploadImage($_FILES["image1"], $uploadDir);
    $image2 = uploadImage($_FILES["image2"], $uploadDir);

    $sql = "INSERT INTO hospital (hname, regprice, hcontact, hlocation, description, image3, image1, image2) 
            VALUES ('$hname', '$regprice', '$hcontact', '$hlocation', '$description', '$image3', '$image1', '$image2')";

    if (mysqli_query($conn, $sql)) {
        echo '<script>alert("Hospital added!!")</script>';
        exit();
    } else {
        echo "Error adding Hospital: " . mysqli_error($conn);
    }
}

function uploadImage($file, $uploadDir)
{
    $targetFile = $uploadDir . basename($file["name"]);
    $imageFileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

    $check = getimagesize($file["tmp_name"]);
    if ($check === false) {
        echo "Error: File is not an image.";
        exit();
    }

    if ($file["size"] > 500000) {
        echo "Error: File is too large.";
        exit();
    }

    if ($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg" && $imageFileType != "gif") {
        echo "Error: Only JPG, JPEG, PNG, and GIF formats are allowed.";
        exit();
    }

    if (move_uploaded_file($file["tmp_name"], $targetFile)) {
        return $targetFile;
    } else {
        echo "Error uploading image.";
        exit();
    }
}

?>
<!DOCTYPE html>
<html lang="en">


<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" />
  <link rel="stylesheet" href="css/edithospitals.css">

  <title></title>
</head>

<body>

<div class="insidecontent">
  <h3>Add Hospital to the Website</h3>

  <form method="post" action="" enctype="multipart/form-data">
    <div class="inputsection">
      <div class="name hospital">
        <input type="text" placeholder="Enter the Hospital name" name="hname" required>
      </div>
      <div class="price hospital">
        <input type="text" placeholder="Registration price" name="regprice" required>
      </div>
      <div class="contact hospital">
        <input type="text" placeholder="Contact Number of Hospital" name="hcontact" required>
      </div>
      <div class="location hospital">
        <input type="text" placeholder="Enter the location of Hospital" name="hlocation" required>
      </div>
      <div class="desc hospital">
        <textarea type="text" placeholder="Description About Hospital" name="description" required></textarea>
      </div>
      <div class="photo hospital">
        <input type="file" name="image3" required>
      </div>
      <div class="photo hospital">
        <input type="file" name="image1" required>
      </div>
      <div class="photo hospital">
        <input type="file" name="image2" required>
      </div>
    </div>
    <div class="edit">
      <button type="submit">Add Hospital</button>
    </div>
</form>
</body>
</html>
