# Extract models and textures from Dolphin emulation

This is the guide I wish I had when I started, so I hope it's helpful for you!

I actually haven't tried with other games or other consoles, but it should work the same way. 

## Step 1: Set up Dolphin Emulator

1. Download latest dolphin version: ![Dolphin Emulator](https://es.dolphin-emu.org)
2. Head to **Settings/Config** -> **Graphics** and in the **General** tab you'll see the **Backend** option. Set it to: `Direct3D 11`
![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

3. Now in the same **Graphics** section, head to the **Hacks** tab. Uncheck `Skip EFB Access from CPU`
![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

## Step 2: Launch Dolphin from within RenderDoc
Close Dolphin Emulator and open RenderDoc. You'll be greeted with the following screen:

![App Screenshot](https://dummyimage.com/468x300?text=App+Screenshot+Here)

Go to **File** -> **Launch Application** and change the following options:

- 
