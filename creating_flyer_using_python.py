# -*- coding: utf-8 -*-
"""Creating Flyer using Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A9ECEzdaNyn3jcsxuPzpqXg6Szcayo9g
"""

!pip install pillow

# Install necessary library
!pip install pillow

from PIL import Image, ImageDraw, ImageFont

# Step 1: Create a blank canvas
width, height = 800, 1200  # Flyer size in pixels
flyer = Image.new('RGB', (width, height), color='white')

# Step 2: Initialize drawing
draw = ImageDraw.Draw(flyer)

# Step 3: Define fonts
try:
    # Load a default font
    title_font = ImageFont.truetype("arial.ttf", 60)
    subtitle_font = ImageFont.truetype("arial.ttf", 40)
    body_font = ImageFont.truetype("arial.ttf", 30)
except IOError:
    # Use default PIL font if specific fonts are not available
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# Step 4: Add text to the flyer
# Title
title = "Grand Opening!"
draw.text((50, 50), title, font=title_font, fill="darkblue")

# Subtitle
subtitle = "Your Favorite Store, Now Open"
draw.text((50, 150), subtitle, font=subtitle_font, fill="darkred")

# Body Text
body = (
    "Join us for the grand opening of our new store!\n"
    "Date: January 15th, 2025\n"
    "Time: 10:00 AM - 8:00 PM\n"
    "Location: 123 Main Street, Springfield\n"
    "Exciting offers, giveaways, and more!"

)
draw.multiline_text((50, 250), body, font=body_font, fill="black", spacing=10)

# Step 5: Add a border (optional)
border_width = 20
draw.rectangle(
    [(border_width, border_width), (width-border_width, height-border_width)],
    outline="black", width=5
)

# Step 6: Save and display the flyer
output_path = "flyer.png"
flyer.save(output_path)
flyer.show()  # Display in Colab (requires PIL viewer support)

# Display the image in Colab notebook
from IPython.display import Image as IPImage, display
display(IPImage(output_path))

# Install necessary library
!pip install pillow

from PIL import Image, ImageDraw, ImageFont

# Step 1: Create a blank canvas
width, height = 800, 1200  # Flyer size in pixels
flyer = Image.new('RGB', (width, height), color='white')

# Step 2: Initialize drawing
draw = ImageDraw.Draw(flyer)

# Step 3: Define fonts
try:
    # Load a default font
    title_font = ImageFont.truetype("arial.ttf", 60)
    subtitle_font = ImageFont.truetype("arial.ttf", 40)
    body_font = ImageFont.truetype("arial.ttf", 30)
except IOError:
    # Use default PIL font if specific fonts are not available
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# Step 4: Add text to the flyer
# Title
title = "Grand Opening!"
draw.text((50, 50), title, font=title_font, fill="darkblue")

# Subtitle
subtitle = "PRAGYANAI"
draw.text((50, 150), subtitle, font=subtitle_font, fill="darkred")

# Body Text
body = (
    "Join us for the Hands-on Bootcamp\n"
    "Date: January 10th, 2025\n"
    "Time: 9:00 AM - 6:00 PM\n"
    "Topic covered: Generative AI, Data Science\n"
    "Gain exposure to key GenAI tools and concepts"
)
draw.multiline_text((50, 250), body, font=body_font, fill="black", spacing=10)

# Step 5: Add a border (optional)
border_width = 20
draw.rectangle(
    [(border_width, border_width), (width-border_width, height-border_width)],
    outline="black", width=5
)

# Step 6: Save and display the flyer
output_path = "flyer.png"
flyer.save(output_path)
flyer.show()  # Display in Colab (requires PIL viewer support)

# Display the image in Colab notebook
from IPython.display import Image as IPImage, display
display(IPImage(output_path))

"""                                                                     OR"""

!pip install pillow

from PIL import Image

# Create a blank white canvas
width, height = 800, 1200  # Flyer dimensions
flyer = Image.new('RGB', (width, height), color='white')

# Display the blank flyer
flyer.show()

from PIL import ImageDraw

# Initialize drawing context
draw = ImageDraw.Draw(flyer)

from PIL import ImageFont

try:
    # Load fonts
    title_font = ImageFont.truetype("arial.ttf", 60)
    subtitle_font = ImageFont.truetype("arial.ttf", 40)
    body_font = ImageFont.truetype("arial.ttf", 30)
except IOError:
    # Fallback if fonts are not available
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# Title
title = "Grand Opening!"
draw.text((50, 50), title, font=title_font, fill="darkblue")

# Subtitle
subtitle = "Your Favorite Store, Now Open"
draw.text((50, 150), subtitle, font=subtitle_font, fill="darkred")

# Body Text
body = (
    "Join us for the grand opening of our new store!\n"
    "Date: January 15th, 2025\n"
    "Time: 10:00 AM - 8:00 PM\n"
    "Location: 123 Main Street, Springfield\n"
    "Exciting offers, giveaways, and more!"
)
draw.multiline_text((50, 250), body, font=body_font, fill="black", spacing=10)

# Add a border
border_width = 20
draw.rectangle(
    [(border_width, border_width), (width-border_width, height-border_width)],
    outline="black", width=5
)

# Save the flyer
output_path = "flyer.png"
flyer.save(output_path)

# Display in the Colab notebook
from IPython.display import Image as IPImage, display
display(IPImage(output_path))

