from flask import Flask, request, render_template
from chapter04.lang_webapp import detect_lang

app = Flask(__name__)


@app.route("/")
def home():
    return "hello, world!"


@app.route("/lang-webapp")
def lang_webapp():
    text = request.args.get("text", "")
    msg = ""
    if text != "":
        lang = detect_lang(text)
        msg = "판정 결과: " + lang
    return """
    <html>
    <body>
        <form>
            <textarea name="text" rows="8" cols="40">{0}</textarea>
            <p><input type="submit" value="판정"></p>
            <p>{1}</p>
        </form>
    </body>
    </html>
    """.format(text, msg)


if __name__ == '__main__':
    app.run(debug=True)
