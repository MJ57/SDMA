## Thibaud's code for scraping tweet from Twitter

import twint

# Configure
c = twint.Config()
c.Username = "now"
c.Search = "fruit"

# Run
twint.run.Search(c)
