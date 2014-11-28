## Design notes

This is an indieweb **static site generator**. It's designed to be used for an entire domain, including making an 'index page' with a user-specified order.


### Plugins

Thinking this will eventually have various input and output plugins. Here's what I am writing for my needs and *others I might add in italics*:

* master input: yml file that will become the index page and drive creation of subsidiary pages
* input: page (photos) from Smugmug
* output: pretty photo page (simple, responsive, with a 'picture popup')
* output: user-defined index page
* publish: post to S3. *Selectively re-upload pages, assets, etc.*
* *output: use (https://github.com/aFarkas/lazysizes)*



## Manifesto

I'm absolutely using [Common Markdown](http://commonmark.org/) (aka Standard Markdown or Common Mark), Gruber be damned.

I'm writing this in Python. It's unsexy now but has enough OO and 
