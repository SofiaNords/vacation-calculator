## Features

### Existing features

#### Start the calculator

- Welcomes the user
- Explains the conditions
- Let the user enter the vacation year

#### Select and validate vacation year

- When the user enters the vacation year, the input is validated to ensure that it is in the correct date format.

#### Enter and validate employment date

- When the user enters the employment date, the input is validated to ensure that it is in the correct date format.

#### Enter and validate holiday entitlement

- When the user enters their holiday entitlement the input is converted to an integer, the validate function controls that it is at least 25 days (which is the minimum by law) and that the format is correct.

#### Enter and validate absence data

- When the user enters their absence data the input is converted to an integer. The validate function controls the format of the input and print out if it's not valid.

#### Calculate employment days

- The function calculates how many employment days the user got during the vacation year by comparing the employment date with the last day of the vacation year.

#### Calculate paid vacation days

- The function calculates how many paid vacation days the user will get. It reduces leave of absence from total employment days. In the next step, the remaining days are related to the days in the current vacation year and are multiplied by the vacation entitlement. At last the result is being rounded up just as it should be according to the law.

## Libraries

### Python Standard Libraries

- I used the datetime module to to parse vacation year and employment date into datetime objects and to be able to validate the input format.

https://stackoverflow.com/questions/74091035/how-do-i-validate-a-date-format-with-python




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
