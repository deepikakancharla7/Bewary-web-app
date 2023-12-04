<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brewery Search Results</title>
</head>
<body>
    <h1>Brewery Search Results</h1>
    {% for brewery in breweries %}
        <p>
            <strong>Name:</strong> {{ brewery.name }}<br>
            <strong>Address:</strong> {{ brewery.address }}<br>
            <strong>Phone:</strong> {{ brewery.phone }}<br>
            <strong>Website:</strong> <a href="{{ brewery.website_url }}">{{ brewery.website_url }}</a><br>
            <strong>Rating:</strong> {{ brewery.rating }}<br>
            <strong>State, City:</strong> {{ brewery.state }}, {{ brewery.city }}<br>
        </p>
    {% endfor %}
    <p><a href="{{ url_for('search') }}">Back to Search</a></p>
</body>
</html>
