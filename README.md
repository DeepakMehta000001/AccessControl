# AccessControl Simple App

## Files
1. **controller.py** contains the functions and core logic for Access Control 
2. **data.py** contains the initial data. 
3. **main.py** contains the menu driven logic and input facilitator. 
4. **test.py** contains the tests for Access Control

## Assumptions
1. There are only two kind of roles admin and user. However, we can add more if we add that to self.roles dictionary.
2. Admin has access to all the resources having access **Read, Write, Delete**.
3. User has access to **read only** resources.
4. There are only 3 kind of actions (file - access) READ, WRITE and DELETE.

## Steps to install and run

1. Clone the repository 
2. System should have python3 installed and added to the path. 
3. run main.py (python main.py)
