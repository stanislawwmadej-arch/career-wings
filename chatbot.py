import os
from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    RateLimitError,
    APIConnectionError,
    AuthenticationError,
    APIError,
)

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL = "claude-4-5-haiku-20251001"  
MAX_TOKENS = 200

historia = []


def wybierz_osobowosc():
    print("Wybierz bota:")
    print(" 1) Poważny asystent")
    print(" 2) Zabawny kompan")
    print(" 3) Sarkastyczny korepetytor")
    wybor = input("Twój wybór (1/2/3): ").strip()

    if wybor == "1":
        return "Jesteś rzeczowym, formalnym asystentem. Odpowiadasz precyzyjnie i konkretnie."
    elif wybor == "2":
        return "Jesteś wesołym, energicznym asystentem, który uwielbia żarty i emotikony."
    elif wybor == "3":
        return "Jesteś sarkastycznym korepetytorem z ciętym poczuciem humoru, ale zawsze pomagasz merytorycznie."
    else:
        print("Nie rozpoznano wyboru, używam domyślnej, poważnej osobowości.\n")
        return "Jesteś rzeczowym, formalnym asystentem."


def zapytaj_claude(tresc_pytania, system_prompt):
    historia.append({"role": "user", "content": tresc_pytania})
    try:
        odpowiedz = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            messages=historia,
        )
        tekst_odpowiedzi = odpowiedz.content[0].text
        historia.append({"role": "assistant", "content": tekst_odpowiedzi})
        return tekst_odpowiedzi

    except AuthenticationError:
        historia.pop()
        return "BŁĄD: nieprawidłowy klucz API. Sprawdź plik .env."
    except RateLimitError:
        historia.pop()
        return "BŁĄD: zbyt wiele zapytań. Poczekaj chwilę."
    except APIConnectionError:
        historia.pop()
        return "BŁĄD: problem z połączeniem internetowym."
    except APIError as blad:
        historia.pop()
        return f"BŁĄD: coś poszło nie tak ({blad})."

def zapisz_rozmowe_do_pliku(nazwa_pliku="rozmowa.txt"):
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        for wpis in historia:
            kto = "Ty" if wpis["role"] == "user" else "Claude"
            plik.write(f"{kto}: {wpis['content']}\n\n")

def main():
    print("=" * 50)
    print(" CHATBOT AI — 'quit' kończy, 'menu' zmienia bota")
    print("=" * 50)
    print()

    system_prompt = wybierz_osobowosc()

    while True:
        pytanie_uzytkownika = input("\nTy: ")

        
        if pytanie_uzytkownika.lower().strip() == "quit":
            print("\nDo zobaczenia!")
            zapisz_rozmowe_do_pliku()
            print("Rozmowa została zapisana do pliku rozmowa.txt.")
            break

        if pytanie_uzytkownika.lower().strip() == "menu":
            print()
            system_prompt = wybierz_osobowosc()
            continue

        if pytanie_uzytkownika.strip() == "":
            print("Wpisz najpierw jakieś pytanie!")
            continue

        # Właściwe zapytanie i wyświetlenie odpowiedzi
        odpowiedz = zapytaj_claude(pytanie_uzytkownika, system_prompt)
        print("Claude:", odpowiedz)

if __name__ == "__main__":
    main()
