<h1 align="center">Morgan & Co</h1>

[View the live project here.](https://morgan-and-co.herokuapp.com/)

Welcome to the brand new Morgan & Co furniture website.

<!-- <h2 align="center"><img src=""></h2> -->

Milestone Project 4, for [Code Institute](https://codeinstitute.net/)'s Diploma in Web App Development.

Morgan & Co is a family-run furniture retailer based in Wales, UK. The company specializes in sofas, chairs, tables and other home furnishings. For many ficticious years, the company has succesfully operated through word-of-mouth and profiting from a respected family reputation, with steady growth eventually leading them to be a leader in their industry - proudly displaying thier motto of "If it can fit through your front door, we'll sell it - if not, we'll take the door off - free of charge". After a recent family intervention, the company has decided to take a leap of faith into the last century and launch their brand new website to further boost sales.

# Table of Contents
* [Website Concept](#website-concept)
* [Project Goals](#project-goals)
* [User Stories](#user-stories)
    - [As a New User](#as-a-new-user)
    - [As a Returning User](#as-a-returning-user)
    - [As an Admin](#as-an-admin)
* [Aesthetic Design](#aesthetic-design)
    - [Wireframes](#wireframes)
        - [Desktop](#desktop)
        - [Tablet](#tablet)
        - [Mobile](#mobile)
    - [Colour Palette](#colour-palette)
    - [Images](#images)
    - [Font](#font)
* [Database](#database)
    - [Data Schema Design](#data-schema-design)
* [Technical Design](#technical-design)
* [Accessibility](#accessibility)
* [Features](#features)
* [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries, Programs and Tools Used](#frameworks-libraries-programs-and-tools-used)
* [Testing](#testing)
* [Future Updates](#future-updates)
* [Initial Setup and Deployment](#initial-setup-and-deployment)
* [Credits](#credits)

# Website Concept
The website will be a fully-interactive e-commerce website, with the main purpose to drive sales for the company.  
This will be achieved by clearly and smartly displaying their products, company information and further necessary information.

It will also serve as a ____ and to bring more exposure, from otherwise unknown custom and enter a market they currently aren't in. The website will display all products that the company sells, allowing vistors to browse through their vast range. There Visitors can seamlessly browse through the website, through the product range and through specific categories and ranges.

Visitors can sign up for free whcih in turn allows for more features. although sales are not limited to users - a decision that will help easy the sales process - member/signed up users will have features and possibilities that will enhance their experience and decision making - including raising the chances of return custom e.g wishlists, saving profile info and review posting.  
All website features will be documented in this README document.

The website will clearly display information for first-time visitors, returning visitors and customers including the company contact information via social media links and ______ (visible address/About us/Contact us/Contact form). The website is fully responsible on a range of devices - from hand-held devices to larger screens such as monitors and even TVs. This is to ensure that as many people as possible can visit the website.

The website is welcoming to a range of visitors, and gives a very nice user experience with plenty of on-screen prompts (explained here - #Features) on dispaly and a whole host of intuitive, secure technology in the background to ensure a smooth, safe, efficent user-friendly experince.

The website is easily maintainable through the admin portal, but also allows admin/superusers to manage some aspects from the website itself.

Scalable. Add products easily.

[Back to table of contents](#table-of-contents)

# Project Goals
This is the final project for Code Institute's Web Development Diploma course. The task is to build an full-stack e-commerce website that incorporates Django, stripe to handle payments and webhooks.

[Back to table of contents](#table-of-contents)

# User Stories

[Back to table of contents](#table-of-contents)

# Aesthetic Design
## Wireframes
### Desktop
### Tablet
### Mobile
## Colour Palette
## Images
## Font

[Back to table of contents](#table-of-contents)

# Database
The database is setup via a model template.  
Locally, using Django's built-in sqlite.  
Initially using Heroku's postgres add-on database, which eventually was changed to use elephantSQL due to Heroku's announcement to end some of their free-tier services.

## Data Schema Design
The data schema shows how all data is connected. Morgan & Co uses a relational database.
Model breakdown:  
- UserProfile = extends through django's User model.  
- Order =  
- OrderLineItem =  
- Product =  
- Category =  
- Room =  
- Review =  
- Wishlist =  

[Back to table of contents](#table-of-contents)

# Technical Design

[Back to table of contents](#table-of-contents)

# Accessibility

[Back to table of contents](#table-of-contents)

# Features

[Back to table of contents](#table-of-contents)

# Technologies Used
## Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


## Frameworks, Libraries, Programs and Tools Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts is used to import the 'Poppins' font into the style.css file which is used on all fonts within the website.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome is used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery is used to simplify and manipulate some tasks instead of regular JS.
1. [Git:](https://git-scm.com/)
    - Git is used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Gitpod:](https://gitpod.io/)
    - Development environment to build the website.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq is used to create the [wireframes](#wireframes) during the design process.
1. [Eye Dropper:](https://eyedropper.org/).
    - This colour picker tool was used to to pick and experiment with colours.
1. [Coolors:](https://coolors.co/)
    - This tool was used to to setup the colour palette [here](#colour-palette).
1. [TinyPNG:](https://tinypng.com/)
    - TinyPNG is used to optimize images used in the website and documentation.
1. [Miscrosoft Paint:](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9)
    - Microsoft Paint is used to crop and resize images and editing photos for the project.
1. [WPS Office:](https://www.wps.com/)
    - WPS Office is used to create the flow charts, the tables found in the [Testing](TESTING.md) and for spell-checking.
1. [Am I Responsive?:](http://ami.responsivedesign.is/)
    - Used to create the image at the very top of this document.

Other:
- PostgreSQL database - initially though heroku's postgres add-on, then elephantSQL
- PsycoPG2 - database adapter. library for connecting Python to PostgreSQL.
- bootstrap
- heroku
- 

Requirements for Installs:
- asgiref==3.5.2
- boto3==1.26.14
- botocore==1.29.14
- dj-database-url==0.5.0
- Django==3.2.16
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-storages==1.13.1
- gunicorn==20.1.0
- jmespath==1.0.1
- oauthlib==3.2.2
- Pillow==9.3.0
- psycopg2-binary==2.9.5
- python3-openid==3.2.0
- pytz==2022.5
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- sqlparse==0.4.3
- stripe==4.2.0


[Back to table of contents](#table-of-contents)

# Testing

[Back to table of contents](#table-of-contents)

# Future Updates

[Back to table of contents](#table-of-contents)

# Initial Setup and Deployment

[Back to table of contents](#table-of-contents)

# Credits

[Back to table of contents](#table-of-contents)