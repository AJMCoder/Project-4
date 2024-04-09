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
- When resizing my screen to test compatiblity i noticed that the Navbar was not reacting accordingly and when at medium-small sizes, part of the end of it was missing from the screen. I tried adjusting the Bootstrap CSS but it didn't work. I went back through the Boostrap website guides for Navbars and realised I had incorrectly insert the container class and not made it fluid. Once added, the Navbar responded to the change in screen size and reacted how it was intended.
- When at full screen, the landing page image was not displaying correctly and was positioned so that the head of the player was missing from the screen. Upon reading through my code, I saw that the styling for the image was set to 'Center', and tried re-styling the image to be at the 'Bottom'. This fixed the issue and remained perfectly scaled for smaller devices also.
- When installing the Django files, I was met with numerous error messages stating my commands not being recognised within the terminal. With the assistance of a mentor i was able to rectify this problem by by selected a new default terminal 'command prompt'.
- During the Django installation I was met with another issue whereby my 'events' folder was not being recognised why trying to run a server and thus was resulting in a failed load. Running through my code i could see that URLPatterns path for the folder was writen okay, but i had forgotten to include the '*from events import views as events_views*'

## Remaining Bugs:

- FOOTER WILL NOT REMAIN A THE BOTTOM OF THE PAGE.

# Deployment:



# Credits

- Inspiration taken from [Net Ninja](https://www.youtube.com/watch?v=yCCIztB-S_k&list=PL4cUxeGkcC9joIM91nLzd_qaH_AimmdAR&index=8).
- Responsive Font Size formula adapted from [Matthew James Taylor](https://matthewjamestaylor.com/  responsive-font-size#:~:text=To%20make%20font%20size%20responsive%20in%20steps%2C%20set%20the%20base,relative%20to%20the%20screen%20width.).
- Resources used from [Codecademy](https://www.codecademy.com/resources/docs/swift/arrays), and Mimo Coding App.