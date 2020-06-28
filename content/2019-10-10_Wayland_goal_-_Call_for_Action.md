+++
title = "Wayland goal - Call for Action"
slug="Wayland-goal"
draft = false
date = 2019-10-10
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++
KDE community has [elected](https://phabricator.kde.org/T11081) to finalize the transition to Wayland and embrace the future of desktop.

This entails making Plasma running smoothly under Wayland, but also making sure KDE Apps can run without bugs and missing features.
It also means that we want to help the wider Wayland community to fill missing features and fix bugs.

I call App users and developers to try out their favorite app in Wayland and report the issue that may arise. and add wayland as keyword to the bug to keep track on those bugs.

And you don't need a wayland session to test an app, you can do it in wayland within a X session !

> kwin_wayland # start an embed kwind_wayland
>
> # In another terminal
>
> gwenview --platform wayland # starts gwenview in the wayland session

<a href="/captures/gwenview_in_wayland_in_X.png" title=""><img src="/captures/gwenview_in_wayland_in_X.png" /></a>

We have a page listing [how to fix a few pitfalls](https://community.kde.org/Guidelines_and_HOWTOs/Wayland_Porting_Notes) that applications may have in Wayland.

You can also test Plasma Wayland session of course and report the same way issues that may arise.

You can reach us at #kde-devel or #plasma in [webchat.kde.org](https://webchat.kde.org) or freenode.

More information on the [Wayland Goal page](https://community.kde.org/Goals/Wayland)