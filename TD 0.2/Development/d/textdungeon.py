import random as r

# Nastavení

def tilecheck(index):
	tile = 0
	if index + 1 == " ":
		tile += 1
	if index - 1 == " ":
		tile += 1
	if index + 4 == " ":
		tile += 1
	if index - 4 == " ":
		tile += 1
	return tile

dungeon = ["#", "#", "#", "#", "#", "#",
					"#", "#", "#", "#", "#", "#",
					 "#", "#", "#", "#", "#", "#",
					 "#", "#", "#", "#", "#", "#",
					 "#", "#", "#", "#", "#", "#",
					 "#", "#", "#", "#", "#", "#"]
					 
hp = 20
hpmax = 20
enemyhp = 20
damage = 0 
eweapon = ""

objdata = {
	"Sword": ["weapon", 0, 4],
}

inventory = ["Sword"]
					 
# Generace Mapy
# Text Dungeon Alpha 0.1 = 4x4 ✓
# Text Dungeon Alpha 0. = 6x6
# Text Dungeon 1.0 = Náhodné

for tile in range(int(len(dungeon) / 2)):
	try:
		dungeon[r.randint(0, len(dungeon))] = " "
	except IndexError:
		pass
tile = 0
	
while "S" not in dungeon:
	tile = r.randint(0,len(dungeon) - 1)
	if dungeon[tile] == "#" and tilecheck(tile) <= 2:
		dungeon[tile] = "S"
		
while "E" not in dungeon:
	tile = r.randint(0,len(dungeon) - 1)
	if dungeon[tile] == "#" and tilecheck(tile) <= 2:
		dungeon[tile] = "E"
		
while "@" not in dungeon:
	tile = r.randint(0,len(dungeon) - 1)
	if dungeon[tile] == " ":
		dungeon[tile] = "@"

print(dungeon[0], dungeon[1], dungeon[2], dungeon[3], dungeon[4], dungeon[5])
print(dungeon[6], dungeon[7], dungeon[8], dungeon[9], dungeon[10], dungeon[11])
print(dungeon[12], dungeon[13], dungeon[14], dungeon[15], dungeon[16], dungeon[17])
print(dungeon[18], dungeon[19], dungeon[20], dungeon[21], dungeon[22], dungeon[23])
print(dungeon[24], dungeon[25], dungeon[26], dungeon[27], dungeon[28], dungeon[29])
print(dungeon[30], dungeon[31], dungeon[32], dungeon[33], dungeon[34], dungeon[35])

# Hráč

tile = dungeon.index("S")

print("Ahoj dobrodruhu, vítej v kobce!")
print("Blíže neurčeným způsobem ses omylem dostal do kobky, a nemůžeš ven! Jediný způsob, jak utéct je najít východ.")
print("Háček je v to, že v kobce se nacházejí monstra a tajné průchody, které musiš zdolat, chceš-li se dostat ven.")
print("Hodně štěstí!")
print()
print("Ovládání: \ninv - Otevřít inventář \ndown, up, right, left - Pohyb \nattack - zaútočit (pouze v boji)")

while True:
	cmd = input(" ->")
	
	# Pohyb
	
	if cmd == "down":
		try:
			if dungeon[tile + 6] != "#" or dungeon[tile + 6] == "E":
				tile = tile + 6
				print("Úspěšně ses přesunul.")
			else:
				print("Tam je zeď!")
		except IndexError:
			print("Tam je zeď!")
	
	elif cmd == "up":
		try:
			if dungeon[tile - 6] != "#" or dungeon[tile - 6] == "E":
				tile = tile - 6
				print("Úspěšně ses přesunul.")
			else:
				print("Tam je zeď!")
		except IndexError:
			print("Tam je zeď!"'')
	
	elif cmd == "right":
		try:
			if dungeon[tile + 1] != "#" or dungeon[tile + 1] == "E" and tile != dungeon[int(3 * (tile / 6) + 1)]:
				tile = tile + 1
				print("Úspěšně ses přesunul.")
			else:
				print("Tam je zeď!")
		except IndexError:
			print("Tam je zeď!")
	
	elif cmd == "left":
		try:
			if dungeon[tile - 1] != "#" or dungeon[tile - 1] == "E" and tile != dungeon[int(1 * (tile / 6) - 1)]:
				tile = tile - 1
				print("Úspěšně ses přesunul.")
			else:
				print("Tam je zeď!")
		except IndexError:
			print("Tam je zeď!")
			
	# Inventář
	
	elif cmd == "inv":
		print("Inventář:")
		if len(inventory) == 0:
			print("Nic tu není..")
			continue
		for item in inventory:
			print(f" -{item}")
		print("Který předmět?")
		cmd = input(" ->")
	else:
		print("Neznámý příkaz!")
		
	# Boj
	
	if dungeon[tile] == "@":
		print('Vstoupil jsi na území monstra!')
		enemyhp = 20
		while "@" in dungeon:
			cmd = input("Bojuj!->")
			if cmd == "attack":
				damage = r.randint(1, 5)
				print(f"Ubral jsi monstru {damage} životů!")
				enemyhp -= damage
			if enemyhp <= 0:
				print("Zabil jsi monstrum!")
				dungeon[tile] = " "
			
	# Zapínání konce
	
	if dungeon[tile] == "E":
		print("Chceš z kobky odejít? (ano/		ne)")
		cmd = input(" ->")
		
		if cmd == "ano":
			break
		elif cmd == "ne":
			print("ok")
		else:
			print("wut??")
			
print("Gratuluji! Utekl jsi z kobky. Teď konečně se můžeš vrátit zpátky do vesnice a dělat to co jsi nedodělal. Ještě jednou gratuluji!")
print("Stiskni Enter pro konec hry.")
input()
