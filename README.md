# Bookler

[Click To See Live Site](http://tailwind-ms3-new.herokuapp.com/)

The Bookler website provides a paid solution for restaurants who want to move away from pen & paper bookings to a digital solution. It's key features are a complete CRM solution, use on any device and easy management of both bookings and guests.

[![Bookler](static/img/team.jpg)](https://sreninc.github.io/tailwind-ms3/)

## Table of Content 

- [Project Stories](#project-stories)
    - [User Stories](#user-stories)
    - [Business Stories](#business-stories)

- [Design and UX](#design-and-ux)
    - [Design and UX Research](#design-and-ux-research)
    - [Website Wireframes](#website-wireframes)
    - [Website Mockups](#website-mockups)

- [Website Pages and Features](#website-pages-and-features)
    - [Homepage](#homepage)
    - [About](#about)
        1. [Contact](#contact)
    - [Dashboard](#dashboard)
        1. [New User](#new-user)
        1. [Add Item Form](#add-item-form)
        1. [Income and Expenses Tables](#income-and-expenses-tables)
        1. [Income and Expenses Bar Chart](#income-and-expenses-bar-chart)
    - [Results](#results)
        1. [Day By Day Line Graph](#day-by-day-line-graph)
        1. [Income and Expenses Pie Charts](#income-and-expenses-pie-charts)
        1. [Advice Cards](#advice-cards)
        1. [Dynamic Text](#dynamic-text)

- [Testing](#testing)
    - [Homepage](#homepage)
    - [About](#about)
    - [Dashboard](#dashboard)
    - [Results](#results)

- [Bug Log](#bug-log)

- [Potential Future Features](#potential-future-features)

- [Deployment](#deployment)

- [Credits and Attribution](#credits-and-attribution)

***

## Project Stories

### User Stories
As a user I want to...
- Input my monthly income and expenses so I can see where my money is going.
- Update and/or delete the items I enter incase I make an error.
- Have my information stored so I can come back to the website at a later date and not have to re-enter the information I previously provided. 
- See my data represented graphically to help me understand where my money is going. 
- Receive advice based on my inputted income and expenses to help me improve my personal finances.
- Be able to contact the website owner incase I have a question or get stuck.

### Business Stories
As the website owner I want to...
- Help users educate themselves on their personal finances.
- Allow users to contact me if they have questions or encounter issues.
- Provide further reading and action links to users so I provide additional assistance and build loyalty.
- Allow users to update their provided information to encourage repeat visits eventually allowing me to build paid partnerships with the advice partners offered to users.

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

### TEAM

### TEAM DETAIL

### GUESTS

### GUEST DETAIL

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
[W3C Markup Validator]() |
[Lighthouse]() |
[JSLint.org]()

### FEATURES

### CONTACT

### SIGNUP

## App Pages and Features

### DASHBOARD

### TEAM

### TEAM DETAIL

### ADD TEAM MEMBER

### GUESTS

### GUEST DETAIL

### ADD GUEST

### BOOKINGS

### BOOKING DETAIL

### ADD BOOKING
 

***

## Bug Log
Below is a log of bugs or issues identified during testing as well as details on how they were solved. If a bug / issue was not able to be solved then this is marked with an unchecked box to the left hand side of the item.

- [] Get Advice button allowing you in without filling in both items
- [] Large numbers breaking charts
- [] Negative numbers allowed

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