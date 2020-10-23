# Memory Pill AWS

Memory Pill AWS passively records the last time a medication bottle was opened to prevent over- and underdosing of medications when you cannot remember if you have already taken a scheduled dose.  Medication data is transmitted to Amazon Web Services, and is viewable in a web dashboard.

Memory Pill AWS is an update to my previous [Memory Pill](https://github.com/nickbild/memory_pill) project.

## How It Works

<p align="center">
<img src="https://raw.githubusercontent.com/nickbild/memory_pill_aws/main/media/memory_pill_aws_overview.jpg">
</p>

A small hole is drilled into the threaded portion of a medicine bottle.  A pushbutton is attached inside the bottle so that the button lines up with the hole.  A 3D printed [button extender](https://github.com/nickbild/memory_pill/tree/master/3d_models) is glued to the button such that the bottle top depresses the button.  Removing the bottle top will then release the button.

The button is connected to a [Microchip AVR-IoT WA](https://www.microchip.com/Developmenttools/ProductDetails/EV15R70A).  When the button is released, the [AVR-IoT WA](https://github.com/nickbild/memory_pill_aws/tree/main/memory_pill_aws.X) sends an MQTT packet to AWS IoT Core.  The data is then stored in a table in AWS DynamoDB.  This database is used to populate a [web dashboard](https://github.com/nickbild/memory_pill_aws/tree/main/web_calendar) that displays a patient's medication administration record.

## Uses

I see the main use for Memory Pill as a monitoring device for assisted living patients or elderly relatives.  In the former case, it can aggregate data from a large number of individuals and provide alerts where medications have been missed (or taken more than scheduled).  This has the potential to significantly reduce time taken by humans to physically check on each case.  For the elderly, relatives could check up on medicine taking habits from across town, state, or country.

It also has uses for the young and healthy who can sometimes forget if they took a medication.  The idea for Memory Pill came to me when my wife had a headache, but couldn't remember if she had already taken medicine for it, or had just thought about it and not yet done so (kids can do that to a person).

## Media

YouTube:  

The device, with internal components removed:
![memory_pill](https://raw.githubusercontent.com/nickbild/memory_pill_aws/main/media/memory_pill_aws.jpg)

Schematic:
![schematic](https://raw.githubusercontent.com/nickbild/memory_pill_aws/main/media/schematic.png)

## Bill of Materials

- 1 x Microchip AVR-IoT WA
- 1 x 2.2K resistor
- 1 x 10K resistor
- 1 x Pushbutton
- 1 x Small LiPo battery pack
- OPTIONAL: 3D Printer to print button extender (can be replaced with misc. scrap materials)
- Miscellaneous wire

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
