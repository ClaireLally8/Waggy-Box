<h1 align=center><strong>Waggy Box - Testing Information</strong></h1>

[Main README.md file](README.md)

[Deployed Site](https://waggy-box.herokuapp.com/)

<a href="https://trello.com/b/egLXahHC/testing" target=_blank>All Testing fixes can be reviewed here in this Trello Board</a>

### **Code Testing**

#### **Validator Testing** 

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


### **Manual Testing** 
Extensive manual testing was taken to ensure the application was responsive across all devices and achieved best practices in sofware developement. 

#### **Lighthouse**
An audit was completed using Lighthouse on the Waggy Box page.  Quite a low `performance` mark was retuned, and so in an attempt to increase this value, image files were converted from .png to .jpg. 
<img src="design/audit.png">
- After converting the images from .png to .jpg, the following audit was complete:
<img src="design/audit-new.png">
- Whist the best performance dropped by some, the best practices increased significantly. 
- Upon completing audits of several other websites, such as: 
    - [Code Like a Girl](https://code.likeagirl.io/)
    - [Medium](https://medium.com/)
- I learned that higher markings in Accessibility, Best Practices & SEO were more frequent than having a high performance rating. 

#### **Responsive Testing**

##### Large Desktop Testing
- 
    | Page | Responsive| Notes| 
    --- | --- | ---
    Index | Y | Fully Responsive. No horizontal scrollbar. 
    About | Y | Fully Responsive.  No horizontal scrollbar. 
    Contact | Y | Fully Responsive.  No horizontal scrollbar. Large button to send email, makes it easy to use. 
    Login | Y | Fully Responsive.  No horizontal scrollbar. Large button to login, makes it easy to use for all users. Form fields rendering quite small. Adjusted to make larger. 
    Sign-Up | Y | Fully Responsive.  No horizontal scrollbar. Large button to login, makes it easy to use for all users. Form fields rendering quite small. Adjusted to make larger. 
    Dashboard | Y | Page is fully responsive, no horizontal scrollbar or mis-sized images. 
    Subscription Overview | Y | Page is rendering correctly on large desktop screen. No mis-sized containers or content. 
    Membership List | Y |  Fully responsive, rendering correctly on large screen. 
    Membership Payment  | Y | Forms are significant in size, large buttons rendering correctly on large screensizes.
    Shop | Y | Four lines rendering per row.  No cramped spacing & stext sizes look well. 
    Shop Item | Y |  No incorreclty sizes content.  Font rendering an appropriate sizes. 
    Cart | Y | Rendering well.  Large buttons making accessible for all users.  Large spacing between the primary & secondary button. 
    Checkout | Y | This page followed a similar structure to the Membership Payment page.  See notes for this. 
    Checkout Success | Y | Page rendering as intended.  No incorrect shaped content & fonts sizes are appropriate. 


##### Laptop Screen Testing (Same results as large monitor)
- 
    | Page | Responsive| Notes| 
    --- | --- | ---
    Index | Y | Fully Responsive. No horizontal scrollbar. 
    About | Y | Fully Responsive.  No horizontal scrollbar. 
    Contact | Y | Fully Responsive.  No horizontal scrollbar. Large button to send email, makes it easy to use. 
    Login | Y | Fully Responsive.  No horizontal scrollbar. Large button to login, makes it easy to use for all users. Form fields rendering quite small. Adjusted to make larger. 
    Sign-Up | Y | Fully Responsive.  No horizontal scrollbar. Large button to login, makes it easy to use for all users. Form fields rendering quite small. Adjusted to make larger. 
    Dashboard | Y | Page is fully responsive, no horizontal scrollbar or mis-sized images. 
    Subscription Overview | Y | Page is rendering correctly on large desktop screen. No mis-sized containers or content. 
    Membership List | Y |  Fully responsive, rendering correctly on large screen. 
    Membership Payment  | Y | Forms are significant in size, large buttons rendering correctly on large screensizes.
    Shop | Y | Four lines rendering per row.  No cramped spacing & stext sizes look well. 
    Shop Item | Y |  No incorreclty sizes content.  Font rendering an appropriate sizes. 
    Cart | Y | Rendering well.  Large buttons making accessible for all users.  Large spacing between the primary & secondary button. 
    Checkout | Y | This page followed a similar structure to the Membership Payment page.  See notes for this. 
    Checkout Success | Y | Page rendering as intended.  No incorrect shaped content & fonts sizes are appropriate. 

##### Tablet Testing
- 
    | Page | Responsive| Notes| 
    --- | --- | ---
    Index | Y | Fully Responsive. No horizontal scrollbar visible and all sections rendering correctly. 
    About | Y | Fully Responsive.  No horizontal scrollbar. Images rendering slightly off - plan to adjust sizing on these. (Adjusted to fit full screen & changed height of images)
    Contact | Y | Fully Responsive.  No horizontal scrollbar. Large button to send email, makes it easy to use on all screen sizes. 
    Login | Y | Rendering correctly.  Form fields are slightly smaller than hoped, however due to limited knowledge with allauth, unsure on how to adjust this. Large button making is increasingly user friendly.
    Sign-Up | Y | Rendering correctly.  Form fields are slightly smaller than hoped, however due to limited knowledge with allauth, unsure on how to adjust this.  Use of a large button to make it increasingly user friendly.
    Dashboard | Y | Page is fully responsive, no horizontal scrollbar or mis-sized images or unintended white space.  
    Subscription Overview | Y | Page is rendering correctly on table. No mis-sized containers or content. 
    Membership List | Y |  Fully responsive, rendering correctly on tablet screen.  Subscriptoin types rendered on fully screen width, makes it friendly for all users of all abilities. 
    Membership Payment  | Y | Forms are acceptably sized, large buttons rendering correctly on tablet screens.
    Shop | Y | Three items rendering per row.  No cramped spacing & stext sizes look well. 
    Shop Item | Y |  No incorreclty sizes content.  Font rendering an appropriate sizes. 
    Cart | Y | Rendering well.  Large buttons making accessible for all users.  Large spacing between the primary & secondary button.  Items content is slightly cramped, however limitations on content due to being a table. 
    Checkout | Y | This page followed a similar structure to the Membership Payment page.  See notes for this. 
    Checkout Success | Y | White space rendering on main image.  Adjusted correctly & resolved by decreasing the padding on tablet screens & smaller. 

##### Tablet Testing
- 
    | Page | Responsive| Notes| 
    --- | --- | ---
    Index | Y | Fully Responsive. No horizontal scrollbar visible and all sections rendering correctly. 
    About | Y | Fully Responsive.  No horizontal scrollbar. Image rendering correctly & with shadow on main text, it's clear to see.  Removed padding-top on dog images to appear correctly.
    Contact | Y | Fully Responsive.  No horizontal scrollbar. Large button to send email, makes it easy to use on all screen sizes. 
    Login | Y | Rendering correctly.  Form fields are slightly smaller than hoped, however due to limited knowledge with allauth, unsure on how to adjust this. Large button making is increasingly user friendly.
    Sign-Up | Y | Rendering correctly.  Form fields are slightly smaller than hoped, however due to limited knowledge with allauth, unsure on how to adjust this.  Use of a large button to make it increasingly user friendly.
    Dashboard | Y | Page is fully responsive, no horizontal scrollbar or mis-sized images or unintended white space.  
    Subscription Overview | Y | Page is rendering correctly on table. No mis-sized containers or content. 
    Membership List | Y |  Fully responsive, rendering correctly on mobile screen.  Subscriptoin types rendered on fully screen width, makes it friendly for all users of all abilities. 
    Membership Payment  | Y | Forms are accurately sized being full width of screen, large buttons rendering correctly on mobile screens.
    Shop | Y | Three items rendering per row.  No cramped spacing & stext sizes look well. 
    Shop Item | Y |  No incorreclty sizes content.  Font rendering an appropriate sizes. 
    Cart | Y | Rendering well.  Not optimised for small phone screen, due to cramped information.  Some styling customised for small mobile, but product image still rendering small despite attempts to resolve. 
    Checkout | Y | This page followed a similar structure to the Membership Payment page.  See notes for this. 
    Checkout Success | Y | Rendering well.  Dark text visible against the light background. Dark text not fully visible.  Looking into making this better - `text-shadow: 0.8px 0.8px gray;` was added on screens less than 1000px to the sub text.

### **Bugs Discovered** 

#### Resolved Bugs.

1) A significant issue with Stripe working in the subscription during creation was discovered in getting the Stripe Token to correctly populate.  Thanks to the help from Simen Daehlin, this was resolved by manually adding the public key for Stripe in the membership_payment.html page. 
2) When the Database is empty, an error occurs with the subscription. 
    - This was discovered to be down to the lack of memberships.
    - Resolved by commenting out two lines during development & re-filling these lines once deployment was ready.
    - Further developement would be required to resolve fully without lines needing to be commented during development.
3) A large issue came up when attempting to move from SQLite to PostgreSQL databases. 
    - Upon inspection, the error seemed to be coming from the CountryField in the forms.
    - To resolve, I removed this form & undone any migrations relating to this.
    - A future feature I would like to re-incorporate into the application would be country selections. 
4) Gitpod was unable to access postgreSQL database for testing
    - Due to the free Hobby-dev postgres package selected when setting up the heroku database, I was not able to set the permissions necessary to alow Django to create a test database when running manage.py test.
    - To fix this I reverted to accessing my sqlite3 database for testing.

#### Unsolved Bugs.
1) Cart page images not hiding on small screen.
    - This seems to be an issue with the MDB framework, however when relevant classess were applied to product items, instead of hiding one image on a small screen & displaying another, both images were rendering to display.
2) Allauth form fields rending significantly smaller than desired.  Due to a limited understanding of Django Allauth, I was unable to resolve this, however would like to look into this in the near future. 


### User Testing

- A site wide User test was conducted.  The user was presented with the following aims:
    - You are hte owner of a large dog breed.  After tirelessly seeking good quality dog toys, you have given up. Until you come across the Waggy Box application.
    - Navigate to the `About Us` page to learn more about the Waggy Box company.
    - After reading the about page, you would love to sign up and try out the service. Navigate to the sign up page & create an account. 
    - Review the subscriptions available to you and purchase the `Premium` subscription type.
    - Enter your delivery and payment information and purchase the subscription.
    - Now you would like to review some of the items in last months box, to get a good idea of the type of products you are sent each month.
    - You spotted an item you would like to purchase.  You would like to find out more about the item, and purchase two of these products.
    - Enter your details & checkout.
    - Now your item has arrived, but there seems to be an issue with the payments and you were charged for three items instead of 2.  You need to get in touch with the site owner to resolve this.

- User Testing Feedback 
    - The option to allow users to subscribe straight from signing up. (Added to future implementations)
    - Adjusting the width of buttons to allow for more mobile friendly user - this was done & has greatly improved the UX. 


### **Manual Testing Navigation.** 

#### 