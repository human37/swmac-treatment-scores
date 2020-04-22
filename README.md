## Getting Started

### Installing Requirements

The requirements are listed in `requirements.txt`. With `pip`, they can be
easily installed in one command:

`pip3 install -r requirements.txt`.

### Running the Server

The server main is found in `main.py`. It requires Python 3 and can be run
with the following command:

`python3 youface.py`.

## Development

### File Tree

```
.
├── dbhelpers.py
├── db.json
├── README.md
├── requirements.txt
├── static
│   ├── bootstrap.min.css
│   └── youface.css
├── templates
│   ├── base.html
│   ├── feed.html
│   ├── friend.html
│   ├── loggedin.html
│   ├── login.html
│   └── nav.html
└── youface.py
```

### External Libraries

The following external libraries were used to help make this project. Please
refer to their documentation frequently. It will be more useful to you to check
with the documentation before you search Google/StackOverflow. In fact, the more
you practice referencing official documentation, the quicker you'll get at it.
You might eventually find yourself not relying on StackOverflow near as much as
before. I'll include some links with helpful tutorials as well.

- [Flask](https://palletsprojects.com/p/flask/)
    - https://pythonhow.com/flask-navigation-menu/
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
    - https://blog.pythonanywhere.com/121/
- [jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - https://jinja.palletsprojects.com/en/2.11.x/tricks/
    - https://realpython.com/primer-on-jinja-templating/
- [TinyDB](https://pypi.org/project/tinydb/)
    - See examples in dbhelpers.py
- [timeago](https://pypi.org/project/timeago/)

### Database Documents (Objects)

Users

| Key | Type | Description |
| --- | ------ | --- |
| id | int | The user's unique identifier. |
| username | str | The user's unique username. |
| password | str | The user's password. |
| friends | []int | A list of user ids for this user's friends. |

Posts

| Key | Type | Description |
| --- | ------ | --- |
| id | int | The user's unique identifier. |
| user | str | The username of the post creator. |
| text | str | The text of the post. |
| time | float | The timestamp for when the post was created. |
