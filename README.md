# Commerce
A web application based on Django to simulate a eBay-like e-commerce that allow users to post auction listings, place biddings on them,<br>
and add them to 'watchlists'. Additionaly, users can check auction listings created and their current state("running" or "closed").
> Live demo [_here_](http://matheushenriquess.pythonanywhere.com/). <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
  This project was developed during CS50's Web Programming with Python and Javascript [course](https://cs50.harvard.edu/web/2020/). The focus of this project is to flex SQL and Database skills. Futhermore, it was necessary to apply some basic web programming features as live bidding and commentary box, as well, as watchlist.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- [Django - version 4.0.3](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [sqlite3](https://www.sqlite.org/index.html) - QLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.
- [jQuery - Ajax](https://jquery.com/) - jQuery simplifies HTML document traversing, event handling, animating, and Ajax interactions for rapid web development.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains HTML, CSS and Javascript-based design templates.


## Features
- Create auction listings
- Place bids on auctions
- Add commentary
- Create watchlist
- Check created auctions


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
- Clone the project:
  ```
    git clone https://github.com/MatheusHenriqueSS/commerce.git
  ```
- Download Django:
  ```
    pip install Django==4.0.3
  ```
- Make migrations:
  ```
    python manage.py makemigrations
  ```
- Migrate:
  ```
    python manage.py migrate
  ```
- Run the application:
  ```
    python manage.py runserver
  ```

## Project Status
Project is: _in progress_.


## Room for Improvement

Room for improvement:
- Website design
- Commentary updating with jquery(ajax)

To do:
- Add more aesthetics design
- Add current commentary without reloading page


## Acknowledgements
Huge thanks for Brian, David and all CS50 staff for host a free online course with such a level of excellence.


## Contact
Created by [@MatheusH](https://www.linkedin.com/in/matheus-hss/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
