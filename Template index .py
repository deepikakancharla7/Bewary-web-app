<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brewery Review System</title>
</head>
<body>
    <h1>Welcome to Brewery Review System</h1>
    {% if current_user.is_authenticated %}
        <p>Hello, {{ current_user.username }}! <a href="{{ url_for('logout') }}">Logout</a></p>
    {% else %}
        <p><a href="{{ url_for('login') }}">Login</a></p>
    {% endif %}
    <p><a href="{{ url_for('search') }}">Search Breweries</a></p>
</body>
</html>
