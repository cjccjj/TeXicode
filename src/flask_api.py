# flask_app.py
from flask import Flask, request, jsonify
import re
from texicode import main  # <-- import your CLI script as a module

app = Flask(__name__)

@app.route("/render", methods=["POST"])
def render_tex_string():
    data = request.get_json(force=True)
    tex_input = data.get("input", "")
    debug = bool(data.get("debug", False))
    color = bool(data.get("color", False))

    try:
        result = main.render_tex(tex_input, debug, color, "raw")
        return jsonify({"output": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/markdown", methods=["POST"])
def render_markdown():
    data = request.get_json(force=True)
    content = data.get("content", "")
    debug = bool(data.get("debug", False))
    color = bool(data.get("color", False))

    def replace_latex(match):
        tex_block = match.group(0)
        clean_tex = tex_block.strip('$')
        context = "md_inline"
        if tex_block.startswith('$$') or tex_block.startswith(r'\[') \
           or tex_block.startswith(r'\begin'):
            context = "md_block"
        return main.render_tex(clean_tex, debug, color, context)

    latex_regex = r'\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{.*?\}.*?\\end\{.*?\}'
    new_content = re.sub(latex_regex, replace_latex, content, flags=re.DOTALL)

    return jsonify({"output": new_content})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)