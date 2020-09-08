from .main import app

@app.get('/')
def home():
    return dict(hello='world')
