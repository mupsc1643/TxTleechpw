from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Welcome To Out TxT Leech Page Powered By - @Invisiblebots </title>
	

</head>

<body>
    <div class="container" style="bg-dark text-red text-center py-3 mt-5">
        
            <p>
                  Welcome To Our Page Of Txt Leech Bot Made By -@Invisiblebots 
		  Feature Are That It Download All Url From Your .txt File<br>
                                            For Using And Support Contact @Invisiblebots <br>

                <b>v2.0.0</b>
            </p>
        </a>
    </div>
	<br></br><br></br><br></br>
	<footer class="bg-dark text-white text-center py-3 mt-5">
        Powered By Invisible 
	
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2025 Video Downloader. All rights reserved.
            </p>
        </div>
    </footer></center>
</body>

</html>
"""


if __name__ == "__main__":
    app.run()
