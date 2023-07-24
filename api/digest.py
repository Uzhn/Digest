from database.db import User, Digest, session, Post


def generate_digest_for_user(user_id):
    user = session.query(User).get(user_id)
    if not user:
        raise ValueError(f"User with user_id={user_id} not found.")

    subscriptions = user.subscriptions

    posts = []
    for subscription in subscriptions:
        posts.extend(subscription.posts)

    filtered_posts = [post for post in posts if post.rating >= 5]

    existing_digest = session.query(Digest).filter_by(user_id=user_id).first()

    if existing_digest:
        existing_post_ids = [post.id for post in existing_digest.posts]
        new_posts = [post for post in filtered_posts if post.id not in existing_post_ids]
        existing_digest.posts.extend(new_posts)

        session.commit()
        return existing_digest

    digest = Digest(user_id=user_id)
    digest.posts.extend(filtered_posts)

    session.add(digest)
    session.commit()

    return digest
