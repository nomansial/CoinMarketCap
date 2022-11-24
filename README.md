**Steps to setup and execute automation test cases**

1. Install python on your machine
2. Install Pycharm on your machine
3. Open Pycharm and Select option Get From VCS option
4. Enter repository URL and clone project
5. Setup Python interpreter
6. Install following requirements
    - Behave
    - assertpy
    - requestes
    - json
    
7. Open Pycharm Terminal
8. Make sure terminal is pointing to project directory
9. Run command behave features/retrieve_ID.feature --no-capture --tags=Test

On executing above command it will execute all the scenarios from retreive_ID.feature file. Please note steps are implemented in stepimp.py file.
   