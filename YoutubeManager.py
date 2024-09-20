
import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
     

def List_all_videos(videos):
    print("\n")
    print("*" * 70)
    
    for index,videos in enumerate(videos ,start=1):
        print(f"{index}.{videos['name']},Duration:{videos['time']}")

    print("\n")
    print("*" * 70)

            
def Add_video(videos):
    name=input('Enter video Name:--')
    time=input("Enter a Time of Video:--")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def Update_video(videos):
    List_all_videos(videos)
    index=int(input("Enter the video number to update:--"))
    if 1<=index <= len(videos):
        name=input("Enter the new video name:--")
        time=input("Enter the Time of  video:--")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")



def delete_video(videos):
    List_all_videos(videos)
    index=int(input("Enter the video number to be deleted:--"))

    if 1<=index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

videos = load_data()

        
while True:
        print("\n Youtube Manager ! choose an option ")
        print("1. List All of Youtube Videos")
        print("2.Add a Youtube video")
        print("3.Update a Youtube video Details")
        print("4. Delete a Video ")
        print("5.Exit the app")

        choice =input("Enter your Choice:--")
        # print(videos)

        match choice:
            case '1':
                List_all_videos(videos)
            case '2':
                Add_video(videos)
            case '3':
                Update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice...!")



        