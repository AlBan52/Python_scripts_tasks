# PersonFaker

This code could create unlimited quantity random personal files for RPG game. Each file forms contained original design, unical name, profession, skills and some other personal features.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
You need to copy ```file_operations.py``` in current directory. This file is the local library for the ```person_faker.py```

### How to use

Previosly you have two ```.py``` files in your working directory: ```file_operations.py, person_faker.py ```
For getting results, you have to run the ```person_faker.py``` code.
Befor you run this code, you need to change the next variables values:
```python
person_amount = 10
min_ability_value = 8
max_ability_value = 14
```
This variables could have different values, as you need.

For this case 10 ```.svg``` files with unical personal profiles in ```output\svg``` directory will be created.

### Output results

As results you get 10 or more ```.svg``` files with unical personal profiles.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).