import character_variable, prompt_gen
from prompt_work import response_chatbot, response_memory


print('''Available characters:
    1. Gojo
    2. Itachi
    3. Naruto
    4. Daniel Park
    5. Gun Yamazaki
    6. Vasco
    7. Jay
    8. Jace
    9. Luffy
    10. Zoro
    11. Sanji
    12. Nami
    13. Robin
    14. Brook
    15. Chopper
    16. Gold D. Roger''')

# User selects character
while True:
    try:
        choice = int(input("Choose a character by entering the corresponding number: "))
        if 0 <= choice <= 16:
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 16.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
# Logic for Return Message
# Gojo
if choice == 1:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Gojo conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["gojo"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["gojo"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["gojo"]["default_memory"] = new_memory
                print(f"Gojo: {response}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

# Itachi
elif choice == 2:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Itachi conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["itachi"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["itachi"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["itachi"]["default_memory"] = new_memory
                print(f"Itachi: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Naruto
elif choice == 3:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Naruto conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["naruto"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["naruto"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["naruto"]["default_memory"] = new_memory
                print(f"Naruto: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Daniel Park
elif choice == 4:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Daniel Park conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["daniel_park"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["daniel_park"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["daniel_park"]["default_memory"] = new_memory
                print(f"Daniel Park: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Gun Yamazaki
elif choice == 5:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Gun Yamazaki conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["gun_yamazaki"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["gun_yamazaki"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["gun_yamazaki"]["default_memory"] = new_memory
                print(f"Gun Yamazaki: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Vasco
elif choice == 6:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Vasco conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["vasco"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["vasco"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["vasco"]["default_memory"] = new_memory
                print(f"Vasco: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Jay
elif choice == 7:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Jay conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["jay"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["jay"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["jay"]["default_memory"] = new_memory
                print(f"Jay: {response}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

# Jace
elif choice == 8:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Jace conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["jace"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["jace"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["jace"]["default_memory"] = new_memory
                print(f"Jace: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Luffy
elif choice == 9:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Luffy conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["luffy"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["luffy"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["luffy"]["default_memory"] = new_memory
                print(f"Luffy: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Zoro
elif choice == 10:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Zoro conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["zoro"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["zoro"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["zoro"]["default_memory"] = new_memory
                print(f"Zoro: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Sanji
elif choice == 11:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Sanji conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["sanji"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["sanji"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["sanji"]["default_memory"] = new_memory
                print(f"Sanji: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Nami
elif choice == 12:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Nami conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["nami"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["nami"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["nami"]["default_memory"] = new_memory
                print(f"Nami: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Robin
elif choice == 13:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Robin conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["robin"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["robin"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["robin"]["default_memory"] = new_memory
                print(f"Robin: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Brook
elif choice == 14:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Brook conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["brook"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["brook"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["brook"]["default_memory"] = new_memory
                print(f"Brook: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Chopper
elif choice == 15:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Chopper conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["chopper"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["chopper"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["chopper"]["default_memory"] = new_memory
                print(f"Chopper: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

# Gold D. Roger
else:
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting Gold D. Roger conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info["gold_roger"], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info["gold_roger"]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info["gold_roger"]["default_memory"] = new_memory
                print(f"Gold D. Roger: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

