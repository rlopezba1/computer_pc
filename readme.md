# Computer Pc

## Code Institute: Milestone Project 4

![Computer PC Responsive Design](https://github.com/rlopezba1/cook_book/blob/master/static/img/responsive_img.png)

*The Cook Book* is an online cookbook that helps people share recipes, create, edit or delete recipes. My goal with this project was to create an intuitive website, useful for people looking for cooking ideas and people who want to share their knowledge.

I am a cooking and food lover. I like to cook and I always look for recipes on the internet that help me to better prepare the dishes.

[Here the full project live.](https://cook-book-ruben.herokuapp.com/)

## Table of contents

- [**UX**](#UX)
    - [Main aims](#Main-aims)
    - [User Stories](#User-Stories)
        - [New Users](#New-Users)
        - [Returning Users](#Returning-Users)
        - [Frequent User](#Frequent-User)
    - [Design Process](#Design-Process)
- [**Features**](#Features)
    - [Database structure](#Database-structure)
    - [Existing features](#Existing-features)
    - [Features left to implement](#Features-left-to-implement)
- [**Technologies used**](#Technologies-used)
- [**Testing**]
- [**Deployment**](#Deployment)
- [**Credits**](#Credits)
    - [Images](#Images)
    - [Acknowledgements](#Acknowledgements)

## UX

### Main aims

- To create a website for people looking for recipes and for people who want to share knowledge

- Users can search, create, edit or delete recipes, create their own account

- Navigation must be intuitive and simple, so that the user finds the recipes easily and can act simply.

### User Stories

- I would like people to contribute with recipes so that people can enjoy them, with quick and easy access.

#### New Users

- I am a user who loves cooking  and I would like to find an online cookbook where I can store and find new recipes.
- I am a user who loves cooking  and I would like to find an online cookbook where I can get new ideas

#### Returning Users

- I am a user who frequently upload recipes and I want to see what recipes people upload
- I am a user who wants to update the recipe that I uploaded, since I have tried new ingredients and the result is better.

#### Frequent User

- As a frequent user, I want to go back to the website and see the new recipes that people have uploaded and / or add new recipes.

### Design Process

#### Design Process: UX Research

- The design had to be simple so that users were direct to find what they were looking for, without too many detours

#### Design process: UX Design

1. Strategic plan: I don't know of any website that allows you to upload recipes and share them. It seems like a very good idea to me, but it has to be something simple so that users collaborate in a fluid way.

2. Scope map: The user must easily find the recipes, and those who collaborate by adding more recipes, must be able to create, edit or delete them quickly and easily.

3. Structure plan: The navigation bar will be the one that directs the user depending on what he wants to do. Search recipes, go to your profile, add recipes, go to the product list, or log out. If you are not registered you can register and log in

4. Skeleton plan: For the average user, the important thing is to find the recipe that he needs. Therefore, the search is essential and that is why it occupies a prominent position on the page. Then the recipes appear so that he can find the one he is looking for.

5. Surface plan: The colors used are elegant and bright, which are combined throughout the web. The font used is Arial, very familiar to all users.



## Features

### Existing Features

#### Wireframes

[wireframes](https://github.com/rlopezba1/cook_book/blob/master/static/documentation/cook_book.pdf)

#### Database structure

MongoDB database has been chosen for the project and locates the 3 collections
- * Categories * - This collection stores the different categories of recipes that are generally based on fish, meat, pasta, desserts
- * Foods * - When a user uploads a recipe, the data is sent to this collection with the following information: the name of the recipe, the category, brief description, and finally the image of the recipe, and the user profile that created the recipe.
- * Users *: this collection stores the user's username and encrypted password

#### Consistent features across all pages

- The navbar is visible and responsive in every page, and when the user scrolls down it turns into white and follows the navigation.
- All the 'Add Recipe' and 'Go Back' / 'Cancel' buttons areof the same color throughout the design, the only exception is the one in the user profile, but it gets the typical green color when hovered.
- All the flash messages appear with the same color and font throughout the app.

#### Homepage

- There are two images of people enjoying their time and a brief explanation of the web
- Continuing, the user can see the ["Enjoying cooking"](https://github.com/rlopezba1/cook_book/blob/master/static/img/pexels-elle-hughes-2696064.jpg)

#### Recipes

- On this page you can find all the recipes, both those created by the user and by other users. There is the search option to find the recipe by name or by parts of the definition, for example looking for the name of an ingredient. There is the option to edit or delete the recipes themselves.

#### Single recipe

- This page shows the user the image of the recipe on a card, and next to the user you can see the category and the username that created the recipe.

- Below this section, the user can read the brief description of the recipe, the list of ingredients and the preparation

#### Products

- This page offers the products promoted by Ikea to the user with related images and a brief explanation of the product, with a link that it sends to the seller. There is a brief explanation on the back of the card.

#### Login

- If any of the username / password combinations are incorrect, the user receives a flash message suggesting that one or both of the entries are incorrect.

- If the user does not have an account, he can register a button through

#### Register

- New users can create an account by providing username and password. If you are already registered you will be notified.

#### Profile

- On the profile page, user information appears and the option to start publishing recipes. You are redirected to the 'Profile' page which includes the section with the button to add a new recipe.

#### Add recipe

- This page allows the user to add a new recipe. You have to fill in a form with all the recipe data such as name, category, a brief description, the ingredients and the preparation steps.

#### Edit recipe 

- If the user created a recipe, he can decide to Edit or Delete that recipe. On the Edit page, the user gets all the current recipe data and can decide to add or change ingredients or any other input that the user decides to change.
- In the Edit form, the user has the options to save the changes or cancel the actions through two buttons.

### Features Left to implement

- There are still many potential implementations to be developed on this website, such as implementing recipe ratings to find out which ones have the most scores, or adding weekly menus.

## Technologies Used

### Languages, libraries, databases, frameworks, editors and version control

- [HTML5](https://html.com/)

- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)

- [Javascript](https://www.javascript.com/)

- [jQuery](https://jquery.com/)

- [Python](https://www.python.org/)

- [Pymongo](https://pymongo.readthedocs.io/en/stable/)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

- [MongoDB](https://www.mongodb.com/)

- [Materialize](https://materializecss.com/)

- [Gitpod](https://www.gitpod.io/)

- [Git Version Control](https://git-scm.com/)

- [GitHub](https://github.com/)

- [Heroku](https://www.heroku.com/)

### Additional tools


- [FontAwesome](https://fontawesome.com/) 
    * I relied on free FontAwesome icons for this project.
- [Google Fonts](https://fonts.google.com/)
    * I used two complementary fonts from Google for my project.
- [Pexels](https://www.pexels.com/)
    * This website was one of the sources for the images contained throughout the project.
- [Am I Responsive](http://ami.responsivedesign.is/)
    * This website was used to implement the responsive image of my website in the project. 
- [W3C Markup Validation Service](https://validator.w3.org/) 
    * This was a great tool throughout the project to check whether there were any errors in my HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    * This was a great tool throughout the project to check whether there were any errors in my CSS code.
 - [JSHint](https://jshint.com/) 
    * This tool helped me test my JavaScript and jQuery code. 
- [PEP 8 online](http://pep8online.com/)
    * I used PEP 8 to check that my Python code complied with formatting standards. 

## Testing

- Validating HTML, CSS, JavaScript and Python
- Checking responsiveness of design on all screen sizes
- Manually testing the functionality of all links

- [Validating HTML](https://github.com/rlopezba1/cook_book/blob/master/static/img/html_testing.png)
- [Validating CSS](https://github.com/rlopezba1/cook_book/blob/master/static/img/css_validation.png)
- [Validating JS](https://github.com/rlopezba1/cook_book/blob/master/static/img/js_validation.png)


In the case of html, the errors are given by the loops and blocks of jinja

I manually tested the project on the following web browsers, checking that all aspects worked :
- Google Chrome 
- Mozilla Firefox 


## Deployment

This project was developed using Gitpod as the chosen IDE and Github as a remote repository.

The deployed project can be viewed on the following link: [The Cook Book: Live Website](https://cook-book-ruben.herokuapp.com/)

The project's GitHub repository can be viewed with the following link: [The Cook Book: Github Repository](https://github.com/rlopezba1/cook_book)


## Credits

### Images

The Images are referenced below

#### Pexels

- [2 women](https://github.com/rlopezba1/cook_book/blob/master/static/img/pexels-katerina-holmes-5908216.jpg)

- [man and woman](https://github.com/rlopezba1/cook_book/blob/master/static/img/pexels-elle-hughes-2696064.jpg)



## Acknowledgements

- My mentor Seun Owonikoko for her support
- Code Institute tutors for the advices, guidance and support, and Student Nicola to some ideas