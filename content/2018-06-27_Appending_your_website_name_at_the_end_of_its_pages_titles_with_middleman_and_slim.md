+++
title = "Appending your website name at the end of its pages titles with middleman and slim"
slug="Appending-your-website-name-at-the-end-of-its-pages-title-with-middleman-and-slim"
draft = false
date = 2018-06-27
[taxonomies]
categories = [ "Monde libre" ]
tags = [  ]
+++
If you use [middleman](https://github.com/middleman/middleman)  and the nice template solution [slim](https://github.com/slim-template/slim) you might encounter the same need as I did: appending your site name at the end of your page titles without hardcoding it everywhere.

I found a simple solution, in my layout I added:
```
    - if current_page.data.title?
        title= current_page.data.title + " | My Website"
    - else
        title My Website
```

When in your slim pages you have :
```
---
title: My page title
---

```

You end up in your generated code using [middleman](https://github.com/middleman/middleman) with the title
```
<title>My page title | My Website</title>
```

And if the page has no title it will default to :
```
<title>My Website</title>
```

This was found when trying to [improve diesel documentation](https://github.com/sgrif/diesel.rs-website/pull/65).

I hope this can be useful to somebody else.