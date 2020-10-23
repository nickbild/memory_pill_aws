# Memory Pill AWS

Memory Pill AWS passively records the last time a medication bottle was opened to prevent over- and underdosing of medications when you cannot remember if you have already taken a scheduled dose.  Medication data is transmitted to Amazon Web Services, and is viewable in a web dashboard.

Memory Pill AWS is an update to my previous [Memory Pill](https://github.com/nickbild/memory_pill) project.

## How It Works

<p align="center">
<img src="https://raw.githubusercontent.com/nickbild/memory_pill_aws/main/media/memory_pill_overview.jpg">
</p>

A small hole is drilled into the threaded portion of a medicine bottle.  A pushbutton is attached inside the bottle so that the button lines up with the hole.  A 3D printed [button extender](https://github.com/nickbild/memory_pill/tree/master/3d_models) is glued to the button such that the bottle top depresses the button.  Removing the bottle top will then release the button.
