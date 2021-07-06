# Bookler

[Click To See Live Site](http://tailwind-ms3-new.herokuapp.com/)

Bookler is a website and app designed for restaurants that deal with reservations and require a CRM to manage manual bookings as they move away from pen and paper diary management (which is still prevalent across the industry). 
A key feature of the app is it's guest profiles which enable the restaurant to keep information in one place to deliver the best guest experience possible.

[![Bookler](static/img/team.jpg)](https://sreninc.github.io/tailwind-ms3/)

## CONTENTS
1. User Stories
    - Website Visitor
    - App User
    - Website & App Owner
1. Design & UX
    - TailwindCSS
    - Color Scheme
    - Mockups & Wireframes
    - Custom CSS
1. Website Pages & Features
    - Common Features
    - Hompage
    - Features
    - Contact
    - Signup
1. App Pages & Features
    - Common Features
    - Dashboard
    - Team
        - Add User
        - Edit User
        - Delete User
    - Guests
        - Add Guest
        - Edit Guest
        - Delete Guest
    - Bookings
        - Add Bookings
        - Edit Booking
        - Delete Booking
1. Database Schema
1. Testing
1. Bug Log
1. Deployment
1. Credits & Attribution


***

## Project Stories

### User Stories
As a user I want to...
- Sign up to the service to access software for my restaurant.
- Manage my team and their access levels within the software.
- Created, Update, Read and Delete Guests.
- Create, Update, Read and Delete bookings.
- Be able to add information for guests to improve their service.

### Business Stories
As the website owner I want to...
- Get website visitors in the target market to sign up to the paid service.
- Get website visitors in the target market who are unsure of the service or who have questions to contact the website owner.

***

## Design and UX

### Design and UX Research
There is a wide range of financial freedom and financial wellness orientated websites across various markets. Before starting the projects wireframes and mockups I looked through the top ranking website results from Google, some of which I have detailed below.
- [daveramsey.com](https://www.daveramsey.com)

The top result on Google. The website uses blue as the primary color and gold/dark yellow as a minor secondary color throughout the site. It's imagery is predominantely smiling and exhuberant people displaying overwhelmingly positive messages. It's primary focus is to get people to start with one of thier free tools today and/or purchase one of their paid items. They have a paid budgeting app. The UI is easy to use with blocks of text kept small and to the point. Images and iconography are used in every section.

- [investopedia.com](https://www.investopedia.com)

The second result on Google. The website is heavily text based with no imagery until the bottom of the page. This is to be expected from a website styled as an encyclopedia however it would be unsuitable for my project. The lack of design on this site would not make it enticing for vistors of the site in this project. 

- [mabs.ie](https://www.mabs.com)

The Irish Money Advice & Budgeting Service. Similar to daveramsey.com the primary and secondary colors are blue and gold. They have an income and expenses tool for visitors to use. It is a 4 step form where the user inputs amounts for pre-defined categories in income and expenses. At the end of the process it shows a recap coupled with displaying the surplus/deficit. The calculator works well and gives the information required and offers some set links to help the visitor increase income or decrease expenditure. What it misses is some imagery / graphical representations of the users data to help them visualize their data. 

- [financialplanner.ie](https://www.financialplanner.ie)

First irish website in Google results. Blue is the primary color on this website. The website is quite text heavy and as an in-person services company aims to get the visitor to fill in a contact form. They do have some calculators on the website however they have code errors stopping the calculator from working during research. 

From the design and UX research it is clear that blue/gold are standard industry colors that should be used for Financial Freedom. This will help the visitor trust the website from the begining by using expected colors. It is also clear that positive imagery and explanatory iconography should be used to convey the sites purpose as much as possible so as to limit the amount of text on the website. None of the websites visited had a modern, easy to use and flexible feature for gauging your income and expenses. This will be the USP of financial freedom compared to the top Google results on google search. 
### Website Wireframes

### Website Mockups

***

## Website Pages and Features
1. All pages on the website have access to a login form in the header and footer navigation. When clicked it opens a modal centered on the screen. It has a number of responses based on the users input:
    - Correct email and password - Logs user in and loads Dashboard
    - Incorrect email or password - Loads the homepage with log in modal open containing an error message.
    - Email doesn't exist - Loads the homepage with login modal open containing an error message directing user to signup.

### HOMEPAGE
The purpose of this page is to get the user to signup or failing that to look at the software in more detail on the features page.

### FEATURES
The purpose of this page is to get the user to signup. It contains two hero sections for primary software use cases which are followed by 6 tiles detailing additional important features.

### CONTACT
The website visitor can send a message to the website owner if they want further details on the software or support if an existing user.

N.B. As a demo the number and email are fake. The send message also only sends to the website creators personal address.

### SIGNUP
The purpose of this page is to get the user to signup. If the email doesn't exist in the users db a new business will be created and a new user based on the signup details. If the email already exists the user will be redirected back to the signup page with a message informing them to login rather than signup.

## App Pages and Features

### DASHBOARD
This page shows the restaurant (user) key statistics about their performance based on bookings and guests within Bookler. 
- Total Guests: The count of total guests created by the restaurant
- Total Bookings: The count of total bookings created by the restaurant
- Total Sales: The sum of the value of bookings that are marked as "Completed"
- % No-Shows: The count of bookings marked "No-Show" divided by the count of all other bookings.
- % Completed: The count of booking marked "Completed" divided by the count of all other bookings.
- Avg. Booking Value: Total Sales / Count of bookings marked "Completed"

### TEAM
This is the page where the account managers it's authorized users, their details and access level. If the user is an admin they will see delete and edit options across all pages. If not an admin the user won't see delete options on any pages and they won't be able to edit team members.

N.B. The original account creator is not able to be deleted from the team section. In addition the logged in user cannot delete themselves.

There are 3 functions available from the team page:
1. Add Team Member
1. Edit Team Member
1. Edit Team Member > Delete Team Member

### GUESTS
This is the page where the account manages their guests. This is a primary page for the user and should be considered mission critical. On this page the user can see their guests listed alphabetically, paginated across pages as required with key information on each guest listed. 

There are 2 functions available from the team page:
1. Add Guest
1. Edit Guest

### GUEST DETAIL AKA Edit Guest
This page is the full guest profile. It contains 4 sections covering important information any restaurant would need on it's guests.
1. Personal information: THis section contains contact information for the guest as well as some useful marketing information.
1. Notes: This section contains 3 textareas for notes that ensure an excellent guest experience is possible. 
1. Stats: This section contains stats that are exactly the same as the dashboard statistics with the exception of total guests being replaced with Guest Age. A useful metric when evaluating top guests for a restaurant.
1. Bookings: This section mirrors the main bookings page but is filtered to just the guests bookings ordered by date.

### BOOKINGS


### BOOKING DETAIL


***

## Database Schema

The MongoDB database is structured as follows:
- restaurant_bookings
    - bookings
        - _id
        - client_id [links booking to client]
        - date
        - time
        - people
        - status
        - value
        - rating
        - account_id [links booking to account]
        - created_by
        - created_date
        - updated_by
        - updated_date
    - business
        - _id
        - email
        - name
    - clients
        - _id
        - first_name
        - last_name
        - email
        - mobile
        - marketing_consent
        - rating
        - dob
        - bookings
        - bookings_completed
        - value
        - notes_service
        - notes_kitchen
        - notes_allergies
        - account_id [links client to account]
        - created_by
        - created_date
        - updated_by
        - updated_date
    - users
        - _id
        - email
        - password
        - name
        - access
        - account_holder
        - account_id [links user to account]
        - created_by
        - created_date
        - updated_by
        - updated_date

***

## Testing
The same testing checklist was used to check each page throughout the website. A checklist unique to each feature was used to 

- [ ] All page content loads correctly
- [ ] Passes lighthouse tests
- [ ] No lorem ipsum or spelling errors
- [ ] Page renders correctly on all inspector screen sizes
- [ ] Hover states and CTA clicks present and correct
- [ ] Page passes HTML, CSS and JS linters
- [ ] Links operate as expected
- [ ] No console errors

### Homepage
Ensure the video can be played easily on all screen sizes.

[W3C CSS Validator]() |
[W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftailwind-ms3-new.herokuapp.com%2F) |
[Lighthouse]() |
[JSLint.org]()

### FEATURES

[W3C CSS Validator]() |
[W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftailwind-ms3-new.herokuapp.com%2Ffeatures) |
[Lighthouse]() |
[JSLint.org]()

### CONTACT

[W3C CSS Validator]() |
[W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftailwind-ms3-new.herokuapp.com%2Fcontact) |
[Lighthouse]() |
[JSLint.org]()

### SIGNUP
I did not add a title to the quote section as it does not require one. 

[W3C CSS Validator]() |
[W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F8080-indigo-dog-2g4nj8u2.ws-eu08.gitpod.io%2Fsignup) |
[Lighthouse]() |
[JSLint.org]()

## App Pages and Features

### DASHBOARD
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### TEAM
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### TEAM DETAIL
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### ADD TEAM MEMBER
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### GUESTS
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### GUEST DETAIL
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### ADD GUEST
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### BOOKINGS
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### BOOKING DETAIL
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()

### ADD BOOKING
Markup Passed - Not linkable due to page being signin only

[W3C CSS Validator]() |
[Lighthouse]() |
[JSLint.org]()
 

***

## Bug & Issues Log
Below is a log of bugs or issues identified during testing as well as details on how they were solved. If a bug / issue was not able to be solved then this is marked with an unchecked box to the left hand side of the item.

- [] Get Advice button allowing you in without filling in both items
- [] Large numbers breaking charts
- [] Negative numbers allowed

1. [] - Features html errors

***

## Potential Future Features
- Enable sms and email to be sent to guests to leave reviews after bookings that populate directly in the software. 
- Have SMS and Email marketing options in the product to allow the restaurant owner to generate new bookings as well as manage existing ones.
- Create a reports section with reports to help restaurants better manage their system.
- Add a booking widget that restaurant owners can use on their websites / social media profiles etc to allow their guests to book directly into the software.
- Add a pos element where restaurants can manage their menu items and process sales through the system. 

***

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sreninc/financial-freedom)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://sreninc.github.io/financial-freedom/) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sreninc/financial-dreedom)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sreninc/financial-freedom)
2. Under the repository name, click the "Code" button and a dropdown menu will appear.
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

***

## Credits and Attributions

1. TailwindCSS for their wealth of components and a best in class CSS system.
1. Unsplash for their library of images
1. My Mentor, Maranatha Ilesanmi,  for continuous helpful feedback and guidance.
1. Fellow Code Institute students for their feedback and suggestions.
1. stackoverflow
1. Heroicons, the perfect companion to TailwindCSS
1. Timer Function on app searches: https://stackoverflow.com/questions/4220126/run-javascript-function-when-user-finishes-typing-instead-of-on-key-up
1. Creating a textarea that auto-resizes: https://stackoverflow.com/questions/454202/creating-a-textarea-with-auto-resize