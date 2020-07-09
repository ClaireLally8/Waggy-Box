<div style="text-align:center;"><img src="static/images/logo.png" max-height=200px></div>

<div style="text-align:center; color:#ff3a95;">

# [Waggy Box](https://waggy-box.herokuapp.com/)

</div>
Waggy Box (fictional) is a dog treat and toy subscription box for pet owners in Ireland. Finding durable toys and tasty treats has been the most difficult task I've encountered as a pet owner.  So, the idea of Waggy Box was created, to allieviate this difficulty.  All toys are tried and tested by my own three dogs, and only the toys approved by these guys will be featured in the monthly box. 

---
## **User Experience**

#### **User Stories**

- As a customer I want to: 
    - View the site from any device
    - Create an account.
    - Be able to login/out without purchasing a subscription. 
    - Gain additional features once I subscribe to a box.
    - Choose the box type I would like to subscribe to & enter my own details for delivery
    - Access my subscription overview where I can review my own information and subscription type. 
    - Cancel or change my subscription type as I wish.
    - Visit an online shop that contains any items from the previous months box.
    - Be able to purchase these items for delivery
    - Read information on any items from the previous months subscription service
    - Find out more about the Waggy Box company as a whole
    - Be able to submit a contact form to get in touch with the site owner
<br>

---

## **Design** 

Waggy Box was designed with ease and playfulness in mind. Making use of bright colours and two sans-serif fonts with varying weights to ensure accurate emphasis is given to the secions. 

This project was aimed at dog owners and dog lovers, who regularly struggle to find great toys and treats tasty enough to train and play with their furry friends. 

Waggy-Box' site is split into two parts :

**Free Tier:**

Users are initially registered on the free tier page.  They have a limited view of what the site offers, in terms of being able to navigate to the subscription page and to contact the site owners. 

**Paid Tier:**

The paid tier users have full access to the website.  They can review items in next month's box, shop items from the previous month, contact the site owner and adjust their own subscription plan. 


#### **Colour Scheme**
<img src="colour-scheme.png">

#### **Typography**
 
 - **Montserrat:**
    - The primary font across the webiste, using four different weights: 200, 300, 400, 500
    - Montserrat is a clean font used regularly, so it is both an attractive and appropriate choice to be the primary font across the site.

- **Rubik**
    - Rubik was used for the main page headings, of a weight 500 for the page headings and 300 for the sub-heading sections.
    - Rubik added the element of playfulness to the application, without making it appear childish. 

### **Frameworks**
- [MDBoostrap](https://mdbootstrap.com/)
    - Taking the responsiveness of Bootstrap and the front-end UI of Materialize, MDBoostrap makes use of both of these. So all aspects of the site were clean and accessible for all users. 

- [JQuery](https://code.jquery.com/jquery/)
    - In order to minimalise the amount of Javascript used across the application, I chose to implenent a lot of the JS functionality with JQuery.

- [Django 3.0](https://docs.djangoproject.com/en/3.0/releases/3.0/) 
    - Django is a free and open-source web framework that I've used to render the back-end Python code with the front-end MDBoostrap and my own custom HTML and CSS. 

### **Icons**

- [MDBoostrap Icons](https://mdbootstrap.com/)
    - A majority of icons used across the website were taken from MDBoostrap documentation. These icons are adapted from both Font Awesome and Materialize icons due to their clean appearence. 
- [Canva](https://www.canva.com/) 
    - Canva was the source of other Icons.  I purchased a pro subscription to canva for the duration of the project.  Canva has an extensive library of images and icons for use by designers and developers alike.
    - The Waggy Box logo was also created using a canva logo template and customised to fit the feel and appearence of Waggy Box.

### **Wireframes**

- **Desktop**
    - [Landing page](design/wireframes/desktop/landing-desktop.png)
    - [About page](design/wireframes/desktop/about-desktop.png)
    - [Contact](design/wireframes/desktop/contact-desktop.png)
    - [Login](design/wireframes/desktop/login-desktop.png)
    - [Signup](design/wireframes/desktop/signup-desktop.png)
    - [Dashboard](design/wireframes/desktop/dashboard-desktop.png)
    - [Subscription-Overview](design/wireframes/desktop/subscription-desktop.png)
    - [Shop](design/wireframes/desktop/shop-desktop.png)
    - [Checkout](design/wireframes/desktop/checkout-desktop.png)

- **Tablet**
    - [Landing page](design/wireframes/tablet/landing-tablet.png)
    - [About page](design/wireframes/tablet/about-tablet.png)
    - [Contact](design/wireframes/tablet/contact-tablet.png)
    - [Login](design/wireframes/tablet/login-tablet.png)
    - [Signup](design/wireframes/tablet/signup-tablet.png)
    - [Dashboard](design/wireframes/tablet/dashboard-tablet.png)
    - [Subscription-Overview](design/wireframes/tablet/subscription-tablet.png)
    - [Shop](design/wireframes/tablet/shop-tablet.png)
    - [Checkout](design/wireframes/tablet/checkout-tablet.png)

- **Mobile**
    - [Landing page](design/wireframes/mobile/landing-mobile.png)
    - [About page](design/wireframes/mobile/about-mobile.png)
    - [Contact](design/wireframes/mobile/contact-mobile.png)
    - [Login](design/wireframes/mobile/login-mobile.png)
    - [Signup](design/wireframes/mobile/signup-mobile.png)
    - [Dashboard](design/wireframes/mobile/dashboard-mobile.png)
    - [Subscription-Overview](design/wireframes/mobile/subscription-mobile.png)
    - [Shop](design/wireframes/mobile/shop-mobile.png)
    - [Checkout](design/wireframes/mobile/checkout-mobile.png)    


## **Features** 

Elements on every page: 
- Navbar
    - Waggy Box makes use of a single navbar with varying elements depending on whether a user is logged in. 
        - Not logged in: <img src="https://i.ibb.co/DDSFqtW/Screenshot-2020-07-09-at-21-01-32.png">
        - Logged in: <img src="https://i.ibb.co/n3qXrC4/Screenshot-2020-07-09-at-20-59-18.png">
        - On mobile the navar turns into a burger menu as such where users click on the hamburger icon and opens a drop down for the menu: 
         <img src="https://i.ibb.co/pQ4Y5VZ/Screenshot-2020-07-09-at-21-02-47.png">

    - The navbar contains links to the home page, where users can gather information about the company when they're not logged in. When a user is logged in, the home link brings the user to the main dashboard page, allowing users to review their subscription, access the shop and contact the site owner.
    - The Get Started link brings users to the sign up page where they can sign up for the application.
    - The login link brings users to the login page, where they can sign into the application.
    - When logged in, users can view the shop page also from the navbar, allowing them to review teh items for sale if htey have an active subscrption.  If the subscription is not active, it will bring users to a page directing them to create a subscription. 

- Footer
    - There is one footer throughout the entire application.
        - On Desktop: <img src="https://i.ibb.co/SVdXy31/Screenshot-2020-07-09-at-20-57-02.png">
        - On Mobile: 
        <div style="text-align:center;">
        <img src="https://i.ibb.co/b3wKJ5P/Screenshot-2020-07-09-at-21-06-39.png" height=200>
        </div>
    - The footer is split into three core sections: Social Media, Navigation & Contact aspects.
        - Social Media section contains three icons, where when clicked bring users to Facebook, Twitter and Instagram, with the intention of bringing users to the relevant pages assosicated with Waggy Box. 
        - Navigation section has three links, About Us which when cliced reidrects the user to the about page, Contact us which brings the user to the contact page and then get started which brings the user to the registration page.
        - Contact Us section contains all the (fictional) contact information for the Waggy Box company, including the address and a contact number for the site owners. 

- Blue was chosen for both of these features due to the appealing contrast it has aganist the white background, and matches well with both Black and white font colors. The blue also incorporates the playful element that was achieved throughout the website. 

### **Landing Page**
The landing page is split into three core components: 

- Main Landing Section 
    - This area contains the main landing image, which is of a pug lying with his belly up, looking straight up at the camera.  This image was chosen due to the cheeky, fun element involved & of course, the cute aspect of it too. 
    - Encorporated in this section is also a short about, on how Waggy Box was founded and why it came to be.  This allows users to get a deeper understanding of what the sites purpose is. 
- How it works Section
    - The how it works section contains three card aspects, which is a short snippet of how the box works.  This area was changed multiple times throughout the application due to varying ideas of how I would have liked the page to be presented.  The final settling, was three card elements, with a shaodw on each, but a darker shaow on the middle element to make it appear as if it was standing out to the user. 
- Testimonials Section
    - The testimonials section was taken from MDBoostrap Design Blocks.  There are three (fictional) testimonails, from dogs, for the added fun and to give the landing page some character. 
    - Each tesimonial is split into 5 parts: 
        - Dogs Image 
        - Dogs Name
        - Dogs Job
        - Dogs Comment on Waggy Box
        - Dog star rating. 

