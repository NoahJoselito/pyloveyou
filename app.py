from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>I Love You</title>
    <style>
        body { margin: 0; background-color: black; color: #ffb6c1; text-align: center; font-family: Arial, sans-serif; overflow: hidden; }
        canvas { display: block; margin: 0 auto; }
    </style>
</head>
<body>
    <canvas id="heartCanvas"></canvas>

    <script>
        const canvas = document.getElementById('heartCanvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        ctx.fillStyle = "#ffb6c1";
        ctx.font = "bold 8px Arial";
        ctx.textAlign = "center";

        let scale = 11;
        let i = 0;

        function drawStep() {
            if (scale > 16) return;

            let angle = i * (Math.PI * 2) / 120;
            let x = 16 * Math.pow(Math.sin(angle), 3) * scale;
            let y = -(13 * Math.cos(angle) - 5 * Math.cos(2 * angle) - 2 * Math.cos(3 * angle) - Math.cos(4 * angle)) * scale;

            ctx.fillText("I love you", centerX + x, centerY + y);

            i++;
            if (i >= 120) {
                i = 0;
                scale++;
            }
            setTimeout(drawStep, 10);
        }

        drawStep();
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run()