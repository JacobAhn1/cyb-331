<!DOCTYPE html>
<html>
<head>
    <title>Comment Form</title>
</head>
<body>

<h2>Leave a Comment</h2>

<form method="post" action="">
    <label for="comment">Comment:</label><br>
    <textarea name="comment" id="comment" rows="4" cols="50"></textarea><br><br>
    <input type="submit" value="Submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $comment = htmlspecialchars($_POST["comment"]);
    
    echo "<h3>Your Comment:</h3>";
    echo "<p>$comment</p>";
}
?>

</body>
</html>