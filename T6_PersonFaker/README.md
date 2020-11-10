# PersonFaker

This code could create unlimited quantity random personal files for RPG game. Each file forms contained original design, unical name, profession, skills and some other personal features.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
You need to copy file_operations.py in current directory.

### How to use

Then you run this code, you'l see in ```output\svg``` directory 10 .svg files with unical personal profiles.
If you need to create more than 10 profiles, you need to change range value in 49th line of the code:
```python
for i in range(10):
```

### Output results

As results you get 10 or more .svg files with unical personal profiles.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).