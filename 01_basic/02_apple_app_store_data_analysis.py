import io

AppleStore= open("../resource/data/app-store-apple-data-set-10k-apps/AppleStore.csv","r")


for row in AppleStore.readlines():
    print(row.split(","))
