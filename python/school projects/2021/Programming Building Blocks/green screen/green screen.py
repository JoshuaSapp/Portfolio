from PIL import Image
import os

def do_green_screen(Foreground,Background,filename,R,G,B,tolarance):

    r_tolarance = tolarance
    g_tolarance = tolarance
    b_tolarance = tolarance
    
    foreground = Image.open(Foreground)
    background = Image.open(Background)
    image_new = Image.new("RGB", background.size)


    foreground_pixels = foreground.load()
    background_pixels = background.load()
    pixels_new = image_new.load()

    f_width, f_height = foreground.size
    b_width, b_height = background.size

    if f_width != b_width or f_height != b_height:
        print("Images are not the same size, some weirdness may occur")

    y = 0
    while y < b_height:
        x = 0
        while x < b_width:
            r, g, b = foreground_pixels[x, y]

            if r <= R +r_tolarance and g <= G +g_tolarance and b <= B +b_tolarance and r >= R -r_tolarance and g >= G -g_tolarance and b >= B -b_tolarance:
                pixels_new[x,y] = background_pixels[x,y]
            else:
                pixels_new[x,y] = foreground_pixels[x,y]


            x += 1
        y += 1
    image_new.save(f"outputs/{filename}.jpg")


def process_files():
    out_folder = "outputs"
    out_folder_exists = os.path.exists(out_folder)

    if out_folder_exists == False:
        os.makedirs(out_folder)
    background_file_list = []
    green_file_list = []

    for file in os.listdir("cse110_images/green"):
        file_name = file.split('.')
        file_name = file_name[0]
        green_file_list.append(file_name)

    for file in os.listdir("cse110_images/background"):
        file_name = file.split('.')
        file_name = file_name[0]
        background_file_list.append(file_name)

    for foreground in green_file_list:
        for background in background_file_list:
            if foreground == "boat":
                r = 86
                g = 196
                b = 61
                tolarance = 60
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "cactus":
                r = 76
                g = 244
                b = 24
                tolarance = 20
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "cat_small":
                r = 66
                g = 229
                b = 24
                tolarance = 25
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "cat":
                r = 66
                g = 229
                b = 24
                tolarance = 25
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "harvester":
                r = 88
                g = 195
                b = 63
                tolarance = 20
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "hiker":
                r = 44
                g = 207
                b = 64
                tolarance = 20
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "penguin":
                r = 44
                g = 207
                b = 64
                tolarance = 20
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)
            if foreground == "spaceshuttle":
                r = 44
                g = 207
                b = 64
                tolarance = 20
                do_green_screen(f"cse110_images/green/{foreground}.jpg",f"cse110_images/background/{background}.jpg",f"{foreground}_{background}",r,g,b,tolarance)

process_files()

