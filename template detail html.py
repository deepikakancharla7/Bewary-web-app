<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brewery Detail</title>
</head>
<body>
    <h1>Brewery Detail</h1>
    <!-- Display Brewery Information -->
    <!-- Loop through reviews and display them -->
    {% for review in reviews %}
        <p>
            <strong>Rating:</strong> {{ review.rating }}<br>
            <strong>Description:</strong> {{ review.description }}<br>
        </p>
    {% endfor %}
    <!-- Form to add a new review -->
    <form method="post" action="{{ url_for('brewery_detail', brewery_id=brewery.id) }}">
        <label for="rating">Rating (1-5):</label>
        <input type="number" name="rating" min="1" max="5" required>
        <label for="description">Description:</label>
        <textarea name="description" required></textarea>
        <button type="submit">Add Review</button>
    </form>
    <p><a href="{{ url_for('search') }}">Back to Search</a></p>
</body>
</html>
