# Django project (Project Portfolio 4) for Code Institute.

## General information
Starhögs Equestrian is a website where you can improve your dressage riding skills. The website provides you with the ability to create your own account and add in your personal details, should you wish. After a user has created their account they can now book riding lessons with an instructor. 

The website has full CRUD functionality, which means that a user can:
- Create a booking.
- Read/View their booking.
- Update their booking.
- Delete their booking.

The idea for this website was to create something that could help my wife with her real life dressage lesson business and make it easier for her to maintain and have control over her schedule. Although there is more that I want to add to the project, this will be future implementations, which you can read more about further down in this documentation.

Link to the application: [Click Here!](https://star-pro4-3dc81848625c.herokuapp.com/)

![Fullscreen image of the application:](/documentation/images/index_fullsize.png)
---
![Phonescreen image of the application:](/documentation/images/index_phonesize.png)

---
## Table of Contents

 - ## [General Information](#general-information)

 - ## [Table of Contents](#table-of-contents-1)

 - ## [UX](#UX-1)

 - ## [Project Goals](#project-goals-1)

 - ## [User Stories](#user-stories-1)

 - ## [Flowchart](#Flowchart-1)

 - ## [General features](#general-features-1)
    
- ## [Testing](#testing-1)
    - ## [Code Validation](#code-validation-1)
    - ## [Testing User Stories](#testing-user-stories-1)
    - ## [Future improvements](#Future-improvements-1)
- ## [Bugs](#Bugs-1)

- ## [Libraries and Software](#Libraries-and-Software-1)

- ## [Final Result](#final-result-1)

- ## [Deployment](#deployment-1)

- ## [Github Pages](#github-pages-1)

- ## [Credits](#credits-1)
---
## UX
The purpose of the site is to provide an easy understandable website with a simple and easy way for the user to create a booking. The site should be pleasing to the eye and to make a booking should be very simple.
No flashy colors were used, but the colors were calm and pleasing to interact with.
A favicon were used to make the website look better in the tab-bar.

### Colors used:


## Project Goals
The project goals was to create a website using the Django Framework in Python along with HTML CSS and Javascript. A user should be able to create a booking for their dressage lesson at available times and should be able to be up to 3 participants per lesson. 

A Database was set up to handle all data and to ensure correct booking and tracking was applied. 

A user should not be able to create or edit any booking without being authorized on the site. Contacting the admin does not require a login status.

---
# User Stories

| **EPIC** | **ID #** | **User Story** | **Github project** |
|-------------|------------|---------------------|---------------------|
| **User Authorization** |
|  | 1 | As a Site User I can register for an account so that I can book, update and delete my bookings | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22User+Authorization%22&pane=issue&itemId=33280441) |
|  | 2 | As a Site User I can easily see my login status so that I know if I'm logged in or not to the site. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22User+Authorization%22&pane=issue&itemId=33281113) |
|  | 14 | As a User I can see my account information so that I can add first name, lastname, adress, update email adress. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22User+Authorization%22&pane=issue&itemId=34983028) |
| **Lesson Booking** |
|  | 3 | As a logged in user I can see all my bookings so that I know when I my bookings will take place. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Lesson+Booking%22&pane=issue&itemId=33281896) |
|  | 4 | As a Logged In Site User I can update and delete my bookings so that I can change or cancel my bookings. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Lesson+Booking%22&pane=issue&itemId=33282761) |
|  | 5 | As a logged in user I can create a booking so that it appears under "My Bookings". | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Lesson+Booking%22&pane=issue&itemId=33283329) |
|  | 6 | As a Logged in User I can add information to my booking so that the teacher can be prepared for the lesson. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Lesson+Booking%22&pane=issue&itemId=33283779) |
|  | 13 | As a User I can filter my bookings so that I easily can see which has passed and which are upcoming. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Lesson+Booking%22&pane=issue&itemId=34977495) |
| **Home/ About pages** |
|  | 8 | As a user I can immediately understand the purpose of the site so that I can easily decide if it meets my needs. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Home%2FAbout+pages%22&pane=issue&itemId=33286328) |
|  | 9 | As a User I can read about the company so that I know who is running it and who the teacher is. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22Home%2FAbout+pages%22&pane=issue&itemId=33286672) |
| **User Contact Abilities** |
|  | 10 | As a user I can contact the teacher so that I can get answers to my questions. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?filterQuery=label%3A%22User+Contact+Abilities%22&pane=issue&itemId=33286913) |
| **Admin** |
|  | 15 | As a Admin I can approve lessons so that the user can see that it has been approved. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?pane=issue&itemId=36399686) |
| **NOT IMPLEMENTED!** |
|  | 11 | As a Logger in User I can book a place for the summer pasture so that I have a place for my horse next summer. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?pane=issue&itemId=33312687) |
|  | 7 | As a Logged in User I will get an email confirmation so that I know that my lesson has been confirmed. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?pane=issue&itemId=33284416) |
|  | 12 | As a Logged in User I can book a box for my horse so that my box can stay long term at the farm. | [Link](https://github.com/users/gStarhigh/projects/4/views/1?pane=issue&itemId=33312758) |
---
## Flowchart

### Structure
The structure of the website is divided between authenticated user and not authenticated.
- Register page gives the user the possibility to create an account.
- Login page gives the user the possibility to login to an existing account.
- The Home page is visible for all users and displays images and information about the site.
- The Contact page is visibile for all users and displays a contact form. If the user is authenticated, the Username and Email will be pre-populated. If the user is NOT authenticated, the user will have to provide that information before submitting.
When the form is valid and sent, an email is sent to both the admin and the user.
- The About page displays images and information of the business. There is also an embedded video and an Google Maps API that displays the location.
- My Bookings page is only accessible if the user is logged in and displays all bookings made by the user. If there is no bookings made, an message will be displayed: "You have no bookings yet". The bookings are sorted by date. As a User you can filter your bookings by three variables: 
    
    All: Displays all bookings, regardless of date or status.

    Upcoming: Only displays "Approved" lessons that has not passed.

    Completed: Only displayes "Approved" lessons that has passed.
- The Book a lessons page is only accessible if the user is logged in. It displays the form neccessary to complete a booking. Here the user will be asked to enter the following information:
    
    Focus for the lesson
    
    Date: You are only able to book Monday to Friday.

    Time: You are only able to book the following times:
    18:00,19:00,20:00,21:00.

    Number of participants: Up to 3 people can share a lesson time.

    Level of the ekipage: Your level of dressage skills, chosen from a dropdown list.

    Terms of booking: A checkbox that must be checked. Terms can be read by pressing the link "Read terms here", that will open a modal.

- My account page is only accessible if the user is logged in and lets the user update the firstname, Lastname and email adress. There is also a readonly field containing the date and time the user created the account. 

#### Here is an image of the structure I used for this project.
The flowchart was made using [Lucidchart](https://lucid.co/).
![Image of the structure:](/documentation/images/structure.PNG)


#### Wireframes


#### Database

The project uses the PostgreSQL relational database for storing the data. It was setup using [ElephantSQL](https://www.elephantsql.com/). Read more about Elephant SQL in the [Deployment](#deployment-1) section.

The schema was made using [Lucidchart](https://lucid.co/).
![Schema:](/documentation/images/pro4_db_schema.PNG)

---
## General features

--- 
## Testing

#### Lighthouse result
A good result was presented on the desktop test.
    <details>
    <summary>Desktop</summary>
    <img src="documentation/lighthouse/desktop.PNG">
    </details>


On Mobile the result was not as good as on desktop. It seems that the boostrap cdn along with the emailjs cdn causes the page to render slower on mobile.
    <details>
    <summary>Mobile</summary>
    <img src="documentation/lighthouse/mobile.PNG">
    </details>
    <details>
    <summary>Mobile Issues</summary>
    <img src="documentation/lighthouse/issues_mobile.PNG">
    </details>


---
### Code Validation

#### HTML
All HTML files has passed through validation and shows no errors:
<details>
<summary>index.html</summary>
<img src="documentation/validations/html/index_html_validation.PNG">
</details>

<details>
<summary>create_booking.html</summary>
<img src="documentation/validations/html/create_booking_html_validation.PNG">
</details>

<details>
<summary>404.html</summary>
<img src="documentation/validations/html/404_validation.PNG">
</details>

<details>
<summary>about.html</summary>
<img src="documentation/validations/html/about_validation.PNG">
</details>

<details>
<summary>delete_booking.html</summary>
<img src="documentation/validations/html/delete_booking_html_validation.PNG">
</details>

<details>
<summary>details.html</summary>
<img src="documentation/validations/html/my_account_html_validation.PNG">
</details>

<details>
<summary>my_bookings.html</summary>
<img src="documentation/validations/html/my_bookings_html_validation.PNG">
</details>

<details>
<summary>update_booking.html</summary>
<img src="documentation/validations/html/update_booking_html_validation.PNG">
</details>

<details>
<summary>logout.html</summary>
<img src="documentation/validations/html/logout_html_validation.PNG">
</details>

<details>
<summary>login.html</summary>
<img src="documentation/validations/html/signin_html_validation.PNG">
</details>

<details>
<summary>signup.html</summary>
<img src="documentation/validations/html/register_html_validation.PNG">
</details>

#### CSS
All CSS files has passed through validation and shows no errors:
<details>
<summary>CSS Validation</summary>
<img src="documentation/validations/css/style_css_validation.PNG">
</details>

#### JavaScript
All Javascript files has passed through validation and shows no errors:
<details>
<summary>googleMaps.js</summary>
<img src="documentation/validations/js/google_maps_js_validation.PNG">
</details>

<details>
<summary>index.js</summary>
<img src="documentation/validations/js/index_js_validation.PNG">
</details>

<details>
<summary>sendEmail.js</summary>
<img src="documentation/validations/js/send_email_validation.PNG">
</details>

#### Python
All Python files has passed through validation and shows no errors:
<details>
<summary>admin.py</summary>
<img src="documentation/validations/python/admin_validation.PNG">
</details>

<details>
<summary>apps.py</summary>
<img src="documentation/validations/python/apps_validation.PNG">
</details>

<details>
<summary>asgi.py</summary>
<img src="documentation/validations/python/asgi_validation.PNG">
</details>

<details>
<summary>env.py</summary>
<img src="documentation/validations/python/env_validation.PNG">
</details>

<details>
<summary>forms.py</summary>
<img src="documentation/validations/python/forms_validation.PNG">
</details>

<details>
<summary>manage.py</summary>
<img src="documentation/validations/python/manage_validation.PNG">
</details>

<details>
<summary>models.py</summary>
<img src="documentation/validations/python/models_validation.PNG">
</details>

<details>
<summary>settings.py</summary>
<img src="documentation/validations/python/settings_validation.PNG">
</details>

<details>
<summary>urls.py</summary>
<img src="documentation/validations/python/urls_validation.PNG">
</details>

<details>
<summary>validation.py</summary>
<img src="documentation/validations/python/validation_validation.PNG">
</details>

<details>
<summary>views.py</summary>
<img src="documentation/validations/python/views_validation.PNG">
</details>

<details>
<summary>wsgi.py</summary>
<img src="documentation/validations/python/wsgi_validation.PNG">
</details>
---

## Testing User Stories
Placeholder

1. Placeholder

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |

2. Placeholder #2

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |
| Placeholder | Placeholder | Placeholder | Placeholder | Placeholder |

---
## Future improvements

1. Having 2 databases, one for local testing and one for the deployed version. This would not flood the deployed versions database with test data.

2. 


---
## Bugs
Known Bugs:

Issue: If you book a lesson where the lesson is full, emailJS will still send out an email.

Solution: I believe an AJAX request to the server would solve this - Future implementation.

---
About page:

Issue:
Error in console:
"Error with Permissions-Policy header: Unrecognized feature: 'ch-ua-form-factor'."

Solution: 
What I've understood this has something to do with Google's end. It has no affect on my site and everything works as it should. If i delete my iframe, the error disappears. I have found no solution to this, and as it does not affect the functionality, the iframe is left in the project.

---
Login page:
Issue: To the right of "remember me" and to the left of the checkbox, there is a symbol which I cannot seem to remove. 

Solution: Unknown

---
## Languages, Libraries and Software
### Main Languages:
- HTML5
- CSS3
- Python
- Javascript
- Django

### Libraries used:


### Software used:
- Gitpod - Used for version control and to commit and push code to github.
- Github - Github is used to store the projects code after being pushed from gitpod. 
- Heroku - Used to deploy the project online.
- PostgreSQL(ElephantSQL)
---
## Final Result
- The final deployed project can be found [here.](https://star-pro4-3dc81848625c.herokuapp.com/)

### Sample printscreens of the finished project below:

(All images can be found [Here](https://github.com/gStarhigh/pro4/tree/main/documentation))

<details>
<summary>Printscreen 1</summary>
<img src="">
</details>


---
## Deployment
Creating the Heroku app


---
## Github Pages
- This project was developed using Gitpod which I used to commit and push to GitHub using the terminal in GitPod.(Note that this project was deployed to Heroku and that those steps also must be followed.)
### Here are the steps to deploy a website to GitHub Pages from its GitHub repository:

- Log in to GitHub and locate the GitHub Repository.
- At the top of the Repository, locate the Settings button on the menu.
- Under Source, click the dropdown called None and select Main Branch.
- The page will refresh automatically and generate a link to your website.
### Forking the GitHub Repository
- By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

- Log in to GitHub and locate the GitHub Repository.
- At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
- You should now have a copy of the original repository in your GitHub account.
### Making a Local Clone
- Log in to GitHub and locate the GitHub Repository
- Under the repository name, click "Clone or download".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 3. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
- Press Enter. Your local clone will be created.
---
## Credits

- I want to thank my mentor Jack at Code Institute for continuing to push me in my projects and for his continued support. 

- I want to thank my wife Maria whom supplied all necessary information about riding, the images and support during this project.
All images belong to us except the favicon.

- Code institute for the walkthrough projects that taught me django to be able to complete this project.

- Django Allauth docs: https://django-allauth.readthedocs.io/en/latest/configuration.html

- EmailJS docs: https://www.emailjs.com/docs/sdk/send-form/

- Class based view docs: https://ccbv.co.uk/

- Favicon Credit: https://favicon.io/emoji-favicons/horse

---