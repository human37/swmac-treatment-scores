### Short Overview

This project was developed by students at Dixie State University. It's goal is to provide the Southwest Mosquito Abatement Center a tool in order to know which mosquito sites to prioritize. We developed a treatment priority score, by looking at the past data the SWMAC center provided us, as well as scientific papers regarding mosquito activity. The input variables our algorithm takes is the temperature and the geography of the station, and uses them to generate numerical scores for each site, with a higher score meaning a higher chance of a mosquito problem. 

### Installing Requirements

The requirements are listed in `requirements.txt`. With `pip`, they can be
easily installed in one command:

`pip3 install -r requirements.txt`.

### Running the Server

The server main is found in `main.py`. It requires Python 3 and can be run
with the following command:

`python3 main.py`.

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
    ├── images
        ├── graph.png
├── templates
│   ├── base.html
│   ├── feed.html
│   ├── infopage.html
│   ├── rankedgraph.html
│   ├── rankedlist.html
│   └── nav.html
├── main.py
├── rankgraph.py
├── scoring_algorithm.py
```

### External Libraries

The following external libraries were used to help make this project.

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
- [matplotlib](https://pypi.org/project/matplotlib/)




