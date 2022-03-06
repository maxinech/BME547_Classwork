# server.py
from blood_calculator import check_HDL
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def status():
    return "Server Om"


@app.route("/info", methods=["GET"])
def info():
    out_string = "This is a test server for class.\n"
    out_string += "This would tell us how to work."
    return out_string


@app.route("/hdl_check", methods=["POST"])
def check_HDL_from_internet():
    """
    input_json = {"name": <patient_name_string>,
                  "hdl_result": <hdl_int>}
    :return:
    """
    in_data = request.get_json()
    hdl_value = in_data["hdl_result"]
    answer = check_HDL(hdl_value)
    print("The answer is {}".format(answer))
    return answer


@app.route("/add", methods=["POST"])
def add():
    """
    {"a": <int>, "b": <int>}
    :return:
    """
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    answer_json = [in_data["a"], in_data["b"], answer]
    return jsonify(answer_json)


@app.route("/add/<a>/<b>")
def add_2(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
