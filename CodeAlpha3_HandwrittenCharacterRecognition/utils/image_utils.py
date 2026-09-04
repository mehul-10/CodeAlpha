from PIL import Image, ImageOps
import numpy as np


# ============================================================
# IMAGE PREPROCESSING
# ============================================================

def preprocess_image(image):
    """
    Convert an uploaded handwritten digit image into the
    28x28 grayscale format expected by the MNIST CNN.

    Returns:
        processed_image : 28x28 numpy array
        display_image   : PIL image showing the processed input
    """

    # --------------------------------------------------------
    # 1. Convert to grayscale
    # --------------------------------------------------------

    image = image.convert("L")

    # --------------------------------------------------------
    # 2. Convert image to numpy array
    # --------------------------------------------------------

    image_array = np.array(image)

    # --------------------------------------------------------
    # 3. Normalize image orientation
    #
    # MNIST:
    #   Black background = 0
    #   White digit     = 255
    #
    # If the uploaded image has a bright background and
    # dark handwriting, invert it.
    # --------------------------------------------------------

    if np.mean(image_array) > 127:
        image_array = 255 - image_array

    # --------------------------------------------------------
    # 4. Remove very small background noise
    # --------------------------------------------------------

    threshold = 30

    image_array[image_array < threshold] = 0

    # --------------------------------------------------------
    # 5. Find bounding box of the handwritten digit
    # --------------------------------------------------------

    coordinates = np.argwhere(
        image_array > 0
    )

    if coordinates.size == 0:
        raise ValueError(
            "No handwritten digit could be detected "
            "in the uploaded image."
        )

    y_min, x_min = coordinates.min(axis=0)
    y_max, x_max = coordinates.max(axis=0)

    # --------------------------------------------------------
    # 6. Crop to the digit
    # --------------------------------------------------------

    cropped = image_array[
        y_min:y_max + 1,
        x_min:x_max + 1
    ]

    # --------------------------------------------------------
    # 7. Convert cropped digit back to PIL
    # --------------------------------------------------------

    cropped_image = Image.fromarray(
        cropped.astype(np.uint8)
    )

    # --------------------------------------------------------
    # 8. Resize while maintaining aspect ratio
    #
    # MNIST digits occupy roughly a 20x20 area inside
    # the 28x28 canvas.
    # --------------------------------------------------------

    width, height = cropped_image.size

    if width > height:

        new_width = 20
        new_height = max(
            1,
            int(height * 20 / width)
        )

    else:

        new_height = 20
        new_width = max(
            1,
            int(width * 20 / height)
        )

    cropped_image = cropped_image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )

    # --------------------------------------------------------
    # 9. Create 28x28 black canvas
    # --------------------------------------------------------

    canvas = Image.new(
        "L",
        (28, 28),
        0
    )

    # --------------------------------------------------------
    # 10. Center the digit
    # --------------------------------------------------------

    x_offset = (28 - new_width) // 2
    y_offset = (28 - new_height) // 2

    canvas.paste(
        cropped_image,
        (x_offset, y_offset)
    )

    # --------------------------------------------------------
    # 11. Convert to numpy array
    # --------------------------------------------------------

    processed_image = np.array(
        canvas,
        dtype=np.float32
    )

    # --------------------------------------------------------
    # 12. Normalize to 0–1
    # --------------------------------------------------------

    processed_image = (
        processed_image / 255.0
    )

    return processed_image, canvas