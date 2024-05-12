import tkinter as tk

def on_checkbox_click(index):
    mission_statuses[index] = not mission_statuses[index]
    save_missions()
    update_status_label()

def reset_missions():
    for i in range(len(mission_checkboxes)):
        mission_statuses[i] = False
        mission_checkboxes[i].set(False)
    save_missions()
    update_status_label()

def save_missions():
    with open("mission_status.txt", "w") as file:
        for status in mission_statuses:
            file.write(str(int(status)) + "\n")

def load_missions():
    try:
        with open("mission_status.txt", "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                mission_statuses[i] = bool(int(line))
                mission_checkboxes[i].set(mission_statuses[i])
    except FileNotFoundError:
        pass

def update_status_label():
    total_missions = len(missions)
    missions_done = sum(mission_statuses)
    missions_left = total_missions - missions_done
    status_label.config(text=f"Total Missions: {total_missions} | Missions Done: {missions_done} | Missions Left: {missions_left}")

# Sample missions
missions = ["The Package", "Clearing The Fields", "Gorneval's Favorite", "Petyr the Eye-less", 
            "A Visit To Marid's Place", "Master the Hunt", "Sergeant Tents",
            "Hunters Lunch", "The Blue Rat", "Bringing the Bad News",
            "Collect Wood", "Buried Bones", "Curse Of Westwood Farm",
            "Last Wish", "The Ruins of Aendisea", "Iron Mines",
            "Lost Book Box", "Sign the Book", "Shapeshifter Among Us",
            "Master The Hunt - Part 2", "Sarcophagus Secret", "Hanged", "Kill the Lieutenants",
            "Finding the Medallions", "Brother of the Hooded Brotherhood", "Kill the Adventure Killer",
            "Beating Farmers", "Ring in Tree Stump", "Find Cutie Pie", "Just Business", 
            "The Stolen Cross", "Find the Necklace", "It's Always Raining In Delphi",
            "Missing Lumberjack", "Rats", "Finding the Lost Son - Again", "Swamp Strength",
            "Over There", "Missing Fishing Rod", "The Cursed Church", "Master the Hunt - Part 3",
            "Healing the Oak", "Help the Potion Maker", "Unwanted Demon", "The Cult",
            "Tournament of Duels", "Kevin", "Cleanse the Crypts", "Crab Sticks",
            "Flowers on Graves", "Helping the Philosopher", "Walker of Soil",
            "Master the Hunt - Final Part", "Solve the Riddle 1", "Solve the Riddle 2",
            "Solve the Riddle 3", "Solve the Riddle 4", "Solve the Riddle 5",
            "World Cornerstones", "Maelstroms"]

mission_statuses = [False] * len(missions)

# Sort missions alphabetically
missions.sort(key=lambda x: x.lower())

# Create the main window
root = tk.Tk()
root.title("Mission Tracker")

# Create a frame to hold the mission checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(padx=10, pady=10)

# Split missions into 3 columns
num_cols = 3
num_rows = (len(missions) + num_cols - 1) // num_cols

# Create checkboxes for each mission
mission_checkboxes = []
for i, mission in enumerate(missions):
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(checkbox_frame, text=mission, variable=checkbox_var, command=lambda i=i: on_checkbox_click(i))
    checkbox.grid(row=i // num_cols, column=i % num_cols, sticky="w")
    checkbox_var.set(mission_statuses[i])
    mission_checkboxes.append(checkbox_var)

# Load mission statuses from file
load_missions()

# Button to reset missions
reset_button = tk.Button(root, text="Reset Missions", command=reset_missions)
reset_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Update status label
update_status_label()

# Run the GUI loop
root.mainloop()
