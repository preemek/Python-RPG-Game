#Maks
import tkinter as tk
from tkinter import messagebox
from game_engine import GameEngine

MAX_LOG_LINES = 10

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_location_display(engine, location_label, description_label, explore_button, talk_button):
    location_label.config(text=f"Current Location: {engine.current_location.name}")
    description_label.config(text=engine.current_location.description)

    if engine.current_location.name.lower() == "village":
        explore_button.pack_forget()
        talk_button.pack(side=tk.LEFT)
    else:
        talk_button.pack_forget()
        explore_button.pack(side=tk.LEFT)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_inventory_display(engine, inventory_label):
    inventory_text = "Inventory: " + ", ".join(engine.player.inventory) if engine.player.inventory else "Inventory: Empty"
    inventory_label.config(text=inventory_text)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_log_display(engine, log_text_widget):
    logs = engine.logs.splitlines()
    if len(logs) > MAX_LOG_LINES:
        logs = logs[-MAX_LOG_LINES:]
    log_text_widget.delete(1.0, tk.END)
    log_text_widget.insert(tk.END, "\n".join(logs))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restart_game(engine, root, location_label, description_label, log_text_widget, inventory_label, restart_button, explore_button, talk_button):
    engine.reset_game()
    update_location_display(engine, location_label, description_label, explore_button, talk_button)
    update_inventory_display(engine, inventory_label)
    update_log_display(engine, log_text_widget)
    restart_button.pack_forget()
    check_game_status(engine, root, restart_button)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def check_game_status(engine, root, restart_button):
    if engine.player.hp <= 0:
        restart_button.pack()
    else:
        root.after(1000, check_game_status, engine, root, restart_button)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start_battle(engine, log_text_widget, inventory_label, fight_button, attack_button, use_item_button, flee_button, explore_button, talk_button, location_buttons):
    engine.start_battle()
    update_log_display(engine, log_text_widget)
    update_inventory_display(engine, inventory_label)
    engine.update_stats()

    fight_button.pack_forget()
    explore_button.pack_forget()
    talk_button.pack_forget()
    attack_button.pack(side=tk.LEFT)
    use_item_button.pack(side=tk.LEFT)
    flee_button.pack(side=tk.LEFT)

    for button in location_buttons:
        button.config(state=tk.DISABLED)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def end_battle(engine, log_text_widget, inventory_label, fight_button, attack_button, use_item_button, flee_button, explore_button, talk_button, location_buttons):
    engine.end_battle()
    update_log_display(engine, log_text_widget)
    update_inventory_display(engine, inventory_label)
    engine.update_stats()

    attack_button.pack_forget()
    use_item_button.pack_forget()
    flee_button.pack_forget()
    fight_button.pack(side=tk.LEFT)

    if engine.current_location.name.lower() == "village":
        talk_button.pack(side=tk.LEFT)
    else:
        explore_button.pack(side=tk.LEFT)

    for button in location_buttons:
        button.config(state=tk.NORMAL)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def open_item_selection(engine, log_text_widget, inventory_label):
    if not engine.player.inventory:
        engine.logs += "Your inventory is empty!\n"
        update_log_display(engine, log_text_widget)
        return

    item_window = tk.Toplevel()
    item_window.title("Select Item")

    for item in engine.player.inventory:
        tk.Button(
            item_window,
            text=item,
            command=lambda i=item: [
                engine.use_item(i),
                update_log_display(engine, log_text_widget),
                update_inventory_display(engine, inventory_label),
                item_window.destroy(),
            ],
        ).pack()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    root = tk.Tk()
    root.title("RPG Python Game")

    engine = GameEngine(root)

    location_label = tk.Label(root, text="", font=("Helvetica", 16))
    location_label.pack()

    description_label = tk.Label(root, text="", wraplength=400)
    description_label.pack()

    stats_label = tk.Label(root, text="Stats: HP: 100 | Level: 1 | EXP: 0/20", font=("Helvetica", 14))
    stats_label.pack()
    engine.stats_label = stats_label

    locations_frame = tk.Frame(root)
    locations_frame.pack()

    location_buttons = []
    for loc_name in engine.locations:
        button = tk.Button(
            locations_frame,
            text=loc_name.capitalize(),
            command=lambda l=loc_name: [
                engine.change_location(l),
                update_location_display(engine, location_label, description_label, explore_button, talk_button),
                engine.update_stats(),
            ],
        )
        button.pack(side=tk.LEFT)
        location_buttons.append(button)

    actions_frame = tk.Frame(root)
    actions_frame.pack()

    fight_button = tk.Button(
        actions_frame,
        text="Fight",
        command=lambda: start_battle(
            engine,
            log_text_widget,
            inventory_label,
            fight_button,
            attack_button,
            use_item_button,
            flee_button,
            explore_button,
            talk_button,
            location_buttons,
        ),
    )
    fight_button.pack(side=tk.LEFT)

    attack_button = tk.Button(
        actions_frame,
        text="Attack",
        command=lambda: [
            engine.player_attack(),
            update_log_display(engine, log_text_widget),
            update_inventory_display(engine, inventory_label),
            engine.update_stats(),
            end_battle(
                engine,
                log_text_widget,
                inventory_label,
                fight_button,
                attack_button,
                use_item_button,
                flee_button,
                explore_button,
                talk_button,
                location_buttons,
            ) if not engine.in_battle else None,
        ],
    )
    attack_button.pack_forget()

    use_item_button = tk.Button(
        actions_frame,
        text="Use Item",
        command=lambda: open_item_selection(engine, log_text_widget, inventory_label),
    )
    use_item_button.pack_forget()  

    flee_button = tk.Button(
        actions_frame,
        text="Flee",
        command=lambda: end_battle(
            engine,
            log_text_widget,
            inventory_label,
            fight_button,
            attack_button,
            use_item_button,
            flee_button,
            explore_button,
            talk_button,
            location_buttons,
        ),
    )
    flee_button.pack_forget() 

    explore_button = tk.Button(
        actions_frame,
        text="Explore",
        command=lambda: [
            engine.explore(),
            update_log_display(engine, log_text_widget),
            update_inventory_display(engine, inventory_label),
            engine.update_stats(),
        ],
    )

    talk_button = tk.Button(
        actions_frame,
        text="Talk",
        command=lambda: [
            engine.talk_to_npc(),
            update_log_display(engine, log_text_widget),
            update_inventory_display(engine, inventory_label),
            engine.update_stats(),
        ],
    )

    talk_button.pack_forget()

    inventory_label = tk.Label(root, text="Inventory: Empty", wraplength=400)
    inventory_label.pack()

    log_frame = tk.Frame(root)
    log_frame.pack()

    log_text_widget = tk.Text(log_frame, height=10, width=50, wrap=tk.WORD, bd=2)
    log_text_widget.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(log_frame, command=log_text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    log_text_widget.config(yscrollcommand=scrollbar.set)

    update_location_display(engine, location_label, description_label, explore_button, talk_button)
    update_inventory_display(engine, inventory_label)
    update_log_display(engine, log_text_widget)
    engine.update_stats()

    restart_button = tk.Button(
        root,
        text="Restart Game",
        command=lambda: restart_game(
            engine,
            root,
            location_label,
            description_label,
            log_text_widget,
            inventory_label,
            restart_button,
            explore_button,  
            talk_button,     
    ),
)

    check_game_status(engine, root, restart_button)

    root.mainloop()

if __name__ == "__main__":
    main()