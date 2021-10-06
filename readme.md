# Computer Pc

## Code Institute: Milestone Project 4

![Computer PC Responsive Design](https://github.com/rlopezba1/computer_pc/blob/main/media/AmI_responsive.png)

*Computer PC* is a website that sells laptops, desktops, tablets, and monitors. My goal with this project was to create an intuitive website, useful for people looking for good deals and good products. There is also a current blog where you can leave your comments.

In our contemporary age, everyone needs computers and I believe that having a store with all these options always has a future.

[Here the full project live.](https://ruben-computer-pc.herokuapp.com/)

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

- To create a website for people looking for laptops and for people who want know the lastest blogs

- Users can search, buy products, pay for them, create a profile, edit or delete products from shopping bag, create their own account

- Navigation must be intuitive and simple, so that the user finds the recipes easily and can act simply.

### User Stories

- I would like people to contribute with comments in the blog area so that people can participate, with quick and easy access.
- I want the main purpose of the site to be clear so that I immediately know what the site is intended for upon entering.

#### New Users

- I am a user who loves technology and I would like to find an online shop where I can buy and find new products.
- I am a user who loves technology and I would like to find an online shop where I can get new ideas.
- I want to be able to find the products I want quickly and easily so I can complete my purchases.

#### Returning Users

- I am a user who frequently look for new products and I want to see what is new.
- I am a user who wants shopping, on an easy way, and keep a record of my shopping.
- I want to easily view the total of my purchases at any time and have the option to update or delete.
- I want to search for individual products to save time a list of products or look for an individual item by its category.


#### Frequent User

- As a frequent user, I want to go back to the website and see the new products and comments from a blog.
- I want be able to see products ratings to I can make informed purchase decisions.
- I want to successfully register for an account and proceed to log in.
- I want to easily access my previous orders.
-I want to be able to store my shipping details so that it’s easier for me to check out.



### Design Process

#### Design Process: UX Research

- The design had to be simple so that users were direct to find what they were looking for, without too many detours

#### Design process: UX Design

1. Strategic plan: There are a lot of websites that you can buy technology products. This web will be easy to navigate with not much options.

2. Scope map: The user must easily find the product, and those who collaborate by adding more comments, must be able to create, edit or delete them quickly and easily.

3. Structure plan: The navigation bar will be the one that directs the user depending on what he wants to do. Search products, go to your profile, go to the product list, or log out. If you are not registered you can register and log in

4. Skeleton plan: For the average user, the important thing is to find the product that he needs. Therefore, the search is essential and that is why it occupies a prominent position on the page. Then the products appear so that he can find the one he is looking for.

5. Surface plan: The colors used are elegant and bright, which are combined throughout the web. The font used is Lato, very familiar to all technological users.



## Features

### Existing Features

- Separate navigation bars for desktop and mobile devices.
- Responsive Design - Site should be responsive on all devices.
- On entering the homepage it will immediately clear what the purpose of the site is.
- Standard e-commerce feed of products with the option to sort products and filter them by category name.
- Clear and obvious call to action buttons with a shop now button on the home page along with links to purchase the bestselling products.
- Blog page – useful and technology advice which will be added to on a regular basis.

#### Wireframes

[wireframes](https://github.com/rlopezba1/cook_book/blob/master/static/documentation/cook_book.pdf)
- Balsamiq was used to create wireframes for the site

#### Database structure

- As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment

#### Consistent features across all pages

- The navbar is visible and responsive in every page, and when the user scrolls down it turns into white and follows the navigation.
- All the 'Add Recipe' and 'Go Back' / 'Cancel' buttons areof the same color throughout the design, the only exception is the one in the user profile, but it gets the typical green color when hovered.
- All the flash messages appear with the same color and font throughout the app.

#### The Structure Plan

- When the user arrives on site, they will see the home page and text which On entering the site. To the left of the image is a shop now button allowing customers to start shopping immediately if they wish. Search and filter features on the top of every page allow customers to quickly and easily find the products they are looking for.

- The products in the shop are divided into relevant categories, which makes it easier to find products. Customers are view the full details of any product by clicking on the product in the shop. Details include the name, description, image, price and rating.

- Once customers add products to their cart, this cart will be visible at all times in the top right hand corner of the site. It will also display the current cart total in Euro.

- Handy message notifications will also appear in the top right hand corner when a customer performs an action such as adding something to their cart, removing it etc.

- Secure checkout has been implemented using Stripe and customers are redirected to a checkout form page when they are ready to pay.

- The about page explains a little about the owners of the website with a paragraph to left of the image of the owners. The blog page contains a list of blogs with links on each to read more. The contact form contains a simple form allowing customers to email the site owners with any questions.

#### Products

- On this page you can find all the products. There is the search option to find the product by name or by parts of the definition.

#### Single product

- This page shows the user the image of the product and caracteristics on a card.


#### Login

- If any of the username / password combinations are incorrect, the user receives a message suggesting that one or both of the entries are incorrect.

- If the user does not have an account, he can register a button through

#### Register

- New users can create an account by providing username and password. If you are already registered you will be notified.


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

- [Django](https://https://www.djangoproject.com/)

- [Gitpod](https://www.gitpod.io/)

- [Git Version Control](https://git-scm.com/)

- [GitHub](https://github.com/)

- [Heroku](https://www.heroku.com/)

- [Django Central](https://djangocentral.com/)

- [Boostrap](https://getbootstrap.com/)

- [Heroku](https://heroku.com)

- [AWS-S3](https://aws.amazon.com/)

- [Stripe](https://stripe.com/)

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


I manually tested the project on the following web browsers, checking that all aspects worked :
- Google Chrome 
- Mozilla Firefox 


## Deployment

This project was developed using Gitpod as the chosen IDE and Github as a remote repository.

The deployed project can be viewed on the following link: [Computer PC: Live Website](https://ruben-computer-pc.herokuapp.com/)

The project's GitHub repository can be viewed with the following link: [Computer PC: Github Repository](https://github.com/rlopezba1/computer_pc)




## Acknowledgements

- My mentor Seun Owonikoko for her support
- Code Institute tutors for the advices, guidance and support.