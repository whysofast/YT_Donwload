import os


# Function to rename multiple files
def main():
    for count, filename in enumerate(os.listdir("F:\Músicas\Top single charts")):
        # dst = "Hostel" + str(count) + ".jpg"
        src = "F:\Músicas\Top single charts/".replace("/","\\") + filename
        newfilename = filename.split(" - 192 kbps")[0]+filename.split(" - 192 kbps")[1]
        newsrc = "F:\Músicas\Top single charts/".replace("/","\\") + newfilename

        os.rename(src, newsrc)
        print(newsrc)
        print(src)
        print(filename.split(" - 192 kbps")[0]+filename.split(" - 192 kbps")[1])
    # Driver Code


if __name__ == '__main__':
    # Calling main() function
    main()