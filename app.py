from flask import Flask, render_template, request
from collections import Counter
from patterns import patterns

app = Flask(__name__)

def detect_citation_style(citation):
    citation = citation.strip()
    for style, pattern in patterns.items():
        if pattern.match(citation):
            return style
    return "Unknown"

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    style_counts = {}
    warning = ""

    if request.method == "POST":
        text = request.form.get("citations", "")
        citations = [c.strip() for c in text.split("\n") if c.strip()]
        
        results = [(c, detect_citation_style(c)) for c in citations]
        style_counts = Counter(style for _, style in results)

        if len(style_counts) > 1:
            warning = "⚠ Mixed citation styles detected! Consider converting to a single style."
        elif len(style_counts) == 1:
            warning = "✅ All citations appear to follow a consistent style."

    return render_template("index.html", results=results, style_counts=style_counts, warning=warning)

if __name__ == "__main__":
    app.run(debug=True)
