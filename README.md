# OnlySnarf

`pip3 install OnlySnarf`  
or  
`git clone git@github.com:skeetzo/onlysnarf && sudo python3 setup.py install`

## Description

OnlySnarf is a python based automation tool to assist with uploading content to OnlyFans. OnlySnarf is capable of downloading and uploading a file (image or video) or gallery of files (images) locally or from a Google Drive folder as specified by run time arguments to an OnlyFans account.

## Menu
[Menu](https://github.com/skeetzo/onlysnarf/blob/master/menu.md)

## Previews
![preview](https://github.com/skeetzo/onlysnarf/blob/master/images/preview.jpeg)
[Gallery](https://github.com/skeetzo/onlysnarf/blob/master/images/gallery.gif)
[Video](https://github.com/skeetzo/onlysnarf/blob/master/images/video.gif)
[Discount](https://github.com/skeetzo/onlysnarf/blob/master/images/discount-recent.gif)
[Message](https://github.com/skeetzo/onlysnarf/blob/master/images/message-recent-debug.gif)

## Scripts
First run:  
  * `(sudo) onlysnarf-config`
Then from within project's OnlySnarf directory either:  
  * `(sudo) onlysnarf [args]`
  * `(sudo) onlysnarfpy (-debug) -category image|gallery|video`
  * or directly via `python3 onlysnarf.py (-debug) -category image|gallery|video`

## args

-debug  
  `python3 onlysnarf.py -debug`  
Tests configuration. Does not upload or remove from Google Drive.

-category image  
  `python3 onlysnarf.py -category image`  
Uploads an image labeled: 'imageName - %d%m%y'  

-category gallery  
  `python3 onlysnarf.py -category gallery`  
Uploads a gallery labeled: 'folderName - %d%m%y'  

-category video  
  `python3 onlysnarf.py -category video`  
Uploads a video labeled: 'folderName - %d%m%y'  

-text  
  `python3 onlysnarf.py -category video -text "your mom"`  
Uploads a video labeled: 'your mom'  

-show
  `python3 onlysnarf.py -show`
Shows the Chromium browser

**more available in menu**

Or include a 'config.conf' file located at '/opt/onlysnarf/config.conf' to set variables at runtime without using arguments. An example file has been provided. Please be sure to follow the key:value pattern. A starting # denotes a comment.

## Authentication  
--------------
The use of this package requires configuring a Google App with *PyDrive* for access to your Google Drive. The Drive API requires OAuth2.0 for authentication.
###### from [Auth Quickstart](https://raw.githubusercontent.com/gsuitedevs/PyDrive/master/docs/quickstart.rst)
1. Go to `APIs Console`_ and make your own project.
2. Search for 'Google Drive API', select the entry, and click 'Enable'.
3. Select 'Credentials' from the left menu, click 'Create Credentials', select 'OAuth client ID'.
4. Now, the product name and consent screen need to be set -> click 'Configure consent screen' and follow the instructions. Once finished:

 a. Select 'Application type' to be *Web application*.
 b. Enter an appropriate name.
 c. Input *http://localhost:8080* for 'Authorized JavaScript origins'.
 d. Input *http://localhost:8080/* for 'Authorized redirect URIs'.
 e. Click 'Create'.

5. Click 'Download JSON' on the right side of Client ID to download **client_secret_<really long ID>.json**.

**Rename the file to "client_secrets.json" and place it into your installed OnlySnarf directory.**
To update your installation with the new file, run `onlysnarf-config`, select 'Update Google Creds', and enter the location of your "client_secret.json" file.

## Config
##### config.conf  
Path: /opt/onlysnarf/config.conf (previously /etc/onlysnarf/config.conf)
Create or update the "config.conf" file with the following values:
  * username -> the Twitter connected to your OnlyFans's username  
  * password -> the Twitter conencted to your OnlyFans's password  

###### Why Twitter credentials?
OnlyFans uses a captcha to prevent malicious bots from accessing user accounts. However, this captcha is only necessary when logging in with your OnlyFans username and password. Logging in with the provided Twitter authentication does not provide a captcha and thus allows a more accessible automated entrance.

##### google_creds.txt   
Generated by Google Drive's authentication process. Saves Google authentication for repeat access.

##### settings.yaml  
Used to facilitate Google Drive's python authentication. Requires generating an app w/ credentials via Google Console. Credentials are authenticated once and then saved to "google_creds.txt".

## Example Crons  

Upload a random image once a day at noon:  
  `* 12 * * * onlysnarfpy -category image`

Upload a random gallery of images every Wednesday at 2:30pm:  
  `30 14 * * 3 onlysnarfpy -category gallery`

Upload a random video every Friday in the month of June at 6:00pm:  
  `00 18 * 6 5 onlysnarfpy -category video`

Text will be generated if not provided with `-text`
  `* 12 * * * onlysnarfpy -category image -text "Your mother is a dirty whore"`

## Dependencies
  ### Google Chrome -> `sudo apt install -y google-chrome-beta`

## Referral
Feel free to make use of my referral code ;)  
https://onlyfans.com/?ref=409408