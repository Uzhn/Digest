import json

from database.db import Post, Subscription, User, session


def load_test_data_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    users_data = data.get('users', [])
    subscriptions_data = data.get('subscriptions', [])
    posts_data = data.get('posts', [])

    for user_data in users_data:
        user = User(id=user_data['id'], name=user_data['name'])
        session.add(user)

    for subscription_data in subscriptions_data:
        subscription = Subscription(id=subscription_data['id'],
                                    source_name=subscription_data['source_name'])
        subscription.subscribers = [user for user in session.query(User).filter(
            User.id.in_(subscription_data['subscribers']))]
        session.add(subscription)

    for post_data in posts_data:
        post = Post(id=post_data['id'], content=post_data['content'],
                    rating=post_data['rating'], subscription_id=post_data['subscription_id'])
        session.add(post)

    session.commit()


if __name__ == "__main__":
    json_file = 'fixtures/test_data.json'
    load_test_data_from_json(json_file)
    print('---Test data was successfully loaded into the database.---')
