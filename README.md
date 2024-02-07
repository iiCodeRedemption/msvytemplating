# MSVY Templating

## A simple HTML templating engine created in 50 lines of code!

### Setup

To use MSVY Templating in your project, you can install it via pip. Navigate to your project directory and run the following command:

```bash
pip install /path/to/msvytemplating
```

Replace `/path/to/msvytemplating` with the actual path to the directory containing the `setup.py` file of the MSVY Templating library.

### Example Usage

To illustrate how to use MSVY Templating, consider the following example:

```python
API_URL = "https://jsonplaceholder.typicode.com/users"

@app.route("/")
def home():
    # Define context with dynamic data
    context = {
        "pageTitle": "My Custom Page",
        "siteName": "MySite",
        "aboutContent": "Here is some information about us.",
        "contactEmail": "contact@mysite.com",
        "users": []
    }
    
    # Fetch data from an API and handle errors (if any)
    response = requests.get(API_URL)
    response.raise_for_status()
    users = response.json()

    # Add fetched data to the context (first 5 users)
    context["users"] = users[:5]

    # Render the template using MSVYEngine
    rendered_html = msvy_engine.render_template("index.msvy", **context)
    return render_template_string(rendered_html)
```

In this example, we define a Flask route that fetches user data from an API, adds it to the context, and renders the `index.msvy` template using MSVY Templating. The rendered HTML is then returned as the response.

### Project Example

Here's an example that demonstrates the syntax and features of MSVY Templating within a project:

`static/css/styles.css`

```css
body {
  font-family: Arial, sans-serif;
}

header {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
}

section {
  padding: 20px;
}

footer {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 5px 0;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 10px;
}

.card {
  background-color: #f9f9f9;
  padding: 10px;
  margin: 10px 0;
}
```

`templates/index.msvy`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Replace with your own styles -->
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/styles.css') }}"
    />
    <title>{{ $pageTitle }}</title>
  </head>
  <body>
    <header>
      <h1>Welcome to {{ $siteName }}</h1>
    </header>
    <section>
      <h2>About Us</h2>
      <p>{{ $aboutContent }}</p>
      <h3>Our Team</h3>
      <ul>s
        <div class="grid">
          {% for $user in $users %}
            <div class="card">
              <li>
                <strong>{{ $user.name }}</strong>
                <p>{{ $user.email }}</p>
              </li>
            </div>
          {% endfor %}
        </div>
      </ul>
    </section>
    <footer>
      <p>Contact us: {{ $contactEmail }}</p>
    </footer>
  </body>
</html>
```

These files demonstrate how placeholders and loops can be used within the HTML structure to create dynamic content.
