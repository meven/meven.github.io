+++
title = "Wayland Status update for Plasma 5.19"
slug="Wayland-Status-update-Plasma-5.19"
draft = false
date = 2020-06-02
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++
We have been busy recently on the Wayland Goal.

A few of those points were already highlight on [Nate's excellent blog](https://pointieststick.com/).
But some were missing, and I wanted to highlight those dedicated to Wayland with more context.

The changes I mention here will be present in Plasma 5.19, but they are not exhaustive.

#### KWin and architecture changes

Thanks to Aleix Pol, KWin Wayland in Plasma 5.19 now has [Wayland tablet protocol](https://github.com/wayland-project/wayland-protocols/blob/master/unstable/tablet/tablet-unstable-v2.xml ) support meaning we have tablet touch and pen pressure. [Kwin patch](https://phabricator.kde.org/D26859) and [KWayland patch](https://phabricator.kde.org/D26858)

Vlad improved [subsurface clipping](https://bugs.kde.org/show_bug.cgi?id=387313), it means the compositor can do less work and better figure out what to paint and not to paint.
It is most visible for applications like Firefox that uses a lot of Wayland surfaces. [D29131](https://phabricator.kde.org/D29131) [kwin!5](https://invent.kde.org/plasma/kwin/-/merge_requests/5)

With [D29250](https://phabricator.kde.org/D29250) the resizing of XWayland windows has become less resource demanding and matches X experience.
This still needs next version of XWayland 1.21 to work though.

And KWin has had more changes under the surface.

The [KWayland library](https://invent.kde.org/frameworks/kwayland) has been split library into two libraries.
One KWayland contains the regular @@KWayland::Client@@ stuff but the new [kwayland-server](https://invent.kde.org/plasma/kwayland-server) contains now the @@KWayland::Server@@ part.

Because @@KWayland@@ is part of [KDE frameworks](https://kde.org/products/frameworks/) it is released monthly, independently of Plasma releases, and we have to care about not breaking the API when making changes.
But on the other hand @@KWayland::Server@@ is only ever used by KWin, so it added some churn to the development of @@KWayland::Server@@ which was not needed.
Now @@KWayland-server@@ will have a Plasma release cycle same as KWin, and will simplify our workflow evolving our Wayland compositor implementation.
New depot is at [https://invent.kde.org/plasma/kwayland-server](https://invent.kde.org/plasma/kwayland-server).

#### Plasma

The global application menu has is now working in Wayland thanks to Carson Black patch serie: [D27464](https://phabricator.kde.org/D27464), [D28168](https://phabricator.kde.org/D28168), [D28150](https://phabricator.kde.org/D28150), [D28112](https://phabricator.kde.org/D28112), [D27959](https://phabricator.kde.org/D27959),
[D27818](https://phabricator.kde.org/D27818) and [D28146](https://phabricator.kde.org/D28146), [bug](https://bugs.kde.org/show_bug.cgi?id=385880).
This is typical Wayland work : make new APIs because old ones were X specific or could not work with Wayland, add some wiring code and then use the new one in programs using.
This most often end up in better code architecture, better decoupled. 

The task manager can now bring forward multiple windows of the same program and remembering in which order they are stacked together
[bug](https://bugs.kde.org/show_bug.cgi?id=370258) [patch 1](https://phabricator.kde.org/D29054) [patch 2](https://phabricator.kde.org/D29054) [patch 3](https://phabricator.kde.org/D29055) and [patch 4](https://phabricator.kde.org/D29056).

KRunner is [better positioned](https://phabricator.kde.org/D27458).

Kscreen Osd are now usable, allowing you to to setup a newly connected screen and identify your plugged-in screen [bug](https://bugs.kde.org/show_bug.cgi?id=385672) [D28817](https://phabricator.kde.org/D28817)[D28818](https://phabricator.kde.org/D28818) [D28916](https://phabricator.kde.org/D28916)

#### Bugfixes

Quite a few crash KWin were resolved :[D28668](https://phabricator.kde.org/D28668) [D28858](https://phabricator.kde.org/D28858)  [D28889](https://phabricator.kde.org/D28889) [D27536](https://phabricator.kde.org/D27536) [kwin!9](https://invent.kde.org/plasma/kwin/-/merge_requests/9) [kwin!8](https://invent.kde.org/plasma/kwin/-/merge_requests/8)

And drkonqi got a couple fix : [D28692](https://phabricator.kde.org/D28692) [D28832](https://phabricator.kde.org/D28832).

### Plasma Wayland specific features

<a href="/captures/scroll-speed.png" title=""><img src="/captures/scroll-speed.png" /></a>

Thanks to the way Wayland is architectured, we can add features than are impossible with X server.
For instance in plasma 5.19 in Wayland you will be able to setup a scrolling speed for mice and touchpads. [D28331](https://phabricator.kde.org/D28331) [D28310](https://phabricator.kde.org/D28310)

__But our journey is far from over.__

[Our goal](https://community.kde.org/Goals/Wayland) is in part to make Plasma run in Wayland by default allowing pixel perfection, real security in the display server, better performance and  overall better architecture.

The road is still long to reach feature parity with the venerable X based sessions.
So we need as much people to help whether it is for testing, hacking code or reporting bugs.

There is a Plasma virtual Sprint starting right now spawning two weeks, where a lot of people involved in the Goal will participate.
I invite you to join-in : [Plasma virtual sprint 2020](https://community.kde.org/Sprints/Plasma/2020Virtual).

Also Drew DeVault released a great book about Wayland you can read at [https://wayland-book.com/](https://wayland-book.com/) to better understand Wayland inner-workings.