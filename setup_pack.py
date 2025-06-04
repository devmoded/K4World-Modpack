import os
import shutil
from pathlib import Path

# Папки, которые нужно скопировать
FOLDERS_TO_COPY = ["mods", "config", "resourcepacks", "options.txt"]

def tl_skin_ask():
    def ask_launcher_type():
        print("\n🤔 Какой лаунчер ты используешь?")
        print("1. TLauncher*")
        print("2. Другой")
        print("* Желательно выбрать, чтобы работали скины")
        
        choice = input("Выбери [1/2]: ").strip()
        
        while choice not in ("1", "2"):
            print("Пожалуйста, введи 1 или 2.")
            choice = input("Выбери [1/2]: ").strip()
        return choice

    if ask_launcher_type() == "1":
        print("📦 Установка мода на скины (tl skin and cape)")
        FOLDERS_TO_COPY.append("tl_skin_cape_fabric.jar")
    else:
        print("❌ Был выбран другой лаунчер, tl skin and cape не будет установлен")

def copy_folder(src: Path, dest: Path):
    if not src.exists():
        print(f"[!] Папка {src} не найдена, пропускаю.")
        return
    
    for item in src.iterdir():
        s = src / item.name
        d = dest / item.name
        if s.is_dir():
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print(f"[✓] Скопировано: {src.name}")

def main():
    # Сообщение пользователю
    print("------------------------------")
    print("📦 Установщик Minecraft-сборки")
    print("------------------------------\n")
    
    print("📝 Сначала создай сборку в TLauncher (или другом лаунчере)")
    print("Требования сборки:")
    print("- Версия Minecraft: 1.20.1")
    print("- Версия Fabric: 0.16.13")
    print("- Имя сборки: Любое")
    
    input("➡️  Нажми Enter, когда сборка будет создана...")
    
    # Узнаём какой лаунчер будет использоваться
    tl_skin_ask()
    
    # Получаем путь до сборки
    target_path = Path(input("📁 Вставь путь до папки твоей сборки: ").strip().strip('"'))

    if not target_path.exists():
        print("❌ Указанный путь не существует. Проверь его внимательно.")
        return

    # Сообщение о начале копирования
    print("\n🚚 Начинаю копирование файлов...\n")

    # Само копирование файлов
    current_dir = Path(__file__).parent

    for folder in FOLDERS_TO_COPY:
        src = current_dir / folder
        dest = target_path / folder
        copy_folder(src, dest)

    # Сообщение о готовности сборки
    print("\n✅ Установка завершена. Сборка установлена.")


if __name__ == "__main__":
    main()

