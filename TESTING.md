<h1 align=center><strong>Waggy Box - Testing Information</strong></h1>

[Main README.md file](README.md)

[Deployed Site](https://waggy-box.herokuapp.com/)

<a href="https://trello.com/b/egLXahHC/testing" target=_blank>All Testing fixes can be reviewed here in this Trello Board</a>
### **Code Testing**
<a href="https://trello.com/b/egLXahHC/testing" target=_blank>All Testing fixes can be reviewed here in this Trello Board</a>


**Validator Testing** 

[W3C Markup Validation](https://validator.w3.org/)
 - W3C was used in the validation of both the HTML and CSS for the application.
    - Some minor errors were encountered with `<img>` tags not have an `alt` attribute.  These were resolved shortly after testing. The remainder of the errors noted across each of the pages can be reviewed [here](https://trello.com/b/egLXahHC/testing)  
    - No errors in the CSS were noted. 

[JSHint](https://jshint.com/) was used to validate the Javascript.
- When run the `stripe_elements.js` the JSHint validator these metrics were returned :
    - There are 3 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 8 statements in it, while the median is 5. 
    - The most complex function has a cyclomatic complexity value of 3 while the median is 2.
- No errors were returned. 
- There were two undefined variables: 
    - $ (for JQuery)
    - Stripe (this is from Stripe Docs)

- When run the `subscription.js` through the validator these metrics were returned: 
    - There are 4 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 8 statements in it, while the median is 4.
    - The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.
- No errors were returned.
- Two undefined variables: 
    - $
    - Stripe
- One unused variable :
    - clientSecret

[JSesprima](https://esprima.org/demo/validate.html)
- "Code is syntactically valid" for both files. 

[Python PEP8](https://pypi.org/project/autopep8/)
- The autopep8 extension was installed in the workspace. 
    - To install this enter this in the terminal: 
        -   `pip3 install --upgrade autopep8`

    In order for autopep8 to run, [pycodestyle](https://github.com/PyCQA/pycodestyle) is also required. 
    To instlal pycodestyle, enter this command into the terminal: 
    -  `pip3 install pycodestyle`

- Once these steps are complete, you can format the code into PEP8 formatting by entering this command into the terminal:
    - `autopep8 --in-place --aggressive --aggressive <.py file name>`

**Python Unit Testing** 

Unit testing was written up to test the core functionality of the site, including rendering pages, checkout and forms. 

- In the terminal type the following command: 

        python manage.py test <<app name>>

- The test results will be shown within the terminal.


### **User Story Testing**

1) View the site from any device
    - This application has been tested across all screen sizes & is shown to be fully responsive.  More about responsive testing undertaken in this application can be read in the below sections. 
2) Create an account.
    - With the inclusion of Django AllAuth, users can create an account & sign in, which gives them access to additional features across the application. 
3) Be able to login/out without purchasing a subscription.
    - Users do not have to purcahse a subscription to gain access to the internal features of the webiste. 
    - The reason behind this, is to allow potential customers get a feel for the type of service they are signing up to before committing to it. 
4) Gain additional features once I subscribe to a box.
    - With the use of the Subscription model & the active field, sections of the application are limited to only users with an active subscription. 
    - First time users, will not have a subscription, and so a filter to ensure if the users accessing do not have a subscription are also not allowed access to the entire application. 
5) Choose the box type I would like to subscribe to & enter my own details for delivery
    - This step can be achieved via the Subscription Overview page which is linked in the dashboard.
    - If a user tries to access the restricted pages without a subscription, an error page shows with directions on how to active their subscription. 
6) Access my subscription overview where I can review my own information and subscription type.
    - This can be done by the subscription overview page.  The page is personalised to each user, and displays the users subscription type an what price their subscription is.
    - If a user does not have an active subscription, then a link will be displayed redirecting the user to activate their subscription.

7) Cancel or change my subscription type as I wish.
    - When a user has an active subscription, they are given two options to change or cancel their subscription. 
    - If a user clicks on the cancel subscription link, a modal will pop up asking the user if they are sure they would like to cancel.  Once confirmed, the page will redirect & a message will display notifying a user of their cancellation. 
    - If a user chooses to change their subscription to another, they click on the change subscription link, which will direct them to the subscription types list, when chosen, then users will be redirected to the payment page. Once confirmed then users will be redirected to the subscription overview page with a message notifying the of a sucessful subscription update. 
8) Visit an online shop that contains any items from the previous months box.
    - If a user has an active subscription they are able to view the shop, which contains items from the previous months subscription box. 
9) Be able to purchase these items for delivery
    - Users are able to purchase items in the online shop.  This can be done by accessing the shop via the link in the navbar, clicking into the item they would like to purchase, and clicking the add to cart option. 
    - This then redirects the user to the shopping cart.  The user is then given the option to process their payment or return to purcahse more items.
    - If the user chooses to proceed to pay for their item, then they can proceed to the checkout page where they enter their information to pay for the item and their delivery information also.
10) Read information on any items from the previous months subscription service
    - This can be achieved by navigating into the shop page and clicking on the item they would lke to purchase. 
    - At the bottom of the page, users can then review the items description where they get a more in depth idea of the product. 
11) Find out more about the Waggy Box company as a whole
    - The site contains a short section and a further compelling About page is included in the site. Providing the user with sufficient information to satisfy a users curiosity without overloading them with more than they need.
12) Be able to submit a contact form to get in touch with the site owner
    - The site contains a contact form accessible through the main dashboard page and also through the site footer.
    - The contact form provides an easy way for the user to send an email to the site owner. 
    - The email that is sent to the shop owner includes all the needed info to reply directly to the sender.

