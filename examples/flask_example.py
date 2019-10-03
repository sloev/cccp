from flask import Flask
from flask_cors import CORS
import dominate.tags as t
import cccp

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return t.html(
        [
            t.head(
                [
                    cccp.REQUIRED,
                    cccp.BOOTSTRAP,
                    cccp.CreateReplaceHtmlFunc(),
                    cccp.CreateAppendHtmlFunc(),
                    cccp.CreatePrependHtmlFunc(),
                ]
            ),
            t.body(
                [
                    t.h1("Hello, CCCP!"),
                    t.div(id="pageContent"),
                    t.button(
                        "go to blog",
                        onClick=cccp.replaceHtml(
                            "http://127.0.0.1:9999/page/1", "pageContent"
                        ),
                    ),
                ]
            ),
        ]
    ).render()


@app.route("/append-page")
def append():
    content = f"this is appended"
    return cccp.render([t.p(content)])


@app.route("/prepend-page")
def prepend():
    content = f"this is prepended"
    return cccp.render([t.p(content)])


@app.route("/page/<page_id>")
def page(page_id):
    page_id = int(page_id)
    content = f"this is page {page_id}"
    return cccp.render(
        [
            t.p(content),
            t.button(
                f"replace with page {page_id-1}",
                onClick=cccp.replaceHtml(
                    f"http://127.0.0.1:9999/page/{page_id-1}", "pageContent"
                ),
            ),
            t.button(
                f"replace with page {page_id+1}",
                onClick=cccp.replaceHtml(
                    f"http://127.0.0.1:9999/page/{page_id+1}", "pageContent"
                ),
            ),
            t.button(
                "append page",
                onClick=cccp.appendHtml(
                    f"http://127.0.0.1:9999/append-page", "pageContent"
                ),
            ),
            t.button(
                "prepend page",
                onClick=cccp.prependHtml(
                    f"http://127.0.0.1:9999/prepend-page", "pageContent"
                ),
            ),
        ]
    )


if __name__ == "__main__":
    app.run(port=9999, debug=True)
