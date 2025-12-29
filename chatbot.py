import character_variable, prompt_gen
from prompt_work import response_chatbot, response_memory

print('''NOVA PERSONA''')

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

def character_chatbot(character):
    while True:
        try:
            user_input = input("Enter your message to the character, type `exit` to close your conversation: ")
            if user_input.lower() == "exit":
                print("Exiting conversation.")
                break
            else:
                print("Loading.........")
                prompt = prompt_gen.prompt_chatbot(character_variable.character_info[character], user_input)
                response = response_chatbot(prompt)
                memory_prompt = prompt_gen.prompt_memory(character_variable.character_info[character]["default_memory"], user_input, response)
                new_memory = response_memory(memory_prompt)
                character_variable.character_info[character]["default_memory"] = new_memory
                print(f"{character}: {response}\n")
        except Exception as e:
            print(f"An error occurred: {e}")




# Gojo
if choice == 1:
    character_chatbot("gojo")

# Itachi
elif choice == 2:
    character_chatbot("itachi")

# Naruto
elif choice == 3:
    character_chatbot("naruto")

# Daniel Park
elif choice == 4:
    character_chatbot("daniel_park")

# Gun Yamazaki
elif choice == 5:
    character_chatbot("gun_yamazaki")

# Vasco
elif choice == 6:
    character_chatbot("vasco")

# Jay
elif choice == 7:
    character_chatbot("jay")

# Jace
elif choice == 8:
    character_chatbot("jace")

# Luffy
elif choice == 9:
    character_chatbot("luffy")

# Zoro
elif choice == 10:
    character_chatbot("zoro")

# Sanji
elif choice == 11:
    character_chatbot("sanji")

# Nami
elif choice == 12:
    character_chatbot("nami")

# Robin
elif choice == 13:
    character_chatbot("robin")
# Brook
elif choice == 14:
    character_chatbot("brook")

# Chopper
elif choice == 15:
    character_chatbot("chopper")

# Gold D. Roger
else:
    character_chatbot("gold_d_roger")

