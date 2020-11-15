+++
title = "Wayland Status for Plasma 5.20"
slug="Wayland-Status-Plasma-5.20"
draft = false
date = 2020-11-15
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++

The KDE community has made some great progress on Plasma Wayland support during this release cycle.
Some people on the Internet have qualified Plasma Wayland session as stable, but I wouldn't go that far yet.
I would qualify Plasma sessions as beta preview, we still have a long way to go.
In some configurations and workflow It might suit you but certainly not all users for now.

I am going to highlight a bit this progress below but first I'd like to explain the technical challenges the KDE Wayland community Goal faces.

# Why Wayland migration takes time

Wayland related issues have different origins.
Here are the main ones :

 * Missing wayland protocol or missing protocol implementation.<br />
 Wayland defines a way to exchange data between an application and the compositor (in Plasma that's KWin). Those exchanges are formalized with protocols. Wayland provides quite a few [standard ones](https://github.com/wayland-project/wayland-protocols). For instance we have a protocol for  when a GUI Application starts, it will ask the compositor some memory to draw its GUI in, and another for when the compositor gives the application the keyboard focus.
 And for each particular window interaction between applications and the compositor we need such a protocol.<br />
 Standard protocols are not enough to build a Plasma session upon, it is generic and is meant to be usable by desktop and embed all the same.
 So KWin and Plasma have [some specific protocols](https://invent.kde.org/libraries/plasma-wayland-protocols). Those, for instance, allow Plasma taskbar to manage other windows.<br />
 Despite Wayland is not anymore a new technology, its protocols mature slowly. Their definition takes time, they are validated through a review process, and are updated as needed. After that step, developers must implement their support in compositors, and sometimes also in applications or frameworks.<br />
 If you are interested on this subject, I can recommend again Drew DeVault's [the wayland book](https://wayland-book.com/).<br />
 Those are often the cause of missing features whether we a protocol does not exist yet or we lack an implementation. The task manager window thumbnails is in this category.

 * Fill the blank issues: the X.Org Display Server encompasses a lot of things, from keyboard input to screensavers, to screen management. And those features need to be reimplemented somehow whether it is through Wayland protocols or new completely new solutions. We have made good progress on this but a few missing cases remain.

 * Immaturity issues: Wayland implementations and related APIs are relatively young especially when you compare to X.Org Server. And on the desktop those implementation have not been used much, preventing issues to be discovered and fixed. Furthermore clients and compositors especially have a lot more responsibility compared to what they had with X, meaning a lot of new code is written, and new code means less stability.
 With [X.org display server now abandonware](https://www.phoronix.com/scan.php?page=news_item&px=Ajax-On-The-X-Server), this should help motivate more users and developers to test and stabilise things.
 Those cause crashes, misbehaviour or feature missing.
 
 * Compatibility issues: Wayland is very different to what we had in X. And we need to adapt to this new paradigm in a lot of places. For instance in plasma, with Xorg the taskbar could simply access Xorg API and manage windows directly. Now it must ask the Compositor to use its Window management API and this is a different API and KWin is the one defining and implementing it. One way to mitigate those issues, is to have a proxy. we try to maintain compatibility with X applications through XWayland notably.

And some issues can be caused by several of those subjective origins.

# Major Plasma 5.20 Wayland improvements

 * The Task Manager has now window thumbnails Wayland. (Aleix Pol Gonzalez) [merge request](https://invent.kde.org/plasma/plasma-desktop/-/merge_requests/36/)

 * Screen recording and screencasting now works on Wayland for compatible applications (e.g. OBS Studio and more to come) (Aleix Pol Gonzalez)
 [merge request](https://invent.kde.org/libraries/plasma-wayland-protocols/-/merge_requests/1)
 <br /> That's a fill the blank issue and missing protocol issue : Xorg allows any program to record the screen with its own API. We needed a new protocol to expose a screencasting feature.  

 * Klipper now uses the Wayland clipboard and works as you would expect in a Wayland session (David Edmundson)
 [merge request](https://invent.kde.org/plasma/plasma-workspace/-/merge_requests/1)

 * Implemented the Wayland input-method-unstable-v1 protocol, which opens the door for proper virtual keyboard support on Plasma Mobile, among other benefits! (Aleix Pol Gonzalez)
 [merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/106)

# Bug fixes

## Stability improvement

 * In a Plasma Wayland session, XWayland no longer brings down the whole session when it crashes; it just restarts normally (Vlad Zahorodniy, Plasma 5.20) [merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/125)

 * Clearing the clipboard history on Wayland no longer crashes Plasma (David Edmundson, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=396308)

 * On Wayland, clicking on a Task Manager entry while that entry’s tooltip is visible no longer crashes Plasma (Vlad Zahorodnii, Plasma 5.20)
[bug](hhttps://bugs.kde.org/show_bug.cgi?id=425869)

 * KWin no longer sometimes crashes when exiting or re-launching (Vlad Zahorodnii, Plasma 5.20) [merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/328)

## Feature Parity

 * On Wayland, context menus on the desktop and throughout Plasma now close when they’re supposed to (Vlad Zahorodnii, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=379635)

 * On Wayland, Task Manager tooltip window thumbnails are no longer overlapped by the app’s icon (Nate Graham, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=427076)

 * On Wayland, pressing Ctrl+Alt+Esc twice no longer results in the “Click a window to kill it” message being re-positioned into the top-left corner of the screen (Vlad Zahorodnii, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=400675)

 * KRunner is now more responsive to typed text on Wayland (Alexander Lohnau, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=426746)

 * Fixed the initialization of dmabuf textures in KWin on Wayland, which in practical terms should ensure that videos played Firefox no longer sometimes display garbage instead of the video (Vlad Zahorodnii, Plasma 5.20)
[merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/323)

 * Clicking on a Task Manager thumbnail now activates that window, as you would expect (Marco Martin, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=426925)

 * the window stacking order is now always correct (Vlad Zahorodnii, Plasma 5.20)
[merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/288)

 * context menus now always have shadows, as expected (Vlad Zahorodnii, Plasma 5.20)
[merge request](https://invent.kde.org/plasma/kwayland-integration/-/merge_requests/3)

* Improved the graphics performance on Wayland (Gang Wu, Plasma 5.20) by allowing KWin not to draw windows placed behind opaque others.
[merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/228)

* It’s now possible to drag windows on Wayland from their empty areas, just like on X11 (Vlad Zahorodnii, Plasma 5.20)
[merge request](https://invent.kde.org/plasma/breeze/-/merge_requests/8)

* Plasma no longer sometimes crashes when you hover the cursor over an auto-hide Panel (Andreas Haratzis, Plasma 5.20)
[merge request](https://invent.kde.org/plasma/kwin/-/merge_requests/83)

* Fixed a case where KWin could crash when logging out of a Wayland session (Andrey Butirsky, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=420077)

* Edge swipe gestures and showing a hidden panel by tapping the screen edge now work on Wayland (Xaver Hugl, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=421212)
[bug](https://bugs.kde.org/show_bug.cgi?id=423842)

* The System Settings Accessibility page is now available (Michael Weghorn, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=414546)

* Fixed the “Windows can cover” panel setting on Wayland (Xaver Hugl, Plasma 5.20)
[merge request](https://invent.kde.org/plasma/kwayland-server/-/merge_requests/60)

* The last-used keyboard layout is now remembered on Wayland (Andrey Butirsky, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=412101)

* Fixed a crash on Wayland when waking up the computer while multiple screens are attached (Andreas Haratzis, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=422460)

* you can now enter full screen mode in MPV by double-clicking on the video (Benjamin Port, Plasma 5.20.0)
[bug](https://bugs.kde.org/show_bug.cgi?id=421232)

* Previews for cursor themes now correctly display real-time previews as you hover your cursor over them on Wayland (David Redondo, Plasma 5.20)
[bug](https://bugs.kde.org/show_bug.cgi?id=424048)

* Spectacle now lets you take a screenshot on Wayland without needing to click first to confirm it (Méven Car, Spectacle 20.12)
[merge request](https://invent.kde.org/graphics/spectacle/-/merge_requests/13)

Special shoutout to our newest ambitious and prolific KWin contributor Xaver Hugl.

Thanks to [Nate blog](https://pointieststick.com/) that makes putting this together so much easier.

We are on [telegram](https://t.me/waylandkdegoal) and IRC *#kde-wayland-goal* on freenode.
More on the community wiki [Wayland Goal](https://community.kde.org/Goals/Wayland).
