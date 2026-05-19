from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>CI/CD Project</title>
        <style>
            body{
                background-color:#0f172a;
                color:white;
                font-family:Arial;
                text-align:center;
                padding-top:100px;
            }
            h1{
                color:#38bdf8;
                font-size:50px;
            }
            .box{
                background:#1e293b;
                width:60%;
                margin:auto;
                padding:30px;
                border-radius:15px;
            }
            p{
                font-size:22px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 End-to-End CI/CD Pipeline</h1>
            <p>✅ Docker Container Running</p>
            <p>✅ Kubernetes Deployment Active</p>
            <p>✅ GitHub Actions Integrated</p>
            <p>✅ AWS EC2 Deployment Successful</p>
            <br>
            <h2>Project By Mamta Gupta</h2>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)