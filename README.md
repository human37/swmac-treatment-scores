### Overview

This project was developed by students at Dixie State University. It's goal is to provide the Southwest Mosquito Abatement Center a tool in order to know which mosquito sites to prioritize. We developed a treatment priority score, by looking at the past data the SWMAC center provided us, as well as scientific papers regarding mosquito activity. Our algorithm takes temperature and geography of the site as input, and uses them to generate numerical scores for each site, with a higher score meaning a higher chance of a mosquito problem. This tool can assist in making the SWMAC treatment methods more cost effective. 

More information about the project can be found [here.](https://docs.google.com/document/d/1jZDWjx4b_Sxw5XU-NHvDYFSn1iXNnFA3rUbeUMOyN1I/edit?usp=sharing)

This project is currently deployed on Microsoft Azure, and can be found [here.](http://swmactreatmentscores.azurewebsites.net/)

### Installing Requirements

The requirements are listed in `requirements.txt`. In order to install run:

`pip install -r requirements.txt`.

### Running the Server

The server main is found in `application.py`. It requires Python 3 and can be run
with the following command:

`python3 application.py`.


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
        ├── mosq_temp.png
├── templates
│   ├── base.html
│   ├── feed.html
│   ├── infopage.html
│   ├── rankedgraph.html
│   ├── rankedlist.html
│   └── treatment.html
├── application.py
├── rankgraph.py
├── scoring_algorithm.py
```




