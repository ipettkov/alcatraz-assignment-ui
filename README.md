# Test Automation Demo Project
The project contains (so far) following CRUD related tests:

- user create, search, delete
- data driven tests for date and names input fields
- validation of delete, edit and details page

# Project features
- project has implemented logger in each step of test case
- framework follows page object patter
- currently it is set up for execution with chrome and firefox
- added config.json file from which you can change browers and tweak few other things, 
- framework is set up so that you can add up on configs which will be pulled from that file

# Project framework structure
- [locators](locators) all element locators are grouped in classes in locators module

- [pages](pages) created page classes in which methods for each step are stored (POM), common methods are stored in [BasePage](base) class
some helper functions are in functions.py module in utility package as well as files responsible for
configuration(driver_factory.py)
- [tests](tests) there are set of tests for main functionality of the page
- [utils](utils) Helper functions are in functions.py module in utility package as well as files responsible for
configuration(driver_factory.py)
- [reports]() Integrated Allure framework for reporting, reports will be saved in specified folder from command line in project root

# Instructions on how to run project
After you clone the project you need to install requirements by executing the following commnad
    
    $ pip install -r requirements.txt

You can simply execute all tets by running
    
    $ pytest 
or
    
    $ python3 -m pytest
To run tests and generate allure reports use the following command

    $ python3 -m pytest --alluredir=<dir>
After that in order to generate reports you need to run

    $ allure serve <dir you specified above>
This will generate and html in your browser with the reports
Screenshots on failed test will be included on tearDown
Keep in mind you should have allure installed on your machine

    sudo apt-add-repository ppa:qameta/allure for linux
    brew install allure for macOS
