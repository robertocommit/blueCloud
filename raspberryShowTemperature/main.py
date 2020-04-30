from google.cloud import firestore
client = firestore.Client()

start_html = """
    <!DOCTYPE html>
        <html lang="en-US">
        <head>
            <style>
                header {
                    font-size: 150px;
                    margin-bottom: 3%;
                    text-style: bold;
                    text-align: center;
                    }

                .button {
                    background-color: #A9A9A9;
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    font-size: 80px;
                    margin: 4px 2px;
                    cursor: pointer;
                    width: 100%;
                    }

                .button:hover {
                    background-color: #F0FFFF;
                    color: black;
                    }

            </style>
            <script>
                function setStatus(status) {
                    var url = 'GOOGLE_CLOUD_FUNCTION_URL' + status; 
                    fetch(url)
                    .then((res) => res.json())
                    .then(output => {
                        var response;
                        })}
            </script>
            <title>Temperature</title>
        </head>
        <body>
            <header>
                <p>"""
end_html = """
     </p>
    </header>
    <button  class="button" onclick="setStatus('a')">a</button>
    <button  class="button" onclick="setStatus('A')">A</button>
  </body>
</html>"""


def show_temperature(request):
    users_ref = client.collection('temperatures')
    docs = users_ref.get()
    temperatures = [i.to_dict() for i in docs][0]
    temperature = temperatures['temperatura']
    output = start_html + 'temperature: ' + temperature + end_html
    return str(output)
