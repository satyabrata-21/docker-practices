# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Love Couple Page</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fad0c4);
    overflow-x:hidden;
}

/* Hero */
.hero{
    height:100vh;
    background:url('https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
    display:flex;
    justify-content:center;
    align-items:center;
    position:relative;
    text-align:center;
}

.hero::before{
    content:"";
    position:absolute;
    inset:0;
    background:rgba(0,0,0,0.45);
}

.hero-content{
    position:relative;
    z-index:2;
    color:white;
    animation:fadeIn 2s ease;
}

.hero h1{
    font-size:70px;
    margin-bottom:20px;
    text-shadow:0 0 20px rgba(255,255,255,0.6);
}

.hero p{
    font-size:24px;
}

/* Gallery */
.section{
    padding:70px 40px;
    text-align:center;
}

.section h2{
    font-size:45px;
    color:#fff;
    margin-bottom:40px;
}

.cards{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:30px;
}

.card{
    background:white;
    border-radius:20px;
    overflow:hidden;
    box-shadow:0 15px 30px rgba(0,0,0,0.25);
    transform-style:preserve-3d;
    transition:0.4s;
}

.card:hover{
    transform:rotateY(10deg) rotateX(10deg) scale(1.05);
}

.card img{
    width:100%;
    height:320px;
    object-fit:cover;
}

.card h3{
    padding:18px;
    color:#e11d48;
}

.footer{
    text-align:center;
    padding:30px;
    color:white;
    font-size:18px;
}

/* Animation */
@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(40px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}
</style>
</head>

<body>

<section class="hero">
    <div class="hero-content">
        <h1>❤️ Forever Together ❤️</h1>
        <p>A beautiful journey of love and memories</p>
    </div>
</section>

<section class="section">
    <h2>3D Couple Moments</h2>

    <div class="cards">

        <div class="card">
            <img src="https://images.unsplash.com/photo-1522673607200-164d1b6ce486?auto=format&fit=crop&w=900&q=80">
            <h3>Romantic Walk 🌹</h3>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80">
            <h3>Sunset Love 🌅</h3>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=900&q=80">
            <h3>Forever Bond 💍</h3>
        </div>

    </div>
</section>

<div class="footer">
Made with Love 💖 | Flask Web App
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
