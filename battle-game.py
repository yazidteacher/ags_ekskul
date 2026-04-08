import random
import time

# 1. DATABASE KARAKTER (Dibuat manual satu-satu biar jelas)
k0 = {"nama": "Knight", "hp": 120, "s1": "Pedang", "d1": 20, "s2": "Perisai", "d2": 5}
k1 = {"nama": "Penyihir", "hp": 80, "s1": "Api", "d1": 35, "s2": "Petir", "d2": 40}
k2 = {"nama": "Pemanah", "hp": 100, "s1": "Panah", "d1": 25, "s2": "Tusuk", "d2": 15}
k3 = {"nama": "Robot", "hp": 150, "s1": "Laser", "d1": 15, "s2": "Roket", "d2": 25}
k4 = {"nama": "Ninja", "hp": 90, "s1": "Kunai", "d1": 20, "s2": "Katana", "d2": 30}

# Masukkan ke dalam list agar bisa dipilih pakai angka
semua_karakter = [k0, k1, k2, k3, k4]

# 2. TAMPILKAN DAFTAR (Manual Print agar Rapi)
print("=== PILIH KARAKTERMU ===")
print(f"1. {k0['nama']} (HP: {k0['hp']}) -> Senjata: {k0['s1']}, {k0['s2']}")
print(f"2. {k1['nama']} (HP: {k1['hp']}) -> Senjata: {k1['s1']}, {k1['s2']}")
print(f"3. {k2['nama']} (HP: {k2['hp']}) -> Senjata: {k2['s1']}, {k2['s2']}")
print(f"4. {k3['nama']} (HP: {k3['hp']}) -> Senjata: {k3['s1']}, {k3['s2']}")
print(f"5. {k4['nama']} (HP: {k4['hp']}) -> Senjata: {k4['s1']}, {k4['s2']}")

# 3. PROSES PILIH
n_p = int(input("\nMasukkan nomor karakter KAMU: ")) - 1
n_m = int(input("Masukkan nomor karakter MUSUH: ")) - 1

# Ambil data dari list (Gunakan .copy() agar darah aslinya tidak rusak)
player = semua_karakter[n_p].copy()
enemy = semua_karakter[n_m].copy()

print(f"\n🔥 BATTLE: {player['nama']} VS {enemy['nama']} 🔥")


#While -> when we're not sure how many loops
#for -> when we're Sure how many loops

#condition = if player or enemy not 0
while player['hp'] > 0 and enemy['hp'] > 0 :
    print(f"\n\n--=-- HP of {player['nama']} :: {player['hp']} || HP of {enemy['nama']} :: {enemy['hp']} --=--")

    # Pilih Senjata Player
    print(f"Pilih Senjata {player['nama']}:")
    print(f"1. {player['s1']} (Dmg: {player['d1']})")
    print(f"2. {player['s2']} (Dmg: {player['d2']})")

    pilihan = input("Mau pakai weapon 1 atau 2? ")

    #check the aamt of damage
    if pilihan == "1":
        dmg = player['d1']
    else:
        dmg = player['d2']

    #reduce enemy blood
    enemy['hp'] = enemy['hp'] - dmg

    #the enemy strikes back

    print("\n --> The enemy is about to attack\n")
    time.sleep(2)

    enemy_weapon = random.randint(1,2)
    
    if enemy_weapon == 1:
        e_w = enemy['s1']
        e_dmg = enemy['d1']
    else:
        e_w = enemy['s2']
        e_dmg = enemy['d2']

    #reduce player's blood
    player['hp'] = player['hp'] - e_dmg

    print(f"The {enemy['nama']} attack the player using ''{e_w}''")
    print(f"The {player['nama']}'s HP is reduced by << {e_dmg} >>")

    time.sleep(1.5)

    #critical hit

    #if tie
    if player["hp"] == enemy["hp"]:
        print(f"\n ⚠️ A TIE Has been matched \nBe Carefull on your next Move !!!....")
        time.sleep(1.5)
    
    #critical
    if player['hp'] < enemy["hp"]:
        print(f"\n\n‼️ Critical ‼️ \nYour HP is lower than your Enemy! \nKeep fighting untill ypur last Breath KING!!!")
        time.sleep(2)


    #who's winning 
    if player["hp"] <= 0:
        time.sleep(1.5)
        print(f"\n\noopss... You Lose")
        print(" ☠️ Game Over ☠️\n\n")
    elif enemy['hp'] <= 0:
        time.sleep(1.5)
        print("\n\n 🌟 ... Congratulation ... 🌟")
        print("🎉 You Win, 🎉\nThe Enemy Has been defeated\n\n")




    