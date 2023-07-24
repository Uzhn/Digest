from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker

from api.digest import generate_digest_for_user
from app import app
from database.db import Digest, User, session


@app.route('/get_digest/<int:user_id>', methods=['GET'])
def get_user_digest(user_id):
    try:
        digest_for_user = generate_digest_for_user(user_id)
        return jsonify({
            'user_id': user_id,
            'digests': [
                {
                    'content': post.content,
                    'rating': post.rating
                } for post in
                digest_for_user.posts
            ]
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 404


if __name__ == '__main__':
    app.run(port=5000)
