import sys
from PIL import Image, ImageFile

def GetInfo():
    print("Arguments: 'path/to/png' 'path/to/output'")

def Run():
    if len(sys.argv) <= 1:
        GetInfo()
        return
    
    im: ImageFile.ImageFile
    try:
        im = Image.open(sys.argv[1])
    except:
        print("First argument failure: Invalid image path.")
        return
    base = Image.new("RGBA", (im.size[0] // 2, im.size[1]))
    faceSize = (base.size[0] // 2, base.size[1] // 3)

    # Front
    front = Image.new("RGBA", faceSize)
    front.paste(im, (faceSize[0] * -1, faceSize[1] * -1))

    # Back
    back = Image.new("RGBA", faceSize)
    back.paste(im, (faceSize[0] * -3, faceSize[1] * -1))

    # Left
    left = Image.new("RGBA", faceSize)
    left.paste(im, (faceSize[0] * -0, faceSize[1] * -1))

    # Right
    right = Image.new("RGBA", faceSize)
    right.paste(im, (faceSize[0] * -2, faceSize[1] * -1))

    # Top
    top = Image.new("RGBA", faceSize)
    top.paste(im, (faceSize[0] * -1, faceSize[1] * -0))

    # Bottom
    bottom = Image.new("RGBA", faceSize)
    bottom.paste(im, (faceSize[0] * -1, faceSize[1] * -2))


    # Merge it all
    base.paste(right, (faceSize[0] * 0, faceSize[1] * 0))
    base.paste(left, (faceSize[0] * 1, faceSize[1] * 0))
    base.paste(bottom, (faceSize[0] * 1, faceSize[1] * 1))
    base.paste(top, (faceSize[0] * 0, faceSize[1] * 1))
    base.paste(front, (faceSize[0] * 0, faceSize[1] * 2))
    base.paste(back, (faceSize[0] * 1, faceSize[1] * 2))

    # Save to path
    if len(sys.argv) == 3:
        try:
            base.save(sys.argv[2])
            print(f"Saved to {sys.argv[2]}")
            return
        except:
            print("Failed to save to specified file path.")

    base.save("output.png")
    print("Saved to output.png")
    


if __name__ == '__main__':
    Run()
