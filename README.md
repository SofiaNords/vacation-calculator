<h1 align="center">Vacation Calculator</h1>

[View the live project here.](https://vacation-calculator-0f929794e117.herokuapp.com/)

The Vacation Calculator is a helpful tool designed to assist users in calculating their entitlement to paid vacation days in accordance with the Swedish Vacation Act. By inputting specific parameters, users can determine the number of paid vacation days they will receive during a given vacation year.

<h2 align="center"><img src="assets/images/vacation-calculator.png">

## User Experience (UX)

### User Stories

#### First Visitor Goals

1. As a First Time Visitor, I want to easily understand the main purpose of the application.

2. As a First Time Visitor, I want to know right away how to start and a clear and concise step-by-step guidance in how to use the application.

3. As a First Time Visitor, I want feedback if my input is not correct in some way.

4. As a First Time Visitor, I want to be able to get more detailed information about rules in the Swedish Vacation Act.

#### Returning Visitor Goals

1. As a Returning Visitor, I want to be able to start the calculations right away and follow a clear and concise step-by-step guidance in how to use the application.

2. As a Returning Visitor, I want feedback if my input is not correct in some way.

3. As a Returning Visitor, I want to be able to choose if I want more detailed information about the rules in the Swedish Vacation Act or not. 

## Flow Chart

I used Canva to produce my flow chart. 

https://www.canva.com/

The flow chart largely corresponds to the final product except for the "Explain absence data" feature that I added during development. 

[View the Flow Chart of the project here.](https://www.canva.com/design/DAF-QQF54tg/LDPiva1vMDlR_EAO3aPBlw/view?utm_content=DAF-QQF54tg&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## Features

### Existing features

#### Start the calculator

- Welcomes the user
- Explains the conditions
- Let the user enter the vacation year

<h2 align="center"><img src="assets/images/start_calculator.png">

#### Select and validate vacation year

- When the user enters the vacation year, the input is validated to ensure that it is in the correct date format.

#### Enter and validate employment date

- When the user enters the employment date, the input is validated to ensure that it is in the correct date format.

<h2 align="center"><img src="assets/images/enter-validate-employment-date.png">

#### Enter and validate holiday entitlement

- When the user enters their holiday entitlement the input is converted to an integer, the validate function controls that it is at least 25 days (which is the minimum by law) and that the format is correct.

<h2 align="center"><img src="assets/images/enter-validate-holiday-entitlement.png">

#### Explain absence data

- Before the user can enter their absence data, they get a choice and a recommendation to read more about absence data. The user is responsible for entering correct absence data and should be aware of the rules that apply.

<h3 align="center"><img src="assets/images/choose-explain-absence-data.png"></h3>

- If the user choose to read more about absence data the following text is presented:

<h3 align="center"><img src="assets/images/explain-absence-data-1.png"></h3>
<h2 align="center"><img src="assets/images/explain-absence-data-2.png"></h2>


#### Enter and validate absence data

- When the user enters their absence data the input is converted to an integer. The validate function controls the format of the input and print out if it's not valid.

<h2 align="center"><img src="assets/images/enter-validate-absence-data.png"></h2>

#### Calculate employment days

- The function calculates how many employment days the user got during the vacation year by comparing the employment date with the last day of the vacation year.

#### Calculate paid vacation days

- The function calculates how many paid vacation days the user will get. It reduces leave of absence from total employment days. In the next step, the remaining days are related to the days in the current vacation year and are multiplied by the vacation entitlement. At last the result is being rounded up just as it should be according to the law.

## Technologies Used

### Languages Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries Used

#### Python Standard Libraries

<h5>Datetime Module</h5>
- I used the Datetime Module to parse vacation year and employment date into datetime objects and to be able to validate the input format.

https://stackoverflow.com/questions/74091035/how-do-i-validate-a-date-format-with-python

<h5>Math Module</h5>
- I used the Math Module to be able to round up the result of the paid vacation days.

https://www.w3schools.com/python/ref_math_ceil.asp


#### Other Libraries

<h5>Pyfiglet Module</h5> 
- I used the Pyfiglet Module to style the program’s header and enhance the visual presentation of the application.

https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

<h5>Colorama Module</h5>
- I used the Colorama Module to be able to use different colours to the text.

https://stackoverflow.com/questions/46349444/how-to-add-color-to-text-in-python


## Testing

### Validator Testing

[The CI Python Linter](https://pep8ci.herokuapp.com/) displays "All clear, no errors found".

<img src="assets/images/ci-python-linter.png">

### User Stories Testing

#### First Visitor Goals

1. As a First Time Visitor, I want to easily understand the main purpose of the application.

        When users launch the application, they are greeted with a brief and clear information message. The text explains that the app functions as a vacation days calculator, specifically tailored to Swedish vacation law. It assumes that the preceding year serves as the qualifying year for calculating paid vacation days.

2. As a First Time Visitor, I want to know right away how to start and a clear and concise step-by-step guidance in how to use the application.

        The user is asked to enter the vacation year they want to calculate in the first step right after the information text. In the following steps the user is asked to enter employment date, holiday entitlement etc.

3. As a First Time Visitor, I want feedback if my input is not correct in some way.

        If the user enters a vacation year, an employment date or a holiday entitlement in the wrong format an error messege appears that encourage the user to try again.

4. As a First Time Visitor, I want to be able to get more detailed information about rules in the Swedish Vacation Act.

        The user get's a choice and a recommendation to read more about absence data. If the user enters y (yes) a detailed description of certain types of absence that qualifies for vacation pay appears.

#### Returning Visitor Goals

1. As a Returning Visitor, I want to be able to start the calculations right away and follow a clear and concise step-by-step guidance in how to use the application.

        The user is asked to enter the vacation year they want to calculate in the first step right after the information text. In the following steps the user is asked to enter employment date, holiday entitlement etc.

2. As a Returning Visitor, I want feedback if my input is not correct in some way.

        If the user enters a vacation year, an employment date or a holiday entitlement in the wrong format an error messege appears that encourage the user to try again.

3. As a Returning Visitor, I want to be able to choose if I want more detailed information about the rules in the Swedish Vacation Act or not. 

        The user get's a choice and a recommendation to read more about absence data. If the user already knows about the absence data rules they can enter n (no) and proceed and enter their absence data.

## Credits

- I was inspired by my classmate Raneem Yad to use the pyfiglet module. She also shared where I could find instructions on how to install and use pyfiglet.

- My Mentor, Spencer Barriball, for continuous helpful feedback.





