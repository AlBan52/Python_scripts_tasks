# Avatar Creator

This code helps you to prepear your avatar image file for any web service or social network.
Also it makes original visual effect on your photo. 

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to use

To start use this code, you need to load your previos photo to the codes rooth directory.
You must change the name of your previos photo in the 3rd string of the code:
```python
3    image = Image.open("monro.jpg")
```
### Output results

As results you get two files named as:
```new_image.jpg``` - full sized image under special visual effect;
```avatar.jpg``` - your's prepeared picture as avatar

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).