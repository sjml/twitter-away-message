# Twitter Away Message

I want to take an extended break from Twitter, but I have some friends who only
think to contact me there and might think I'm ignoring them. This resurrects the
old AIM away message concept for Twitter DMs. (Note, it only responds to DMs, not
regular Twitter mentions.)

You'll need credentials for a [Twitter Developer](https://developer.twitter.com/)
account. Once you have them, rename `credentials.json.base` to simply 
`credentials.json` and put them in there. 

Make sure to install all the listed Python requirements with 
`pip install -r requirements.txt`, then run `python away.py`.

You probably want to set this up as a cron job somewhere. Note that DMs can take
several minutes before they're available to the API, so you probably don't want this
to run more than every 10 minutes. (I've set it to go once per hour, just to be safe.)

Enjoy; use your powers only for good; etc. 

