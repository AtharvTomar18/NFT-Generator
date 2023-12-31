# the name of your collection.
NFT_NAME = 'Doodle Doods'

# the description of your collection
DESCRIPTION = "the result of a python code tutorial"

# enter number of desired images here
# number of desired images must be mathematically possible.
NUMBER_OF_DESIRED_IMAGES = 500

# enter the type of image file you are using including the '.'
FILE_TYPE = '.png'

# base uri/CID you get from IPFS
# AFTER you run the program and upload JUST the images to IPFS, you will get a CID 
# use "find all and replace" feature in your IDE to replace {REPLACE_WITH_CID} with the CID from IPFS
# this will update each JSON file so it points to the correct image on IPFS
BASE_URI = 'ipfs://{REPLACE_WITH_CID}'

# any website you want to link to
EXTERNAL_URL = 'https://www.{REPLACE_WITH_WEBSITE}.com'

# "True" if you want rarity score on csv AND JSON metadata "False" if you don't
ADD_RARITY= True

#the order of the layers in the image from left to right (bottom to top)
LAYER_ORDER = ["background", "head", "hair", "nose", "mouth", "eyes", "body", "arms", "logo", "ears", "hat", "slacker"]

# "folder name: [10, 40, 60, 30, 1]"
# values to be between 0 and 100. 
#  1=extremely rare, 100=always
# "weights are in the same order as the files in the folder 0=top file, 1=file below top, etc."
WEIGHTS = {
    "background" : [10, 40, 60, 3, 20, 30, 20],
    "head" : [10, 15, 20, 5, 20, 30],
    "hair" : [5, 10, 30, 40],
    "nose" : [30, 40, 8, 30, 25],
    "mouth" : [4, 12, 25, 30, 15],
    "eyes" : [11, 9, 15, 12, 11, 10, 10, 12, 17, 6, .5],
    "body" : [10, 30, 30, 2, 22, 32, 20, 12],
    "arms" : [50, 50, 10],
    "logo" : [60, 40],
    "ears" : [10, 40, 60, 30, 25],
    "hat" : [100], 
    "slacker" : [100]
}

#(((((((((((((((((((((((((((((((ADVANCED OPTIONS)))))))))))))))))))))))))))))))

# layers that are optional. not every image will contain them
# leave empty if you don't have optional layers
# use exclusive layers to indicate that only one of the layers can be used per image. if one is chosen, the others can not be on the same image
# use inclusive layers to indicate that any of the layers can be used on the same image 
INCLUSIVE_OPTIONAL_LAYERS = ["logo"]
EXCLUSIVE_OPTIONAL_LAYERS = ["hat", "slacker"]

# for use with optional layers
# if you have a trait that can not exist with other trait values, add that here 
# ex: 
# "sunglasses" : ["eyes"],
# "motorcycleHelmet" : ["eyes", "ears", "hat", "nose", "mouth"]
# if a motorcycle helmet is picked, 
# the eyes, ears, hat, nose, and mouth will be removed from the image
# this is done to keep the meta data clean 
# so attributes that aren't in the image are not included in the meta data
CONFLICTING_TRAITS = {
    "hat" : ["ears", "hair"], 
    "slacker" : ["ears", "mouth", "hair"]
}

# for optional layers. must be between 1 and desired number of images. 
# the more numbers you have the more likely it is for the image to have that layer 
LUCKY_NUMBERS = [2, 5, 25, 7, 225, 18, 2555, 575, 777, 42, 888, 1920, 4242, 444, 4444, 555, 4998, 1234, 2345, 3456, 4567, 4321, 321, 21, 1]
