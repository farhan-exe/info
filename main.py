from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

PRIVATE_KEY = "thug4ff"

@app.route("/api/info", methods=["GET"])
def info():
    uid = request.args.get("uid", "")

    if not uid:
        return jsonify({
            "status": "error",
            "message": "Please provide a UID."
        })

    target_url = f"http://raw.thug4ff.com/info?uid={uid}&key={PRIVATE_KEY}"

    try:
        r = requests.get(
            target_url,
            timeout=15,
            allow_redirects=True,
            verify=False
        )

        # raw response forward করা হচ্ছে (PHP এর মতো)
        return Response(
            r.content,
            status=r.status_code,
            content_type=r.headers.get("Content-Type", "application/json")
        )

    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": f"Request Error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
