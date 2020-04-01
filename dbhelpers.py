import time
from tinydb import Query

def new_user(db, username, password):
    users = db.table('users')
    User = Query()
    if users.get(User.username == username):
        return None
    return users.insert({'username': username, 'password': password, 'friends': []})

def get_user(db, username, password):
    users = db.table('users')
    User = Query()
    return users.get((User.username == username) &
            (User.password == password))

def get_user_by_name(db, username):
    users = db.table('users')
    User = Query()
    return users.get(User.username == username)

def delete_user(db, username, password):
    users = db.table('users')
    User = Query()
    return users.remove((User.username == username) &
            (User.password == password))

def add_user_friend(db, user, friend):
    users = db.table('users')
    User = Query()
    if friend not in user['friends']:
        if users.get(User.username == friend):
            user['friends'].append(friend)
            users.upsert(user, (User.username == user['username']) &
                    (User.password == user['password']))
            return 'Friend {} added successfully!'.format(friend), 'success'
        return 'User {} does not exist.'.format(friend), 'danger'
    return 'You are already friends with {}.'.format(friend), 'warning'

def remove_user_friend(db, user, friend):
    users = db.table('users')
    User = Query()
    if friend in user['friends']:
        user['friends'].remove(friend)
        users.upsert(user, (User.username == user['username']) &
                (User.password == user['password']))
        return 'Friend {} successfully unfriended!'.format(friend), 'success'
    return 'You are not friends with {}.'.format(friend), 'warning'

def get_user_friends(db, user):
    users = db.table('users')
    User = Query()
    friends = []
    for friend in user['friends']:
        friends.append(users.get(User.username == friend))
    return friends

def add_post(db, user, text):
    posts = db.table('posts')
    posts.insert({'user': user['username'], 'text': text, 'time': time.time()})

def get_posts(db, user):
    posts = db.table('posts')
    Post = Query()
    return posts.search(Post.user==user['username'])

def add_same(db, post, user):
    posts = db.table('posts')
    users = db.table('users')
    User = Query()
    if user not in posts['sames']:
        posts['sames'].append(user)
        users.upsert(user, (User.username == user['username']) &
                (User.password == user['password']))
        return 'Successfully samed post'
    return "Already samed post"            


def add_language(db, user, language):
    users = db.table('users')
    User = Query()
    if language not in user['languages']:
        user['languages'].append(language)
        users.upsert(user, (User.username == user['username']) &
                (User.password == user['password']))
        return 'Language {} added successfully!'.format(language), 'success'
    return 'You have already added {}.'.format(language), 'warning'


def add_comment(db, post, user, comment):
    if comment == '':
        return 'Empty comment not allowed'
    posts = db.table('posts')
    users = db.table('users')
    User = Query()
    posts['comments'].append([user, comment])
    users.upsert(user, (User.username == user['username']) &
            (User.password == user['password']))
    return 'Successfully commented'
              
def get_comments(db, post):
    posts = db.table('posts')
    comments = []
    for comment in posts['comments']:
        comments.append(posts.get(comment))
    return comments
