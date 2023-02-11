import csv
from PIL import Image, ImageDraw, ImageFont

# Set the width and height of the playing card
card_width = 300
card_height = 450

# Open the CSV file and read its contents
with open("../data/ingredients.csv") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip the header row
    for row in reader:
        # Create a new image for each row
        card_image = Image.new("RGB", (card_width, card_height), (255, 255, 255))
        draw = ImageDraw.Draw(card_image)

        # Add the text from the CSV file to the image
        font = ImageFont.truetype("../fonts/arial.ttf", 20)
        draw.text((230, 30), row[1], font=font, fill=(0, 0, 0))
        draw.text((30, 30), row[3], font=font, fill=(0, 0, 0))
        draw.text((30, 90), row[0], font=font, fill=(0, 0, 0))
        draw.text((30, 120), row[2], font=font, fill=(0, 0, 0))

        # Save the image
        card_image.save(f"../generated/ingredients/{row[0]}.png")