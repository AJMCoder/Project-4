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

- Corrected an error in the code where 'chr' was written, rather than 'ch' resulting in the code not running correctly and not printing the table or content.
- When testing the code to see if inputting coordinates was working, i discovered that the grid wasnt being displayed at all. I tried re-writing the 'check shot' function to see if it was interfering with the results, but that didnt fix it. However, this did help me discover another issue, as the original code for this section was not functioning properly and didn't allow the user to enter another guess.
- In order to fix my original error above, i scanned through the written code and could see that the the 'show_board' and surrounding code at the bottom had not been grouped into a function, so by moving the code into a for loop fucntion, the list then became workable.
- When adding a new ship, i realised that when writing the second check_shot function that it wasn't as simple as re-writing it the same as ship 1. I needed to add an 'elif' statement so that if there is a miss for both, the code can understand that it has missed both ships not just 1 of them. 
- When testing after adding a third ship location, the terminal after the first coordinate input was returning a ValueError message, pointing to line 168 as the culprit. I tried re-writing that line of code, ensuring it was written out correctly and included the 'ship3' in its command, however the same message was beign returned each time. So, i started working from the top-down, analysing my code to see if i had missing something earlier on. Within the check shot function i noticed (after many scans) that in the return at the bottom of the function, 'ship3' was not defined. Upon editing this mistake and adding this in, the board now functioned again properly.
- During some of the final testing stages, it was discovered that there was no message to the user if all attempts had been used, to say the game had ended and that they had lost. This was rectified and added in as a feature.
- When putting my code through the CI Python Linter, i was met with a multitude of errors, ranging from ' trailing whitespace', 'line too long', missing white space', and 'do not use bare "except"'. Running through my code again, i removed the whitespace where needed and additinally added whitespace where necessary. I also shortened lines of code to fit the 80 character limit by either rewording or using a '\' to move to next line. The "except" term required the addition of 'Exception:' as this is the base type for all 'Regular' exceptions rather than catching all of them, some of which i wouldnt want to catch, if left with just a bare except.
- During a test from my mentor, it was found that the play_again function was accepting any input as a 'yes' input. To fix this, I changed the function to require a specific 'yes' or 'no' input, otherwise: 'Invalid input. Please enter yes or no.', would be displayed to the user.

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