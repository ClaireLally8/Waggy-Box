<h1 align=center><strong>Waggy Box - Testing Information</strong></h1>

[Main README.md file](README.md)

[Deployed Site](https://waggy-box.herokuapp.com/)

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
    - `autopep8 --in-place --aggressive --aggressive app.py`