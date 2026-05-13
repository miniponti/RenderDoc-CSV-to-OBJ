# Extract models and textures from Dolphin emulation

This is the guide I wish I had when I started, so I hope it's helpful for you!

I actually haven't tried with other games or other consoles, but it should work the same way.

## ⚠️ Recommendations ⚠️
- Opening Dolphin from Renderdoc runs games reaaaaaally slowly, like at 4 fps. If you still haven't played the game, start a new run before this process and save the game at least in one state slot, so when you open Dolphin from Renderdoc you can directly load the game at your desired spot.

- The object you want must be visible on screen.

## Step 1: Set up Dolphin Emulator

1. Download latest dolphin version: ![Dolphin Emulator](https://es.dolphin-emu.org)
2. Head to **Settings/Config** -> **Graphics** and in the **General** tab you'll see the **Backend** option. Set it to: `Direct3D 11`
![App Screenshot](readme_img/dolphin_general.png)

3. Now in the same **Graphics** section, head to the **Hacks** tab. Uncheck `Skip EFB Access from CPU`
![App Screenshot](readme_img/dolphin_hacks.png)

## Step 2: Launch Dolphin from within RenderDoc
Close Dolphin Emulator and open RenderDoc. You'll be greeted with the following screen:

![App Screenshot](readme_img/renderdoc.png)

Go to **File** -> **Launch Application** and change the following options:

- Executable Path -> path to Dolphin.exe
- Working Directory -> Dolphin's folder

As in the picture:
![App Screenshot](readme_img/renderdoc_launch.png)

Click on **Launch**.
Now Dolphin will start normally. Open your game, load the save/state and head back to RenderDoc. You'll see a new tab has opened with the name Dolphin.

## Step 3: Capture frames

![App Screenshot](readme_img/renderdoc_captures.png)

1. Press **Capture Frame(s) Immediately**. A screenshot of the game will appear.
2. Select the capture and save it.
3. To open it, double-click it.

