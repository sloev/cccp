from string import Template
from dominate.tags import script, link, style
from dominate.util import raw


REQUIRED = [
    script(
        src="https://unpkg.com/axios@0.19.0/dist/axios.min.js", crossorigin="anonymous"
    ),
    script(
        src="https://code.jquery.com/jquery-3.3.1.slim.min.js",
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo",
        crossorigin="anonymous",
    ),
]

BOOTSTRAP = [
    link(
        rel="stylesheet",
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T",
        crossorigin="anonymous",
    ),
    script(
        src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js",
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1",
        crossorigin="anonymous",
    ),
    script(
        src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js",
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM",
        crossorigin="anonymous",
    ),
]


def render(x):
    if isinstance(x, list):
        return "".join(e.render(pretty=False) for e in x)
    return x.render(pretty=False)


class CustomTemplate(Template):
    delimiter = "$$"


class JavaScript:
    defaults = None
    js_source = ""

    def render(self, values, with_script_tag=True):
        template = CustomTemplate(self.js_source)
        rendered = raw(template.substitute(values).strip())
        if with_script_tag:
            return script(rendered, type="text/javascript")
        else:
            return rendered

    def __new__(cls, with_script_tag=True, **kwargs):
        values = cls.defaults or {}
        values.update(kwargs)
        inst = super(JavaScript, cls).__new__(cls)
        return inst.render(values, with_script_tag)


class CreateReplaceHtmlFunc(JavaScript):
    js_source = """
    function ReplaceHtml(url, id){
        axios.get(url)
        .then(function (response) {
            document.getElementById(id).innerHTML = response.data;
        });
    };
    """


def replaceHtml(url, id):
    return f"ReplaceHtml('{url}', '{id}')"


class CreateAppendHtmlFunc(JavaScript):
    js_source = """
    function AppendHtml(url, id){
        axios.get(url)
        .then( function (response) {
            $("#"+id).append(response.data);
        });
    };
    """


def appendHtml(url, id):
    return f"AppendHtml('{url}', '{id}')"


class CreatePrependHtmlFunc(JavaScript):
    js_source = """
    function PrependHtml(url, id){
        axios.get(url)
        .then( function(response) {
            $("#"+id).prepend(response.data);
        });
    };
    """


def prependHtml(url, id):
    return f"PrependHtml('{url}', '{id}')"


class CreateRemoveHtmlFunc(JavaScript):
    js_source = """
    function RemoveHtml(id){
        $("#"+id).remove();
    };
    """


def removeHtml(id):
    return f"RemoveHtml('{id}')"


def chain_functions(*function_strings):
    return "; ".join(function_strings) + ";"


def style_tag_with_css(css):
    return style(css)
