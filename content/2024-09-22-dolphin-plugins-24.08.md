+++
title = "Dolphin plugins 24.08"
slug="dolphin-plugins-24.08"
draft = false
date = "2024-09-22 14:00:00"
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++

Since dolphin-plugins 24.05, you can `git clone` from dolphin with dolphin-plugins git plugin.

Once the plugins are installed and `Git` is enabled in the context menu settings, you have this context menu action available:

<img src="/captures/git-clone-context-menu.png" width="100%"/>

And this shows this git clone dialog (with my french locale):

<img src="/captures/git-clone-dialog.png" width="100%"/>

You can paste a git repository url and it will fetch its branches.
If you happen to have a url in your clipboard or a `git clone` command line, it will directly extract it as the repository url.

This was [spearheaded](https://invent.kde.org/sdk/dolphin-plugins/-/merge_requests/58) by Nikolai Krasheninnikov, thanks.
I participated a bit as well and reviewed it.

There is still opportunity to improve the git implementation, like having a better commit dialog.
That would be a nice and simple new contributor opportunity :)
