# Software Requirements Specification for Code Connect

Version 1.0 approved

Prepared by <author>
<date created>

## Revision History

- Name, Date, Reason For Changes, Version
-

## 1. Introduction

### 1.1 Purpose

CodeConnect will be created as a way for programmers to connect with each other
and make friends and other people to collaborate and create projects with. 
This will be a social media platform designed specifically for developers to find
other people with certain skill sets that they are searching for.

### 1.2 Document Conventions

Standard Markdown

### 1.3 Intended Audience and Reading Suggestions

This document will be used by the developers of the project in order to stay on track
and have a commmon goal and vision.

### 1.4 Product Scope

This product will provide a platform for developers to connect with each other. 
The goal is for people to be able to form teams and develop cool projects together.

### 1.5 References

None

## 2. Overall Description

### 2.1 Product Perspective

This product will be a standalone social network, and it will not be a part of any bigger organization. It will be web-based, and will follow a similar design to websites like linkedin, or facebook for example. 

### 2.2 Product Functions

- Creating an account unique to the user.
- Connecting with friends or new people met through the service.
- Allowing the user to search by categories such as the type of technology being used, or the product genre.
- Allowing employers to search for candidates for short projects. 
- Allowing people to met new people interested in working on projects together. 


### 2.3 User Classes and Characteristics

The user classes we expect to use our service include:
- Computer Science students.
- Employers needing some work done for a project.
- Self-taught individuals wanting to grow and apply their skills. 

### 2.4 Operating Environment

This product will operate as a web application, allowing desktop computers or mobile phones the ability to use the service. 

### 2.5 Design and Implementation Constraints


- Security (we don’t want our user’s information leaked). 
- Accessibility (we want our web application lightweight and supportive for a variety of users, as well as higher contrast colors to be as visible as possible).


### 2.6 User Documentation

We will provide a document outlining what our service provides for new time users, as well as a document outlining help resources if they run into an issue with the service. 

### 2.7 Assumptions and Dependencies

We plan to use technologies such as python and flask, and those are both open source. So there are no other dependency problems that we know of at this moment. 

## 3. External Interface Requirements

### 3.1 User Interfaces

Our interface will include a webpage that the user can login to to access the product.

### 3.2 Hardware Interfaces

Our product will only be available for PC's and Laptops or anything else that can run the website locally. The website will communicate with the Python code and flask to run the site.

### 3.3 Software Interfaces

Our product will store the data such as, a user's posts, personal information, groups, and messages
using tinydb in python.

### 3.4 Communications Interfaces

Users will be required to have an email, any web browser. Personal data will be encrypted.

## 4. System Features

### 4.1 System Feature 1
- User Profiles
<User Profiles>
Our users will have access to set, change, and delete information on their very own profile. This feature will be available to all users and can be viewed by everyone on the platform.

### 4.1.1 Description and Priority
User profiles are high priority. (7/9)
We want to create a platform capable of sharing and interacting. A good way to achieve this is to have a public profile that serves as an advertisement for an individual.

### 4.1.2 Stimulus/Response Sequences
Users can edit their profile and that will change their data in the backend. "Friends" will be stored along with our user's data. All groups, friends, and any other data will be stored in user's data. An action such as 'adding a friend' will initiate a response for another user. 

### 4.1.3 Functional Requirements
With the use of Flask, html, css we can achieve a 'user's profile'.

### 4.2 System Feature 2
- Rating System
Users will be able to rate other's posts. They are allowed a "same" option.

### 4.2.1 Description and Priority
The rating system is a medium-high priority. (6/9)
We want our users to feel they can change the feel of the platform. By allowing a rating system, users can show others how they feel about other's posts.

### 4.2.2 Stimulus/Response Sequences
Just like all the other user's data, it will be stored in the backend. Wherever a user's post will be stored is where their post's ratings will be. 

### 4.2.3 Functional Requirements
With the use of Flask, html, css we can achieve a 'post rating'.

### 4.3 System Feature 3
- Image support
Users will be able to upload images in their posts. 

### 4.3.1 Description and Priority
Image support is of medium priority. (5/9)
Just as the name says we will allow users to post images of legal size.

### 4.3.2 Stimulus/Response Sequences
Users may add a photo to their post and the data will be stored with all their post information. We will only allow certain file extensions (jpg / png)

### 4.3.3 Functional Requirements
With the use of Flask, html, css we can achieve 'image support'.

## 5. Other Nonfunctional Requirements

### 5.1 Performance Requirements

Access to the internet will be required for useres to conncect with eachother.

### 5.2 Safety Requirements

Since useres code will be publibly deplayed unless otherwise specified, cation should be taken if an individual would like their work to not be copied by others.

### 5.3 Security Requirements

Passwords will be hashed and salted to ensure user user security

### 5.4 Software Quality Attributes
Expect and constantly changing enviroment as new posts come in old posts will be replaced by the new posts but old posts will still be visible

### 5.5 Business Rules

Only useres that have a created acount will be able to sociolize and create connections. no private data will be collected about useres and no data will be used against useres.

## 6. Other Requirements

<Define any other requirements not covered elsewhere in the SRS. This might
include database requirements, internationalization requirements, legal
requirements, reuse objectives for the project, and so on. Add any new sections
that are pertinent to the project.>

## Appendix A: Glossary

<Define all the terms necessary to properly interpret the SRS, including
acronyms and abbreviations. You may wish to build a separate glossary that spans
multiple projects or the entire organization, and just include terms specific to
a single project in each SRS.>

## Appendix B: Analysis Models

<Optionally, include any pertinent analysis models, such as data flow diagrams,
class diagrams, state-transition diagrams, or entity-relationship diagrams.>

## Appendix C: To Be Determined List

<Collect a numbered list of the TBD (to be determined) references that remain in
the SRS so they can be tracked to closure.>
