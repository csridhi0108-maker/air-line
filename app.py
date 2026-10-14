import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Local dev only. On Render, gunicorn serves `wsgi:app` (see render.yaml / Procfile).
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1" or "PORT" not in os.environ)
