+++
title = "Dolphin at Akademy 2023"
slug="dolphin-at-akademy-2023"
draft = false
date = 2023-07-22
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++

I am returning from akademy and I had a great time, meeting new people or people I had already worked with online.

In particular I was very happy to meet Felix, my fellow dolphin co-maintainer.
We get along very well together, this will only make our dolphin work more pleasant and efficient.

# Dolphin

We had a [Bof](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force#Organization) about dolphin on Tuesday.

You can have a look at the [notes](https://invent.kde.org/system/dolphin/-/issues/45#note_720629) taken by Felix.
Unfortunately we didn't manage to have sufficient audio quality so that people online could properly participate.

Still with the amazing people present, we made some plans to improve dolphin search feature, the possibility of publishing dolphin on Windows Store and more.

I shared my interest in fixing [the most popular bugs, by votes or duplicate count](https://bugs.kde.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&columnlist=product%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cshort_desc%2Cchangeddate%2Cdupecount%2Cvotes%2Ckeywords&list_id=2409564&product=dolphin&query_format=advanced&resolution=---&resolution=FIXED&resolution=LATER&resolution=REMIND&resolution=DUPLICATE&resolution=WAITINGFORINFO&resolution=BACKTRACE&resolution=UNMAINTAINED).
Those are usually hard but very rewarding to fix.

A perfect area for interested people willing to contribute to dolphin, would be to help on our [setting redesign plans](https://invent.kde.org/system/dolphin/-/issues/36).
If you are interested, you can pick some part of the changes and try to implement them as I did in [this MR](https://invent.kde.org/system/dolphin/-/merge_requests/553) and join the [KDE file management channel](https://go.kde.org/matrix/#/#kde-fm:matrix.org) to get some help and advice.

With the current KDE goals being Accessibility, Sustainability and Automation, it has made apparent that the [selenium-appium-at-spy](https://invent.kde.org/sdk/selenium-webdriver-at-spi/) testing tool can greatly help dolphin in those three regards.
It allows to automate UI tests, by using the accessibility API present in applications (in Qt for instance). So for it to work we need dolphin to have good accessibility support. In turn this allows to automate test scenarios to measure energy consumption and ensure dolphin of its energy-efficiency.
The good news is that it is already in the pipe thanks to the work of [Marco](https://notmart.org/blog/).

Finally, Dolphin 23.08 is close to release, it will feature some bug fix and some small features:
 * when hiding hidden files dolphin will also hide files files whose name ends with "~", ".bak" or "%". Technically files having the "application/x-trash" mimetype. This is configurable by editing mime type either in file association kcm or using the utility command `keditfiletype application/x-trash`.
 * Double clicking on a tab will dupicate the tab.

# Akademy

This my fourth akademy, and my second in-person, it has been great.

Conferences were very nice, I learned many new things. The goals are making nice progress and getting traction.

I attended the qml-c++-integration training by Kevin Krammer of [KDAB](http://kdab.com/).
It was an occasion to complete my Qml+C++ knowlegde, now I have a better understanding of [attached properties](https://doc.qt.io/qt-6/qtqml-syntax-objectattributes.html#attached-properties-and-attached-signal-handlers). Kevin told us about use cases for qml without QtQuick, as a scripting language or a to build QWidget interfaces using [Declarative Widgets](https://www.kdab.com/declarative-widgets/) for instance.
I was reminded about KDAB's [KDToolbox](https://github.com/KDAB/KDToolBox/) a very nice collection of C++ utilities and learned about the nifty NotifyGuard that can help reduce boiler code for instance in KCM when writing c++ objects having many properties. Since it is MIT licensed, it is very easy to reuse.

Now it is time to finish my own planned work for Plasma 6 because it is coming !

Many thanks to every one who made the event possible, the local team, the akademy team, the sponsors and the donators to KDE e.v .
