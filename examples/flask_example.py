import flask
from flask import Flask
import dominate.tags as t
import cccp
import os

app = Flask(__name__)


@app.route("/")
def home():
    return t.html(
        [
            t.head(
                [
                    cccp.REQUIRED,
                    cccp.BOOTSTRAP,
                    cccp.CreateReplaceInnerHtmlFunc(),
                    cccp.CreateReplaceOuterHtmlFunc(),
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
                            "/page/1", "pageContent"
                        ),
                    ),
                ], id="wholePage"
            ),
        ]
    ).render()

def mostargs():
    return repr(dict(flask.request.args))


@app.route("/append-page")
def append():
    a = repr({"l": flask.request.args.getlist("l[]")})
    content = f"append called with {a}"
    return cccp.render([t.p(content)])


@app.route("/prepend-page")
def prepend():
    a = mostargs()
    content = f"prepend called with {a}"
    return cccp.render([t.p(content)])


@app.route("/goodbye")
def goodbye():
    with t.body() as body:
        t.h1("Goodbye, CCCP!"),
        t.div("reload page to start again"),
    return body.render()


@app.route("/page/<page_id>")
def page(page_id):
    page_id = int(page_id)
    a = mostargs()
    content = f"{page_id} called with {a}"
    return cccp.render(
        [
            t.p(content),
            t.button(
                f"replace with page {page_id-1}",
                onClick=cccp.replaceHtml(
                    f"/page/{page_id-1}", "pageContent",
                    hello="world"
                ),
            ),
            t.button(
                f"replace with page {page_id+1}",
                onClick=cccp.replaceHtml(
                    f"/page/{page_id+1}", "pageContent"
                ),
            ),
            t.button(
                "append page",
                onClick=cccp.appendHtml(
                    f"/append-page", "pageContent",
                    l=["1","2","3","4","5"],
                ),
            ),
            t.button(
                "prepend page",
                onClick=cccp.prependHtml(
                    f"/prepend-page", "pageContent",
                    more={"hello":"world"}
                ),
            ),
            t.button(
                # replaces whole page
                "Goodbye",
                onClick=cccp.replaceOuterHtml(
                    f"/goodbye", "wholePage",
                ),
            ),
        ]
    )


if __name__ == "__main__":
    import os
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
                            port=9999, debug=True)
