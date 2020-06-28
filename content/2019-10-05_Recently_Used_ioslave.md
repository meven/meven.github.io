+++
title = "Recently Used ioslave"
slug="Recently-Used-ioslave"
draft = false
date = 2019-10-05
[taxonomies]
categories = [ "Monde libre" ]
tags = [ "kde" ]
+++
With [D7446](https://phabricator.kde.org/D7446) landing, the new ioslave recentlyused:/ ioslave will become user visible with KDE Frameworks 5.63.
This differential revision adds two entries "Recent Files" and "Recent Locations" to the place panel (in dolphin and open/save dialogs)

<img src="/captures/recently-used.png" alt="Recent screenshot" />

It leverages the ioslave recentlyused:/ introduced in [D22144](https://phabricator.kde.org/D22144), allowing to access KActivity data.
KActivity is the service that provides "recent" elements to kickoff menu and is activity aware as the name suggests.

So now "Recent Files", "Recent Locations" in the places panel share the same underlining data with kickoff.

But recentlyused:/ can be used to create your virtual folders for recent files or folders. For instance
* {{recentlyused:/files?type=video/*,audio/*}}
To filter recently accessed video and audio files.

* {{recentlyused:/files?path=/home/meven/kde/src/*&type=text/plain}}
To filter recently accessed text files in any subdirectory of /home/meven/kde/src/

* {{recentlyused:/locations?path=/home/meven/kde/src/*}}
To filter recently accessed folders in any subdirectory of /home/meven/kde/src/

You can read the [documentation](https://cgit.kde.org/kio-extras.git/tree/recentlyused/recentlyused.h#n28) for more details.

When working on this new feature, It was a great time to improve KActivity.
So I allowed KActivity to ingest data from gtk applications in [differential D23112](https://phabricator.kde.org/D23112).

I want to thank Ivan Lukić for building KActivity service and library and reviewing most of this work. 
And I want to thank all the other reviewers involved.