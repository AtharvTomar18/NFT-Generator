from colorama import init, Fore
init(autoreset=True)

EMPTY_INPUT = Fore.RED + 'The input folder does not contain any folders or files. please place attribute folders into input folder'

INPUT_FOUND = Fore.GREEN + 'Input attributes successfully gathered'

NO_INPUT = Fore.YELLOW + 'There was no input folder\nA new input folder has been created,\nbut you will need to add the attribute folders and files before restarting the program'

FINISHED = Fore.GREEN + 'nft metadata has been assembled. review rarity.json file'

NFTS_ASSEMBLED = Fore.GREEN + 'NFT ingredients successfully collected and mixed. baking images now...'

REVIEW_MESSAGE = Fore.YELLOW + 'review the rarity.json file.\nif you are happy with the results, type "yes" to create images\ntype "no" to try again.\n>>> '

RERUN = Fore.RED + 'please rerun the program to try again.'

RARE = Fore.GREEN + 'LUCKY NUMBER MATCH!'

IMPOSSIBLE = Fore.RED + 'Your desired number of images is too large a too large of request.\nYou may not have enough traits, or weights may be off balance.\nto fix this you will need to add more unique layers or ask for fewer images'