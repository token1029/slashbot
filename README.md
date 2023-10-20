# :money_with_wings: SlashBot
<hr>
<p align="center">
<a><img width=500 
  src="/docs/workflows/banner.jpg" alt="Expense tracking made easy!"></a>
</p>
<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/github/languages/top/secheaper/slashbot?color=red&label=Python&logo=Python&logoColor=yellow)
![GitHub contributors](https://img.shields.io/github/contributors/secheaper/slashbot)
[![DOI](https://zenodo.org/badge/431190543.svg)](https://zenodo.org/badge/latestdoi/431190543)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
[![codecov](https://codecov.io/gh/secheaper/slashbot/branch/main/graph/badge.svg?token=YCKWZTHO7O)](https://codecov.io/gh/secheaper/slashbot)
[![Actions Status](https://github.com/mtkumar123/MyDollarBot/workflows/CI/badge.svg)](https://github.com/mtkumar123/MyDollarBot/actions)
![github workflow](https://github.com/mtkumar123/MyDollarBot/actions/workflows/black.yml/badge.svg)
![Discord](https://img.shields.io/discord/879343473940107264?color=blueviolet&label=Discord%20Discussion%20Chat)
![Lines of code](https://img.shields.io/tokei/lines/github/secheaper/slashbot?color=9cf)
![Version](https://img.shields.io/github/v/release/secheaper/slashbot?color=ff69b4&label=Version)
![GitHub issues](https://img.shields.io/github/issues-raw/secheaper/slashbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/secheaper/slashbot)

<hr>

## Demo Video

https://www.youtube.com/watch?v=uIHnW8YmrsU

## About SlashBot

SlashBot is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle.  
With simple commands, this bot allows you to:
- Add/Record a new spending
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to
- Download your expenditure history in the CSV format
- Visualize your spendings in the form of graphs/pie chart using the /chart option
- Email the history CSV file to yourself
- See the total daily/monthly expenditure in different currencies
- Add/Delete members
- Displays members
- split bills across different
- email splited bill to members involved
- display splited bill
- delete bills splited

Check out the bot here: https://t.me/ncsuBot

---
Sample demos are shown below. They are run on a local machine.

- [:information_desk_person: Sample Demos](#information_desk_person-Sample-Demos)


---

# :star: Whats New

### Release Version 1.3.1

- Split a bill acrross different members using the /splitBill command
- Email the bill splited to members involved using the /emailBill command
- Display the bill history using the /viewSplitBill
- Delete the bill by choosing the name of the bill by using /deleteBill
- Details for testing requirements added in README.md
- Add more test cases


### Release Version 1.3.0

- Add members using /addMember
- Delete the member by choosing the name of the memebr by using /memberDelete
- Display the members list by using the /memberList
- Add more documentaions for the functions




<!-- [comment]: <> (## Demo) -->

<!-- [comment]: <> (https://user-images.githubusercontent.com/15325746/135395315-e234dc5e-d891-470a-b3f4-04aa1d11ed45.mp4) -->



# :rocket: Installation Guide

## 💻For developers 
1. Install Python, atleast Python3

2. Clone this repository to your local system at a suitable directory/location of your choice

3. Start a terminal session, and navigate to the directory where the repo has been cloned

4. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt
```
5. Download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/

6. Once you login to your Telegram account, search for "BotFather" in Telegram. Click on "Start" --> enter the following command:
```
  /newbot
```
7. Follow the instructions on screen and choose a name for your bot. Post this, select a username for your bot that ends with "bot" (as per the instructions on your Telegram screen)

8. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy this token for future use.

9. Search for "Edit the system environment variables" on your local computer. Click on Environment Variables and create a new System Variable called "API_TOKEN" and paste the token copied in step 8.

10. In the Telegram app, search for your newly created bot by entering the username and open the same. Once this is done, go back to the terminal session. 
Make sure you export the PYTHONPATH variable to the main project folder
 ```
 python src/bot.py
```
11. A successful run will generate a message on your terminal that says "TeleBot: Started polling." 
12. Post this, navigate to your bot on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

For more info on deployment(Heroku), check out the doc [here](https://github.com/mtkumar123/MyDollarBot/blob/main/CONTRIBUTING.md#more-tips-for-developers)


## 💻For testing with Pytest
1. Some modules in testing require CHAT_ID environment variable to be set.
2. This is the specific ID that is maintained for your chat with the Bot.
3. While running the bot.py , get this id from line 72 and set it in your system environment variables.
4. This should ensure effective running of all tests.


# :information_desk_person: Sample Demos

  ### Add member

<p align="center"><img width="700" src="https://github.com/token1029/slashbot/blob/main/docs/workflows/addmember.png"></p>

1. Enter the `/addMember` command
2. Enter the new new member name
3. Enter the member email address


### Delete member

<p align="center"><img width="700" src="./docs/workflows/add.gif"></p>

1. Enter the `/memberDelete` command
2. Chose the name of the member

### View memberList

<p align="center"><img width="700" src="./docs/workflows/delete.gif"></p>

1. Enter the `/memberList` command

### Split a bill

<p align="center"><img width="700" src="./docs/workflows/csv_vis.gif"></p>


1. Enter the `/splitBill` command
2. Enter name of the bill
3. Enter amount of the bill
4. Chose Creditor
5. Chose Debtors

### View the splited bill

<p align="center"><img width="700" src="./docs/workflows/download.gif"></p>

1. Enter the `/viewSplitBill` command

### Email the splited bill

<p align="center"><img width="700" src="./docs/workflows/currencyWorking.gif"></p>

1. Enter the `/emailBill` command


### Delete a splited bill

<p align="center"><img width="700" src="./docs/workflows/multipleVisualizations.gif"></p>

1. Enter the `/deleteBill` command
2. Chose the name of the bill to delete

### Cleara Bill history

I want to send myself an email for the monthly expenditure


<p align="center"><img width="700" src="./docs/workflows/email.gif"></p>

1. Enter the `/clearBill›` command



:heart: Acknowledgements
---
We would like to thank Dr. Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project.


:page_facing_up: License
---
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/secheaper/slashbot/blob/main/LICENSE) for more details.


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="https://github.com/WeizhiGao"><img src="https://avatars.githubusercontent.com/u/57804858?v=4" width="75px;" alt=""/><br /><sub><b>Weizhi Gao</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Itaru-Shin"><img src="https://avatars.githubusercontent.com/u/143905092?v=4" width="75px;" alt=""/><br /><sub><b>Fucheng Guo</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/KingBanshou"><img src="https://avatars.githubusercontent.com/u/143905049?v=4" width="75px;" alt=""/><br /><sub><b>Zikang Wang</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/token1029"><img src="https://avatars.githubusercontent.com/u/38797209?v=4" width="75px;" alt=""/><br /><sub><b>Dongming Wu</b></sub></a></td>
  </tr>
</table>



# :calling: Support

For any support, email us at wdming1029@gmail.com
