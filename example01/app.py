from flask import Flask, render_template_string
import os

app = Flask(__name__)

VALID_COLORS = {"red", "green", "blue", "yellow", "black"}
DEFAULT_COLOR = "black"

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Demo Docker ENV</title>
    <style>
        body {
            background-color: {{ color }};
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .info {
            margin-top: 20px;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Demo Docker ENV</h1>
    <div class="info">
        Color actual: {{ color }}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    color = os.getenv("COLOR", DEFAULT_COLOR).lower()
    color = color if color in VALID_COLORS else DEFAULT_COLOR
    return render_template_string(TEMPLATE, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))