<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brewery Search</title>
</head>
<body>
    <h1>Brewery Search</h1>
    <form method="post" action="{{ url_for('search') }}">
        <label for="city">Search by City:</label>
        <input type="text" name="city" required>
        <button type="submit">Search</button>
    </form>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</body>
</html>
