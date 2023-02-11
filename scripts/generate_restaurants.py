import csv
from PIL import Image, ImageDraw, ImageFont

# Set the width and height of the playing card
card_width = 450
card_height = 300

# Open the CSV file and read its contents
with open("../data/restaurants.csv") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip the header row
    for row in reader:
        # Create a new image for each row
        card_image = Image.new("RGB", (card_width, card_height), (255, 255, 255))
        draw = ImageDraw.Draw(card_image)

        # Add the text from the CSV file to the image
        font = ImageFont.truetype("../fonts/arial.ttf", 20)
        draw.text((30, 20), row[0], font=font, fill=(0, 0, 0))

        wordsperline = 4
        words = row[1].split()
        lines = (int)(len(words)/wordsperline+1)

        print(lines)

        for i in range(0,lines):
            if i<lines:
                draw.text((60, i*30+70), ' '.join(words[i*wordsperline:(i+1)*wordsperline]), font=font, fill=(0, 0, 0))




        # Save the image
        card_image.save(f"../generated/restaurants/{row[0]}.png")