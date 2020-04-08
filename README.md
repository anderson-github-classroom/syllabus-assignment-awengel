# CSC 448 Template Lab

## Dependencies
This class relies on the following packages being installed.
* Anaconda Python 3.7
* JupyterLab. I'm going to assume you are using this as your primary tool for this class. All videos will reference and assume this to be the case unless otherwise specified. 
* jupytext (installed via ``pip install jupytext``). After you install this, make sure you restart you jupyterlab environment.

## Instructions
This is a blank repo containing information about working on and submitting your labs and assignments.

* The lab assignments are located in https://github.com/anderson-github-classroom/csc-448-student
* You will only need to clone csc-448-student repo once. Each week (or more frequent) you can issue a ``git pull`` and receive updated information.
* You should not make changes inside csc-448-student. It should be viewed as read only; however, if you do make changes, please copy/save them manually and then issue a ``git stash`` before trying ``git pull``.
* To work on your lab, click on the link in the schedule, accept the GitHub assignment which will create you an individual repo. It is in this individual repo where you will copy the lab assignment from csc-448-student. 
* When you are done with the lab (or whenever you want), add your changes, commit your changes, and push your changes.

## Testing your code locally
* Install dependencies
    * ``pip install pytest``
    * ``pip install joblib``
    * ``pip install matplotlib``
* Issue the following command once on your system:
    * ``git clone https://github.com/anderson-github-classroom/csc-448-student ../csc-448-student``
* Issue this command everytime you want to test. It will try to automatically detect what assignment you are working on.
    *  ./run_tests_locally.sh or python run_tests_locally.py
* You can always try to test specific questions using:
    * pytest ../csc-448-student/tests/test_Syllabus.py::test_question_1