# PyEngine4

Python 2D Game Engine

## Installation, Download, Usage

Documentation : <https://pyengine4-docs.readthedocs.io/>

## Dependancies

### Editor

- Python 3
- PyGame 2
- PyQt 5

### Game made with PyEngine4

- Python 3
- PyGame 2

## Features

- Assets : Textures, Scripts, Scenes
- Child system
- Rotation, scale, position with a component
- Sprite, Spritesheet and Text rendering
- Collision detection with Callback
- Ultra-basic physics (only Gravity) without engine
- Build and Launch System

## Uncoming Features

*Warning : This is a non-exhaustive list and subject to change.*

- Prefabs
- Particles System
- Translation System
- Save System
- Player Settings System
- UI
- Translation of PyEngine4
- Themes for PyEngine4
- New Components : ShapeComponent, AnimComponent
- Integration of a 2D physics Engine

## Changelog

Caption : [+] Addition, [~] Modification, [-] Deletion, [#] Bug fix 

### V 1.1.0 : Kisure Update - XX/XX/XX (INDEV)

- [+] Engine Settings
- [+] Utility classes : Vec2, Color, Math
- [+] requirements.txt
- [+] Components : ButtonComponent, TimeScaleComponent, MusicComponent
- [+] Assets : Sounds
- [+] Project Settings : Number of mixer channels
- [+] Pong assets in project_files (must be relinked to project)
- [+] Color picker in components widgets
- [+] Tag in GameObject
- [~] Open a project from a different version of PE4
- [~] Upgrade UI of ComponentsWidget and AssetsExplorer
- [~] Can now use more than one key for ControlComponent
- [~] Specify size of collision in CollisionComponent
- [~] Modification of Game Properties is now apply (title, width, height)
- [~] Textures have their own directory in build
- [~] You can now drag and drop scripts to ScriptComponent and textures to SpriteComponent or SpriteSheetComponent
- [#] Down_keys and Down_mousebutton in Engine can make crash
- [#] Missing Assets make crashes
- [#] Can't launch game if Sound or Texture path is None
- [#] Create gameobject without opened scene make crash

### V 1.0.0 : Colombe Update - 04/04/21 (LATEST)

- First version
