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

## Testing
For all pages check the responsiveness, image quality, video quality, text display, general UX and readibility of the page on: 
1. Chrome Browser on the 6 pre-set screen sizes in inspection mode.
1. Android Phone on Chrome and Samsung browsers.
1. Microsoft Edge Browser on the 6 pre-set screen sizes in inspection mode.

### Homepage
Ensure the video can be played easily on all screen sizes.

[W3C CSS Validator]() |
[W3C Markup Validator]() |
[Lighthouse]() |
[JSLint.org]()

### About
1. Try to send the contact form with incorrect email address formatting. 
1. Try to send the contact form with no information provided. 
1. Try to send the contact form with no category selected.
1. Ensure the contact form is received to the email address provided.
1. Does the confirmation message show once the form is submitted.

[W3C CSS Validator]() |
[W3C Markup Validator]() |
[Lighthouse]() |
[JSLint.org]()

### Dashboard
1. Does the new user information show correctly.
1. Can I add a negative value to the add item form. 
1. Can I choose an expense category for income and vice-versa.
1. Does the correct paid when option show for each frequency selected.
1. Does the bar chart show correctly for very high values. 
1. Can I edit and delete items in both the income and expenses tables. 
1. Does the bar chart update correctly when creating, editing and deleting items. 
1. Does my information get saved correctly when I leave the webpage and come back at a later time.
1. Does the get your advice button only work when I have entered at least 1 income and 1 expense.
1. When editing an item can I change the type of the item.

[W3C CSS Validator]() |
[W3C Markup Validator]() |
[Lighthouse]() |
[JSLint.org]()

### Results
1. Does the dynamic text show the correct response based on my income and expenses?
1. Do the pie charts show the correct category information?
1. Do the charts display correctly with large values and small values mixed together?
1. Do the advice cards appear correctly based on the pre-defined triggers?
1. Do all the blog and action links function correctly and open in the same browser window?
1. Can I go back to the dashboard page with ease?
1. If no advice is available does the success text appear correctly?

[W3C CSS Validator]() |
[W3C Markup Validator]() |
[Lighthouse]() |
[JSLint.org]()

***

## Bug Log
Below is a log of bugs or issues identified during testing as well as details on how they were solved. If a bug / issue was not able to be solved then this is marked with an unchecked box to the left hand side of the item.

- [] Get Advice button allowing you in without filling in both items
- [] Large numbers breaking charts
- [] Negative numbers allowed

***

## Potential Future Features
- Allow users to create an account that saves their information to website servers rather than relying on localStorage for the information. 
- Add features for Assets & Liabilities to provide a fully rounded personal finance analysis. 
- Offer paid services for digital coaching and advice.
- Localized content for countries other than the Republic of Ireland.
- Allow upload of financial statements or linking to financial institutions through the one banking system so users don't have to manually input their data. 
- Create a budget tracker and goal setting feature that allows users to track their performance over time rather than a snapshot.  

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

1. Code to sort maps by key values: https://stackoverflow.com/questions/31158902/is-it-possible-to-sort-a-es6-map-object/51242261
1. chartjs.org used for all charts and examples taken from their website
1. chartjs-datalabels used to alter the display of tables 
1. Bootstrap
1. Images
1. My Mentor, Maranatha Ilesanmi,  for continuous helpful feedback and guidance.
1. Fellow Code Institute students for their feedback and suggestions.
1. stackoverflow
1. Feather icons
1. Unsplash Images

1. [Flaticon](www.flaticon.com)
    1. [Homepage > Income](https://www.flaticon.com/free-icon/salary_3135706?term=income&page=1&position=4&page=1&position=4&related_id=3135706&origin=search)
    1. [Homepage > Expenses](https://www.flaticon.com/free-icon/expenses_4093960?term=expense&page=1&position=18&page=1&position=18&related_id=4093960&origin=search)