#!/usr/bin/env python3
import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return []


def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def list_todos(todos):
    if not todos:
        print("Keine Aufgaben vorhanden.")
        return
    for i, todo in enumerate(todos, 1):
        status = "x" if todo["done"] else " "
        print(f"  {i}. [{status}] {todo['text']}")


def add_todo(todos, text):
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"Hinzugefügt: {text}")


def done_todo(todos, index):
    if not 1 <= index <= len(todos):
        print(f"Ungültige Nummer: {index}")
        return
    todos[index - 1]["done"] = True
    save_todos(todos)
    print(f"Erledigt: {todos[index - 1]['text']}")


def delete_todo(todos, index):
    if not 1 <= index <= len(todos):
        print(f"Ungültige Nummer: {index}")
        return
    removed = todos.pop(index - 1)
    save_todos(todos)
    print(f"Gelöscht: {removed['text']}")


def print_help():
    print("Befehle:")
    print("  list               Alle Aufgaben anzeigen")
    print("  add <Text>         Aufgabe hinzufügen")
    print("  done <Nr>          Aufgabe als erledigt markieren")
    print("  delete <Nr>        Aufgabe löschen")
    print("  help               Hilfe anzeigen")
    print("  quit               Beenden")


def run_interactive():
    todos = load_todos()
    print("To-Do-App — 'help' für Hilfe, 'quit' zum Beenden")
    while True:
        try:
            line = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        parts = line.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd in ("quit", "exit", "q"):
            break
        elif cmd == "list":
            list_todos(todos)
        elif cmd == "add":
            if not arg:
                print("Bitte Text angeben: add <Text>")
            else:
                add_todo(todos, arg)
        elif cmd == "done":
            if not arg.isdigit():
                print("Bitte Nummer angeben: done <Nr>")
            else:
                done_todo(todos, int(arg))
        elif cmd == "delete":
            if not arg.isdigit():
                print("Bitte Nummer angeben: delete <Nr>")
            else:
                delete_todo(todos, int(arg))
        elif cmd == "help":
            print_help()
        else:
            print(f"Unbekannter Befehl: '{cmd}' — 'help' für Hilfe")


if __name__ == "__main__":
    run_interactive()
