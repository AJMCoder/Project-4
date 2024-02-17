# CityServe Tennis League

Project 4...

## Table of contents

## Introduction

Welcome...

## User Experience (UX)
### Over Goals of the site
### Target Audience
### Site Goals

## User Stories & Aims



## Technologies Used
### Frameworks, Libraries and Programs

- Bootstrap 5: 
- GitHub:
- Font Awesome:
- Visual Studio Code:

### Languages

- HTML
- CSS
- JavaScript

## Features
### Existing Features



### Future Developments

**Coming Soon**


## Testing
### User story testing



### Validator Testing



### General Continuous Testing
#### Responsiveness

#### Browser Compatibility



## De-bugging:

- When creating a modal for the Login button, now popup was being shown. Re-reading the code line by line of the modal and the Login section made me realise that the data-bs-target was not correctly aligned with what it was trying to pull from and was resulting in no popup. Renaming it to match the modal code section finally allowed the modal to appear. 
- Upon creating a custom CSS file, I noticed that any styles that were being added, we not affecting the site. I re-wrote the link to the css file, ensuring it was correct but that didn't result in a fix. Browsing the internet for answers, I came across a comment that showed the order of which the CSS custom file and Bootstraps CSS file should be written in. I moved the custome CSS file below Bootstraps and it fixed the issue, allowing me to use custom CSS styles alongside.


## Remaining Bugs:

- No remaining bugs.

# Deployment:

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:

- Clone this repository.
- Create a new Heroku app.
- In the settings, within the 'Config Vars', add the KEY/Value pairs: PORT. Set this to 8000.
- Set the buildbacks to Python and NodeJs in that order.
- Link the Heroku app to the repository.
- Click Deploy.

# Credits

- Inspiration taken from [Dr. Codie](https://drcodie.com/battleships-game-in-python/).
- Resources used from [Codecademy](https://www.codecademy.com/resources/docs/swift/arrays), and Mimo Coding App.