from flask import Flask, request, jsonify
import parser as parse


app = Flask(__name__)


@app.route('/parse', methods=['GET'])
def parse_url():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400

    try:
        parsed_data = parse.parse_url(url)
        return jsonify(parsed_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
