# Selenium Design Patterns Playground
## Install Instructions
* Clone the `selenium-design-patterns` repo:
```
git clone https://github.com/hamologist/selenium-design-patterns
```
* Install the `selenium-design-patterns` repo (from the `selenium-design-patterns` repo):
```
pip install -e .
```
## How to Run the Login Page
`python -m http.server`
## How to Run the Tests
* Traditional approach without design patterns
```
python selenium_design_patterns_playground/tests/without_design_patterns/test_login_page.py
```
* Using design patterns
```
python selenium_design_patterns_playground/tests/with_design_patterns/test_login_page.py
```