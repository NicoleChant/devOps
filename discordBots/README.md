# Discord Bots

### Step I : Create a Discord Server

### Step II : Create a Discord Bot Account

First we need to navigate to the discord developer portal.

Let's click to the New Application button and give a name to our application.

We can add an image icon and a description to our application.

Let's go to Bot tab and click <span style="color:blue"> Add Bot </span>.

A wild bot has appeared!

Now the bot has been created!

Let's copy the bot token (our bots password DO NOT SHARE!)

Lets add it as an environment variable:

```
echo 'export botToken="<your bot token>"' >> ~/.zshrc
```

Now we have to invite our bot to our server.

Lets create an invite URL.

Lets go to OAuth2 -> URL Generator -> Click bot

Permissions Section

After selecting the appropriate permissions lets copy the generateed URL and open it in a new tab.
