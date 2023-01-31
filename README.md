# Side Bar Enhancements
[![Latest Release](https://img.shields.io/github/tag/CodeByZach/sublime_side_bar_enhancements.svg?label=version)](https://github.com/CodeByZach/sublime_side_bar_enhancements/releases)

## Description

Provides enhancements to the operations on Side Bar of Files and Folders for [Sublime Text](https://www.sublimetext.com).

Notably provides delete as "move to trash", open with.. and a clipboard.

Close, move, open and restore buffers affected by a rename/move command. (even on folders)

New file/folder, edit, open/run, reveal, find in selected/parent/project, cut, copy, paste, paste in parent, rename, move, delete, refresh....

Copy paths as URIs, URLs, content as UTF8, content as <data:uri> base64 ( nice for embedding into CSS! ), copy as tags img/a/script/style, duplicate

Preference to control if a buffer should be closed when affected by a deletion operation.

Allows to display "file modified date" and "file size" on statusbar (may be a bit buggy).

To get rid of the stock ST menuitems create two empty files on "Preferences -> Browse Packages"

- `Default/Side Bar Mount Point.sublime-menu`
- `Default/Side Bar.sublime-menu`

## Installation

Download or clone the contents of this repository to a folder named exactly as the package name into the Packages/ folder of ST.

Troubleshooting Installation:

- First please note this package only adds a context menu to the "Folders" section and not to the "Open Files" section.
- Open the package folder. Main menu -\> Preferences -\> Browse Packages.
- Close Sublime Text.
- Remove the folder "Packages/SideBarEnhancements"
- Remove the folder "User/SideBarEnhancements"
- Navigate one folder up, to "Installed Packages/", check for any instance of SideBarEnhancements and remove it.
- Open ST, with Package Control go to : Remove Package, check for any instance of SideBarEnhancements and remove it.
- Restart ST
- Open ST, check if there is any entry about SideBarEnhancements in Package Control(in sections: "Remove Package" and just in case in "Enable Package")
- Repeat until you find there no entry about SideBarEnhancements
- Restart ST
- Install it.
- It works

## F12 key

(Please note that from version 2.122104 this package no longer provides the key, you need to manually add it to your sublime-keymap file (see next section))

F12 key allows you to open the current file in browser.

`url_testing` allows you to set the url of your local server, opened via F12

`url_production` allows you to set the url of your production server, opened via ALT+F12

### With absolute paths

- Right click any file on the Side Bar and select: "Project -\> Edit Projects Preview URLs"
- Edit this file, and add your paths and URLs with the following structure:

<!-- -->
    {
        "S:/www/domain.tld":{
            "url_testing":"http://testing",
            "url_production":"http://domain.tld"
        },
        "C:/Users/luna/some/domain2.tld":{
            "url_testing":"http://testing1",
            "url_production":"http://productiontld2"
        }
    }

### With relative paths

Imagine we have a project with the following structure

    Project/ < - root project folder
    Project/libs/
    Project/public/ < - the folder we want to load as "http://localhost/"
    Project/private/
    Project/experimental/ < - other folder we may run as experimental/test in another url "http://experimental/"

Then we create configuration file:

`Project/.sublime/SideBarEnhancements.json`

with content:

    {
        "public/":{
            "url_testing":"http://localhost/",
            "url_production":"http://domain.tld/"
        },
        "experimental/":{
            "url_testing":"http://experimental/",
            "url_production":"http://domain.tld/"
        },
        "":{
            "url_testing":"http://the_url_for_the_project_root/",
            "url_production":"http://the_url_for_the_project_root/"
        }
    }

You can create config files `some/folder/.sublime/SideBarEnhancements.json` anywhere.

#### F12 key conflict

On Sublime Text 3 `F12` key is bound to `"goto_definition"` command by default. This package was conflicting with that key, this no longers happens. You need to manually add the keys now, go to:
`Preferences -> Package Settings -> Side Bar -> Key Bindings - User`
and add any of the following:

    [
        { "keys": ["f12"],
            "command": "side_bar_open_in_browser" ,
            "args":{"paths":[], "type":"testing", "browser":""}
        },
        { "keys": ["alt+f12"],
            "command": "side_bar_open_in_browser",
            "args":{"paths":[], "type":"production", "browser":""}
        },
        {
            "keys": ["ctrl+t"],
            "command": "side_bar_new_file2"
        },
        {
            "keys": ["f2"],
            "command": "side_bar_rename"
        },
    ]

## Keybinding for Find in paths:

You may wish to add a key for opening "find in paths.."

    [
        {
            "keys": ["f10"],
            "id": "side-bar-find-files",
            "command": "side_bar_find_files_path_containing",
            "args": {
                "paths": []
            }
        }
    ]


## Notes on configuring the `Open With` menu:

Definitions file: `User/SideBarEnhancements/Open With/Side Bar.sublime-menu` (note the extra subfolder levels). To open it, right-click on any file in an open project and select `Open With > Edit Applications...`

- On macOS, the 'application' property simply takes the _name_ of an application, to which the file at hand's full path will be passed as if with `open ...`, e.g.: "application": "Google Chrome"
- On macOS, invoking _shell_ commands is NOT supported.
- You should change Caption and id of the menu item to be unique.

<!-- -->
    {
        "caption": "Photoshop",
        "id": "side-bar-files-open-with-photoshop",
        "command": "side_bar_files_open_with",
        "args": {
            "paths": [],
            "application": "Adobe Photoshop CS5.app", // macOS
            "extensions": "psd|png|jpg|jpeg",  // Any file with these extensions
            "multiple": true,
            "args": []
        }
    },

### Vars on "args" param

- \$PATH - The full path to the current file, "C:\Files\Chapter1.txt"
- \$PROJECT - The root directory of the current project.
- \$DIRNAME - The directory of the current file, "C:\Files"
- \$NAME - The name portion of the current file, "Chapter1.txt"
- \$NAME_NO_EXTENSION - The name portion of the current file without the extension, "Chapter1"
- \$EXTENSION - The extension portion of the current file, "txt"

## Using the External Libraries

(check each license in project pages)

- "getImageInfo" to get width and height for images from "bfg-pages". See: <https://code.google.com/p/bfg-pages/>
- "desktop" to be able to open files with system handlers. See: <https://pypi.python.org/pypi/desktop>
- "send2trash" to be able to send to the trash instead of deleting for ever!. See: <https://pypi.python.org/pypi/Send2Trash>
- "hurry.filesize" to be able to format file sizes. See: <https://pypi.python.org/pypi/hurry.filesize/>
- "Edit.py" ST2/3 Edit Abstraction. See: <https://www.sublimetext.com/forum/viewtopic.php?f=6&t=12551>

## Source-code

<https://github.com/CodeByZach/sublime_side_bar_enhancements>

## Forum Thread

<https://www.sublimetext.com/forum/viewtopic.php?f=5&t=3331>

# Contributors:

Thank you so much!

Aleksandar Urosevic, bofm, Dalibor Simacek, Devin Rhode, Eric Eldredge, Hewei Liu, Jeremy Gailor, Joao Antunes, Leif Ringstad, MauriceZ, Nick Zaccardi, Patrik Göthe, Peder Langdal, Randy Lai, Raphael DDL Oliveira, robwala, Stephen Horne, Sven Axelsson, Till Theis, Todd Wolfson, Tyler Thrailkill, Yaroslav Admin

## License

Side Bar Enhancements is released under the [GNU General Public License](LICENSE).
