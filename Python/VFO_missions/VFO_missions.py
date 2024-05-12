import tkinter as tk

def on_checkbox_click(index, mission_statuses, missions, status_label, file_path):
    mission_statuses[index] = not mission_statuses[index]
    save_missions(mission_statuses, file_path)
    update_status_label(missions, mission_statuses, status_label)

def reset_missions(mission_checkboxes, mission_statuses, missions, status_label, file_path):
    for i in range(len(mission_checkboxes)):
        mission_statuses[i] = False
        mission_checkboxes[i].set(False)
    save_missions(mission_statuses, file_path)
    update_status_label(missions, mission_statuses, status_label)

def save_missions(mission_statuses, file_path):
    with open(file_path, "w") as file:
        for status in mission_statuses:
            file.write(str(int(status)) + "\n")

def load_missions(mission_checkboxes, mission_statuses, file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i < len(mission_statuses):
                    mission_statuses[i] = bool(int(line))
                    mission_checkboxes[i].set(mission_statuses[i])
    except FileNotFoundError:
        pass

def update_status_label(missions, mission_statuses, status_label):
    total_missions = len(missions)
    missions_done = sum(mission_statuses)
    missions_left = total_missions - missions_done
    status_label.config(text=f"Total Missions: {total_missions} | Missions Done: {missions_done} | Missions Left: {missions_left}")

def open_mission_window(file_path, missions, mission_statuses):
    mission_window = tk.Toplevel(root)
    mission_window.title("Mission Tracker")

    mission_checkboxes = []

    # Sort missions alphabetically
    sorted_missions = sorted(missions)

    # Create a frame to hold the mission checkboxes
    checkbox_frame = tk.Frame(mission_window)
    checkbox_frame.pack(padx=10, pady=10)

    # Calculate number of columns based on the number of missions
    num_columns = 3
    num_rows = (len(sorted_missions) + num_columns - 1) // num_columns

    # Create checkboxes for each mission
    for i, mission in enumerate(sorted_missions):
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(checkbox_frame, text=mission, variable=checkbox_var, command=lambda i=i: on_checkbox_click(i, mission_statuses, missions, status_label, file_path))
        checkbox.grid(row=i % num_rows, column=i // num_rows, sticky="w")
        checkbox_var.set(mission_statuses[missions.index(mission)])
        mission_checkboxes.append(checkbox_var)

    # Load mission statuses from file
    load_missions(mission_checkboxes, mission_statuses, file_path)

    # Button to reset missions
    reset_button = tk.Button(mission_window, text="Reset Missions", command=lambda: reset_missions(mission_checkboxes, mission_statuses, missions, status_label, file_path))
    reset_button.pack(pady=10)

    # Status label
    status_label = tk.Label(mission_window, text="")
    status_label.pack()

    # Update status label
    update_status_label(missions, mission_statuses, status_label)


# Create the main window
root = tk.Tk()
root.title("Mission Selection")

# Define lists of missions for Mission 1 and Mission 2
mainland_missions = ["The Package", "Clearing The Fields", "Gorneval's Favorite", "Petyr the Eye-less", 
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

denumald_missions = ["Welcome to Denumald", "Sightseeing the Island", "Deliver Letter", "Thing in stump. Again.",
            "The Hooded Brotherhood", "Send for more wood", "Kill em' Bandits", "Slay Dragonlings", 
            "Still Alive?", "Like Hay in the wind", "Convince Husband", "The map on the stone",
            "Yeti", "They were wolves", "Mortem Contractor Ironhold 1", "Mortem Contractor Ironhold 2",
            "Mortem Contractor Ironhold 3", "Tender meat", "Missing Fire Watcher", "The First Watchers",
            "The Sabotage at Eyjan Farm", "The Portal", "Ruins", "Mike's Boxes", "Letter from Box",
            "The Mountain Calls", "Ruins again", "Ruins yet again", "Follow the Light",
            "The King's Hammer", "The Fate of The Mountain King", "Light the Bush",
            "The End of the Swamp", "Bloodstone Mines", "Fountains", "Burning Bones",
            "Bring The Message", "Victims", "Rebuild the Bridge", "Salty", "Haunted Houses",
            "Swamp Quest", "Creator of The Blue Light", "Ambushed", "Mortem Contractor Mangrove 1",
            "Mortem Contractor Mangrove 2", "Mortem Contractor Smuggler's Bay 1",
            "Mortem Contractor Smuggler's Bay 2", "Mortem Contractor Smuggler's Bay 3",
            "Mortem Contractor Gordova 1", "Mortem Contractor Gordova 2", "Mortem Contractor Gordova 3",
            "Helping the Farseers", "The Three Golems", "The Stone Angels of Shal'tuhn",
            "Map 4th Part (*Hunt for Sava)"]

# Button to open mainland missions window
mainland_button = tk.Button(root, text="Mainland Missions", command=lambda: open_mission_window("mission1_status.txt", mainland_missions, mainland_statuses))
mainland_button.pack(pady=10)

# Button to open denumald missions window
denumald_button = tk.Button(root, text="Denumald Missions", command=lambda: open_mission_window("mission2_status.txt", denumald_missions, denumald_statuses))
denumald_button.pack(pady=10)

# Initialize the lists for mission statuses
mainland_statuses = [False] * len(mainland_missions)
denumald_statuses = [False] * len(denumald_missions)

# Run the GUI loop
root.mainloop()
