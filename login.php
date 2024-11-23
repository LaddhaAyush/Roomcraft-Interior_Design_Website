<?php
// Start a session to maintain user login status
session_start();
echo '<pre>';
var_dump($_SESSION);
echo '</pre>';
// Database connection parameters
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'wt_cp';

// Create connection to MySQL database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve username and password from POST data
$user_input_username = $_POST['username'] ?? '';
$user_input_password = $_POST['password'] ?? '';

// Check for empty inputs
if (empty($user_input_username) || empty($user_input_password)) {
    echo "Username and password are required.";

    exit;
}

// Prepare a SQL query to get the stored password hash for the given username
$sql = "SELECT username, password FROM users WHERE username = ?";
$stmt = $conn->prepare($sql);

if ($stmt) {
    // Bind the parameter and execute the query
    $stmt->bind_param('s', $user_input_username);
    $stmt->execute();

    // Fetch the result from the query
    $result = $stmt->get_result();

    if ($result->num_rows === 1) {
        // Fetch the user data
        $user_data = $result->fetch_assoc();
        
        // Verify the provided password against the stored hashed password
        if (password_verify($user_input_password, $user_data['password'])) {
            // Login successful: Set session variable for user
            $_SESSION['username'] = $user_data['username']; // Start user session
            echo "Session username set: " . $_SESSION['username']; // Debugging
            header("Location: index.php"); // Redirect to a welcome page or dashboard
            exit;
        } else {
            // Incorrect password
            echo "Invalid username or password.";
        }
    } else {
        // User not found
        echo "Invalid username or password.";
    }

    $stmt->close();
} else {
    echo "Error preparing statement: " . $conn->error;
}

echo '<pre>';
var_dump($_SESSION);
echo '</pre>';

// Close the database connection
$conn->close();
?>
