# HashThemAll_Bot

#### Discord-Bot that calculates hashes from a text

- Written with Python 3.8
- Runs well under Linux; not tested on Windows/MacOS



# Installation

1.)  Clone the repository:

```bash
git clone https://github.com/DevEmperor/HashThemAll_Bot.git
```



2.)  Fix missing dependencies

   ```bash
cd HashThemAll_Bot && pip3 install -r requirements.txt
   ```

   

3.)  Tell the bot your channel's name, where he should listen on and your application-token by editing "*main.py*"

```python
channel_name = 'my_hashthemall_bot'  # ENTER THE CHANNEL'S NAME HERE, ON WHICH THE BOT SHOULD LISTEN
token = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg'  # ENTER YOUR APPLICATION-TOKEN HERE
```



4.)  Run the Bot:

```bash
python3 main.py
```



# Usage

After running the bot and adding it to your server ([Discord-Developer-Portal](https://discord.com/developers/applications)) you have to create a channel on your server that matches the name that you declared in "*main.py*". I also suggest to **enable the slow-mode in the channel's settings (10 sec.)** and **disable the welcome-message in the server-settings**, so that your backend doesn't get flooded.

After this is done, you can simply type a message in the channel you set and after a few seconds you'll get a direct-message with all calculated hashes.



# License

HashThemAll_Bot is under the terms of the [Apapche 2.0 license](https://www.apache.org/licenses/LICENSE-2.0), following all clarifications stated in the [license file](https://raw.githubusercontent.com/DevEmperor/HashThemAll_Bot/master/LICENSE).