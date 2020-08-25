# Mail sender

This code helps to send mails automatically

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to use

To start use this code, you need to input yours datas for the next variables: ```my_mail, friend_mail,
subject_mail```. Check the example below:

```python
my_mail = 'From: alex.balakin52@gmail.com'
friend_mail = 'To: alex.balakin52@gmail.com'
subject_mail = 'Subject: Invite'
```
In fact, this variables means the headers of your's mail.

The next step is to fill the mail text template, which consider in the ```mail_text``` variable. For example like this:
```python
mail_text = '''\n\n Hello, %friend_name%! %my_name% invite you on site %website%!

%website% — is the new release of our online Python web developer course. 
Practice in Python and many other things. Solve the real developers tasks. Got the detail review from masters.
```
```%friend_name%, %my_name%, %website%``` is the templates which you need to change in variables below.

Also, you need to create tne ```.env``` file in current directory whith running code.
In the ```.env``` you need detect the login and password of mail sender account in accordance to next template:
```.env
LOGIN=LOGNAME
PASSWORD=1234
```
## Warning!

If your mail sender account not on the ```gmail.com``` host - you need change ```SMTP_SSL``` in 39th line of the code.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
