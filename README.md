The King Of Chores is a todo list app built with Django. It allows users to create, manage, and complete tasks. 
The target audience for this webapp is families or other groups of people who need a to-do list where they can create a to do list together. And so they can see who did what.

The live link can be found here - [The King Of Chores](https://the-king-of-chores.herokuapp.com/)

![responsive](assets/readme/images/responsive.png)







<!-- <small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small> -->
## User Experience (UX)

A visitor to The King Of Chores. Is most likely a small group of people such as a family. 
And with a need to create a common to-do list where they can see what needs to be done and who has done what.

### User Stories

#### EPIC | User Profile
- As a user, I want to be able to log in to my account using my credentials. This allows me to access personalized features and view my own 
  data.
- As a user, I want to be able to create a new account by registering with a username.
  This allows me to have a unique identity within the system and access its functionalities.
- As a user, I want to be able to view my login status. This provides me with information about my authentication status.
- As a user, I want the ability to log out of my account to ensure the security of my personal information and prevent unauthorized access.


#### EPIC | List of chores
- As a user, I want the ability to check off completed chores and mark them with my name. This allows me to take ownership of the tasks I have completed and keep a record of my contributions.
- As a user, I want to be able to view a list of completed chores that are marked with the name of the person who completed them. This helps me track the progress and accountability of each individual.
- As a user, I want to be able to delete unwanted or completed chores from the list. This helps me keep the chore list organized and remove any unnecessary tasks.
- As a user, I want the ability to edit the details of a chore, such as its title, description or how completed task. This allows me to make necessary changes or updates to the tasks as needed.
- As a user, I want to see a comprehensive list of all the chores. This helps me have an overview of the tasks that need to be done.
- As a user, I want the ability to add new chores to the list. This allows me to include new tasks that need to be completed.

The following user stories where labelled as "could have" and "Won't Have" on my project board on Github.

#### EPIC | List of chores
- As a user, I would like the option to select multiple tasks and delete them simultaneously. This provides a more efficient way of managing and removing multiple tasks from the list.

#### EPIC | Game Functionality
- As a user, I want the system to track and display the number of completed tasks for each invited user. This allows me to compare my progress with other users and see how I rank.
- As a user, I would like to see a leaderboard that showcases the top performers based on completed tasks. This adds a competitive element and encourages users to complete more tasks.
- As a user, I want to be able to compete with invited users to see who can complete the highest number of tasks. This creates a sense of competition and motivation among users.
- As a user, I want the system to track and display the number of completed tasks for each invited user. This allows me to compare my progress with other users and see how I rank.

### User Stories

![User story diagram](assets/readme/images/user_story_diagram.png)

#### Colour Scheme
<small><i><a href='https://coolors.co/ffffff-343a40-5aa29a-40b997-47cd82-70de5d-a8eb12'>Colour palette from Coolors</a></i></small>

![Colour Palette](assets/readme/images/colour_palete.png)

The colour scheme of the site is mainly linear-gradient. The rest is bg-dark and text-light boostrap.

The colors are designed with ease of use in mind. 


<details>

 <summary>Login Page</summary>

![Login page](assets/readme/wireframes/login_page.png)
</details>

<details>

<summary>Register Page</summary>

![Register page](assets/readme/wireframes/register_page.png)
</details>

<details>

<summary>Home Page</summary>

![Home page](assets/readme/wireframes/home_page.png)
</details>

<details>

<summary>Todo List Page</summary>

![Todo list page](assets/readme/wireframes/todolist_page.png)
</details>

<details>

<summary>View Page</summary>

![View page](assets/readme/wireframes/view_page.png)
</details>

<details>

<summary>Update Page</summary>

![View page](assets/readme/wireframes/update_page.png)
</details>

<details>

<summary>Delete Page</summary>

![Delete page](assets/readme/wireframes/delete_page.png)
</details>

## Agile Methodology

Github projects was used to manage the development process using an agile approach. The link to my project board is [here.](https://github.com/users/assofiejakobsson/projects/23)

## Data Model

The diagram below details the database schema.

![Database Schema](assets/readme/images/database_schema.png)

## Testing

Testing and results can be found [here](/TESTING.md)

## Security Features and Defensive Design

### User Authentication

 - The UserCreationForm form to create a new user based on the submitted data. If the form is valid, a new user is created, and they are logged in using the login function. This I use in the register view.

  - The AuthenticationForm form to authenticate the user based on their submitted credentials. If the form is valid, the user is logged in using the login function. This I use in the user_login view.

 - The @login_required decorator is used to restrict access to certain views. It ensures that only authenticated users can access those views. If an unauthenticated user tries to access a view decorated with @login_required, they will be redirected to the login page.

  - The CSRF tokens and middleware are built in django mechanisms. This are to handle CSRF protection and mitigate the risks associated with CSRF attacks.

  - The form classes (UserCreationForm, AuthenticationForm, and TodoForm) are for form validation. Django's form validation ensures that user input is validated and secure.

  - The 'get_object_or_404' function are for handle object retrieval from the database. This function retrieves an object but raises a 404 HTTP response if the object is not found. This helps avoid exposing sensitive information or potential security vulnerabilities.

### Database Security

 - The database url and secret key are stored in the env.py file to prevent unwanted connections to the database.

## Features

### Header

![header](assets/readme/features/header_loggedin.png)


 - The name on the project is the logo. And it is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user and it has a hover efect.
 - The register and login links are to the right whene the user not are loggedin.
 - The register and login links are hidden in a burger navbar in mobile view. And whene the user click on the burger navbar
 the register and login links are displayde under the loggo to the left.

![header](assets/readme/features/header_loggedout.png)
![header](assets/readme/features/header_loggedout_mobile.png)

 - The username whit a welcome is displayd on the right side whene someone i logde in. And a logout link are displayd next to the usernam.
 - The logout link and the username are hidden in a burger navbar in mobile view. And whene the user click on the burger navbar
 the logout link and the username are displayde under the loggo to the left.

![header](assets/readme/features/header_loggedin.png)
![header](assets/readme/features/header_loggedin_mobile.png)

### Footer 

![fotter](assets/readme/features/footer.png)

 - The logo is placed in the middle of the footer and next to the loggo is the contact information.The loggo has a hover function and whene the user click it they ar redirect to the home page.
 Below this in the middle there is an upward arrow with the blue link color and it fits because the main buttons in the app have that color.
 And whene you hover over the arrow a text go to top shown. Whene the user click the arrow the page gos up to the top. The fotter are fixed. This simplifies navigation for the user.

### Home Page

![header](assets/readme/features/home_page.png)

 - The home page is simply designed with a brief description of the app. 
 And it also appears that you need an account to be able to use the app.
  - Below the text there is a button "Go To The Todo List. If you not are logged in it will take you to the login page. if the user is logged in, the user goes directly to the todo list page.
  - The simple design with little content facilitates the user's understanding of what and how the app can be used.


### Todo List page

![header](assets/readme/features/todolist_page.png)
![header](assets/readme/features/modal.png)


  - The Todo List page has a simple and user-friendly design.
  - First on the page comes a title "Todo List" First on the page comes a title "Todo List" to clarify what it is.
  - After the title, there are two input fields, one for task title, which is mandatory in order to add tasks. The second input field is optional and it is for description, the reason 
  I have chosen an input field and not a text area is because it both looks nicer and gives a less cluttered impression. And since description is not something that is needed but only a small plus and if you want to edit the task there is a text area. right after both input fields comes an Add Task button.
  - After the add task section there will be two titles the first "Uncompleted Chores" and below this will be "Completed Chores".
  Under "Uncompleted Chores" All tasks that are added and not marked as completed are visible in this section. 
  - Each uncompleted task has four buttons, the first button is "View" and it takes the user to the View page. The second button is "Edit" and it takes the user to the uncompleted update page. The third button is "Delete" and it takes the user to the uncompleted delete page.
   The fourth button is "Complete" And this button brings up a modal where the user can enter who completed the task.
  - The modal has a title "Complete Task" and a cross button that closes the modal. And this comes an input field with lable "Your Name:" And immediately after a button "Submit".
   When the user presses the "Submit" button, the modal disappears and the task appears as completed by: Name under the title "Completed Task"
  - Under "Completed Task" all tasks that have been marked as completed are visible and they also have an overtitle "completed by: name" And all tasks that a name has completed are gathered together under "completed by: name". Each completed task has three buttons, the first is "View" and it takes the user to the View page.
   The second button is "Edit" and it takes the user to the updater completed page. The third is "Delete" and it takes the user to the delete page.


### View page

![header](assets/readme/features/view_page.png)

- First comes a title "Task Title". Which makes it easier for the user to understand where and what it is about.
- After the title. Will the title of the task the user chose to look more closely at and a possible description,
 completed status and who completed the task.
 - After the task details there are two buttons. The first button is "Delete" and it takes the user to the delete page.
  And the second button is "Back" and it takes the user to the todo list page.

### Edit page

![header](assets/readme/features/edit_page.png)

- There are two pages for editing, one is for uncompleted tasks. And the other is for the completed tasks but they work and look the same. I never managed to fix the code so I only need one of them, but I will fix that later.
- First comes a title "Update Task". Which makes it easier for the user to understand where and what it is about. 
- After that comes a form with input field for task title, check box for completed, input field, input field for completed by and a text area for description.
- After that there are two buttons, the first one is "Update" and when the user clicks on it, an alert message appears asking if the user is sure it wants to update the task. And there are two buttons on the alert message and one is "Yes" and the other is "Cancel". If the user selects yes, the task is updated and the alert message disappears. If the user selects cancel, the alert message disappears without updating the task.
- The second button next to the "update" button is a "Back" button that takes the user back to the todolist page.

### Delete page

![header](assets/readme/features/delete_page.png)

- There are two pages for delete, one is for uncompleted tasks. And the other is for the completed tasks but they work and look the same. I never managed to fix the code so I only need one of them, but I will fix that later.
- First comes a title "Delete Task". Which makes it easier for the user to understand where and what it is about. 
- After that comes a text asking the user if they are sure they want to delete the task. The task's title is below the text, so the user must be sure which task he is talking about.
- After that there are two buttons, the first one is "Delete" and when the user clicks on it the task disappears and the user returns to the todolist page.
- The second button next to the "Delete" button is a "Cancel" button that takes the user back to the todolist page.

### Register page

![header](assets/readme/features/register_page.png)

- First comes a title "Register". Which makes it easier for the user to understand where and what it is about. 
- After that comes a form with input field for username, password, input field and cofirm password.
- After that comes a "Register" button. And if the user has filled in everything correctly, and clicks on it, the user will be taken to the website as a logged in user.
- At the bottom it says "Already have an account?" and a link "Login" that takes the user to the login page.

### Login page

![header](assets/readme/features/login_page.png)

- First comes a title "Login". Which makes it easier for the user to understand where and what it is about. 
- After that comes a form with input field for username and password.
- After that comes a "Login" button. And if the user has filled in everything correctly, and clicks on it, the user will be taken to the website as a logged in user.
- At the bottom it says "Don't have an account?" and a link "Register" that takes the user to the Register page.







.wrapper. https://css-tricks.com/best-way-implement-wrapper-css/

https://mycolor.space/gradient?ori=to+bottom&hex=%23053337&hex2=%23A8EB12&sub=1

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
