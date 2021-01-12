# MEMECROPPER
Ladies and Gentlemen, (lads and ladies if you will)

### ***behold --***

**T**he apex of my scripting capabilites, a poorly cobbled-together handful of programs that when used correctly, will automatically crop your memes.

Yeah, I know, it sounds lame, but hear me out.


Are you an avid ifunny.co user? If so, you know that it is a serious faux pas to post, comment with, or otherwise share with the world, a meme that has the dreaded "ifunny.co" watermark at the bottom.
Hence, I have created a program that can work together with your phone and computer to take a folder of memes, crop the ones with watermarks, and copy them to another folder.

You can make it even more helpful by making your save location on your phone mirrored to google drive, and mirror the output folder in drive to your phone.
The way I have it set up, I have the folder where memes are saved on my phone uploaded to GD then deleted every 5 minutes. Every 15 minutes, my computer runs `cropthememes.bat` which performs it's magic.

It deletes the old memes, and copies the new ones to a local GD folder on my computer. Every 5 minutes the contents of this folder in drive are then downloaded & deleted to my phone, where the resulting images are saved to my photos.
The whole process means that when I save a photo, it is not saved to my phone camera roll for up to 25 minutes, (usually less), but when it is, it has no watermark.
Images without a watermark are left alone, and videos are also left alone.

If you would like to recreate this glorious experience, hesitate no longer. Clone this repository, and the execute `setup.bat`. It will prompt you for the locations of the two local google drive folders on your computer, and also the location of your `python.exe` file (python 3 only)
This is most likely in Program Files/Python{version}/python.exe, but your mileage may vary. If you enter in these paths correctly, the `setup.bat` will setup a few more python programs to work in concert with `cropTheGoddamnMemes.py` and will also generate an executable `cropmemes.bat` file.

Once you have this file, all you need to do is set this program to run every so often using Task Scheduler. I have provided a task template for you to use, but no guarantees, you might just have to set it up yourself if it doens't work for you.
My preferred settings are to run the program every 15 minutes and also at login, but do what you like.

Please know, I make no guarantees as to the viability of this set of programs, just bear in mind that they work for me as given, and if they don't for you, you're smart, you can modify them and check [StackOverflow](www.stackoverflow.com) if you run into any issues.

If you have the guts to look at my code, make sure you're sitting down, then please remember I cannot and will not be held responsible for any injuries caused as a result of your ineveitable fainting.
