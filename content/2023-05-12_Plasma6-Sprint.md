+++
title = "Plasma 6 Sprint 2023"
slug="Plasma6-Sprint-2023"
draft = false
date = 2023-05-12
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++


# Plasma 6 Sprint

I was at the Plasma 6 sprint. It took place in Augsburg at [Tuxedo](https://www.tuxedocomputers.com/) office, a well-known german company selling computers that offers preinstalled with Gnu/Linux and KDE Plasma. They also are a KDE e.v (i.e foundation) sponsor. I will certainly consider their offers when buying hardware.
Their office were great and very nice people welcomed us.

It was great to get to work in person again with KDE community members, since I wasn't in person at last Akademy in Barcelona.

I am very happy to have met the new contributors that I hadn't met before.

Meetings and discussions were incredibly valuable and galvanizing.

## Plasma 6

After some detour building plasma 6, I am now using Plasma 6 Wayland.
It turns out only Qt 6.5.1 and 6.5.0 are compatible with Plasma 6, not even dev branch (6.6) are compatible with current plasma dev.

The stability is decent but it made a few issues glaring that we can take care of head-on, both visualy and with our development environment.
Qt6 is now 5 years and we never really used it, so a few paper cuts were to-be expected.

Still all in all, everything runs well enough.
Don't do that at home ;)

This relative stability won't last very long as important refactoring is taking place and has not yet reached our main branches.

It seems Qt dev branch currently (to be 6.6) should be preferable to use, because it is expected to be the version Plasma 6.0 will use and it can be contributed to contrary to Qt 6.5 that is in maintenance mode.
An important area for this is Wayland support.

Plasma 6 uses now [C++20](https://en.cppreference.com/w/cpp/20) which solves a few shortcomings.
I am especially happy about [ranges](https://en.cppreference.com/w/cpp/header/ranges) that is going to make let boiler-plate-y to loop over collections, and c++ modules.

## dolphin + kf6

As dolphin co-maintainer and a KIO framework contributor, I felt the need to have a Dolphin kf6 version to be able to test our work, this is now done.
I made a [kf6 branch](https://invent.kde.org/system/dolphin/-/tree/kf6) and it can be installed using [kdesrc-build6](https://nicolasfella.de/posts/building-plasma-against-qt6/) dolphin.
I took care first of [baloo-widgets](https://invent.kde.org/libraries/baloo-widgets/-/merge_requests/52) and then of [dolphin-plugins](https://invent.kde.org/sdk/dolphin-plugins/-/merge_requests/39) along the way.

[kio-extras](https://invent.kde.org/network/kio-extras/), the library that provides `recentlyused:/` protocol and thumbnail generators should soon have a kf6 branck too.

This work took me longer that I would have expected, having to learn the many ways CI tools and cmake can trick you.
Fortunately I had great people around to help me getting through it and iterate faster.
Thank you Nicolas and even more Alexander.

## Plasma contributions

Apart from that, I did some work improving plasma dependency declaration so that developers wouldn't miss important runtime dependencies and some warning fix.

I started my self-assigned task for Plasma 6, [the wallpaper Kcm in systemsettings](https://phabricator.kde.org/T12622).
Discussing with [Marco](https://notmart.org/blog/author/mart/) gave me the direction to follow it through.

I finished the work initiated by Jonathan Haney to fix [bug 348529](https://bugs.kde.org/show_bug.cgi?id=348529), that was his first contribution !

In plasma 6 when your screen is locked by default it will turn off the screen after 60 seconds by default.

A question I am asking myself is do we want backport to plasma 5.27 ?

Knowing that if we did, we wouldn't have the UI to change the 60 seconds threshold or turn off the feature, we'd have to edit by hand a tricky config file.
It is a high priority feature request that can be considered a bug as without this you might waste energy consumption.
And with Plasma 6 very far off this seems to me reasonable. 

Do you think that would be acceptable ?

I should be at [Akademy 2023](https://akademy.kde.org/2023/).
