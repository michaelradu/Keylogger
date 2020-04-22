# A simple keylogger for Linux
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

[Website](https://michaelraduu.github.io/Keylogger/) - [Keylogger wiki](https://github.com/michaelraduu/Keylogger/wiki)


Welcome to the simple keylogger repo! A keylogger is a program that records your keystrokes, and this program saves them in a log file on your local computer.

Check out below to learn how to install them. This keylogger is simple and bare bones, however it works great! Feel free to fork and improve it if you want. Be sure to check out the [issues](https://github.com/michaelraduu/Keylogger/issues) or [pull requests](https://github.com/michaelraduu/Keylogger/pulls) to see if your problem has been fixed, or to help out others.

Currently, there is ony one keylogger program which works for Linux and possibly macOS. In the future I will update it so it works on all major platforms out there.

> Looking to make a fix or change on the website? You can find the website repo [here (https://michaelraduu.github.io/Keylogger/).

## Contents
- [Linux installation guide](#)
- [Check out the site for more information](https://michaelraduu.github.io/Keylogger/)

Or, view the `README.md` file in each programs folder for more up to date information.


## Linux
### Installation

First, install the required libraries:

`pip install pynput`


### How to run it?

To run it just cd into the directory and run: 
`python3 logger.pyw`

The keylogger is now running! It will log your strokes to the file named `key_log.txt`


---

### TO DO:

- Add an option to stop the keylogger with a combination of keys chosen by the user.

- Custom file path to use as a log file (default being current directory).

- Option to clean log file on startup.

- Option to email the files in which logged keys are stored.

- Encrypt logged file with a custom method and decryption key chosen by the user.

- Autorun on startup.

- Self destruction if the file with the logged keys is opened with the wrong decryption key or with no decryption key.

- New keylog file structure for easier reading.

- Make it a hidden proccess perhaps.

- Windows and macOS versions.

---

#### Uses

Some uses of a keylogger are:

- Business Administration: Monitor what employees are doing.
- School/Institutions: Track keystrokes and log banned words in a file.
- Personal Control and File Backup: Make sure no one is using your computer when you are away.
- Parental Control: Track what your children are doing.
- Self analysis

---

Feel free to contribute to fix any problems, or to submit an issue!

**Please note, this repo is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.**

Don't really understand licenses or tl;dr? Check out the [MIT license summary](https://tldrlegal.com/license/mit-license).

Distributed under the MIT license. See [LICENSE](https://github.com/michaelraduu/Keylogger/blob/master/LICENSE.txt) for more information.

Michael Radu – [Website](https://michaelradu.cf)

