

# THIS PROGRAM MAKES THE GOOGLE DRIVE SHARE LINK EMBEDDEBLE IN HTML FOR E.G.,IMAGES.


print("Give space after giving URL as input so as to not open the URL")      # WARNING

old_drive_link = str((input("Enter link : \n")))  #Takes Url as input

# old_drive_link =  "https://drive.google.com/file/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/view?usp=sharing"  : FORMAT OF GOOGLE DRIVE SHARE LINK

splited_link = old_drive_link.split("/")        # SPLITS IT INTO A LIST [.....]

id_part = splited_link[5]      # ACESSES TJE ID PART OF URL

# print(id_part)    : PRINT IT TO CHECK TH ID PART

joining_part = "https://drive.google.com/uc?export=view&id="       # THIS PART MAKES LINK EMBEDDEBLE IN HTML

link_to_embed = joining_part + id_part       # JOINS THE ID AND EMBEDDEBLE PART & GIVES FINAL LINK

print(link_to_embed)         # GET THE FINAL EMBEDDEBLE LINK

