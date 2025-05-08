import random as r

"""
tilex, tiley = Pozice hráče
inventory = Seznam itemů v inventáři hráče
objdata = Data všech itemů ve hře
hp = Hráčoův počet hp
maxhp = Hráčův maximální počet hp
enemyhp = Počet hp monstra
damage = Kolik hp má být ubráno
curweapon = Zbraň kterou mommentálně používá hráč

TODO:
 - Better Inventory
 - Chests with loot
 - Weapon switching
 - Nerf UMG Hammer
"""

#Nastavení

def isspace(border):
   space = 0
   try:
      if dungeon[tilex + 1][tiley] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex - 1][tiley] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex][tiley + 1] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex][tiley - 1] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex + 1][tiley + 1] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex - 1][tiley  - 1] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex - 1][tiley + 1] == " ":
         space += 1
   except IndexError:
      pass
   try:
      if dungeon[tilex + 1][tiley - 1] == " ":
         space += 1
   except IndexError:
      pass
   if space >= border:
      return True
   elif space < border:
      return False

inventory = [
   "Sword"
   ]

objdata = {
   #weapon: (objtype, mindamage, maxdamage)
   #s/wexplosive: (objdata, damage, radius, timer)
   "Sword": ("weapon", 1, 4),
   "Fist": ("weapon", 0, 1),
   "Ultra Mega God Hammer": ("weapon", 50, 1200),
   "Dynamite": ("wexplosive", 3, 1, 2)
}

curweapon = "Sword"

dungeon = []

size = r.randint(6, 10)

for x in range(size):
   templist = []
   for y in range(size):
      templist.append("#")
   dungeon.append(templist)
   del templist

dungeonsize = 0
for x in dungeon:
   dungeonsize += len(x)

#Generace Mapy

tile = 0

for tile in range(int(dungeonsize / 2)):
   try:
      tilex = r.randint(0, len(dungeon) - 1)
      tiley = r.randint(0, len(dungeon[tilex]))
      if dungeon[tilex][tiley] == "#":
         dungeon[tilex][tiley] = " "
   except IndexError:
      pass

tile = 0

def generate(char, gen, space):
   while True:
      tilex = r.randint(0, len(dungeon) - 1)
      tiley = r.randint(0, tilex)
      if dungeon[tilex][tiley] == char and isspace(space) == True:
         dungeon[tilex][tiley] = gen
         break

generate("#", "E", 2)

generate(" ", "@", 1)

generate("#", "S", 2)

for x in dungeon:
   for y in x:
      print(y,end = " ")
   print()

#Hráč (tilex, tiley)

print("Ahoj dobrodruhu, vítej v kobce!")
print("Blíže neurčeným způsobem ses omylem dostal do kobky, a nemůžeš ven! Jediný způsob, jak utéct je najít východ.")
print("Háček je v to, že v kobce se nacházejí monstra a tajné průchody, které musiš zdolat, chceš-li se dostat ven.")
print("Hodně štěstí!")
print()
print("Ovládání: \ninv - Otevřít inventář \nd, u, r, l - Pohyb \nur, ul, dr, dl - Diagonální pohyb \nattack - Zaútočit (pouze v boji)")

while True:
   cmd = input(" ->")

   #Pohyb

   if cmd == "d":
      try:
         if dungeon[tilex + 1][tiley] != "#":
            tilex += 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   elif cmd == "u":
      try:
         if dungeon[tilex - 1][tiley] != "#":
            tilex -= 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   elif cmd == "r":
      try:
         if dungeon[tilex][tiley + 1] != "#":
            tiley += 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   elif cmd == "l":
      try:
         if dungeon[tilex][tiley - 1] != "#":
            tiley -= 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   #Diagonální pohyb

   elif cmd == "ur":
      try:
         if dungeon[tilex - 1][tiley + 1] != "#":
            tilex -= 1
            tiley += 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   elif cmd == "ul":
      try:
         if dungeon[tilex - 1][tiley - 1] != "#":
            tilex -= 1
            tiley -= 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   elif cmd == "dr":
      try:
         if dungeon[tilex + 1][tiley + 1] != "#":
            tilex += 1
            tiley += 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   elif cmd == "dl":
      try:
         if dungeon[tilex + 1][tiley - 1] != "#":
            tilex += 1
            tiley -= 1
            print("Úspěšně ses přesunul.")
         else:
            print("Tam je zeď!")
      except IndexError:
         print("Tam je zeď!")

   #Inventory

   elif cmd == "inv":
      print("Inventář:")
      if len(inventory) == 0:
         print("Nic tu není")
         continue
      for item in inventory:
         print(f" -{item}")
      print("Který předmět?")
      cmd = input(" ->")

      if cmd not in inventory:
         print("To tam není!")
         continue
      else:
         print("Co s ním uděláš?")

   #Easter egg :)

   elif cmd == "godmode":
      inventory.append("Ultra Mega God Hammer")
      curweapon = "Ultra Mega God Hammer"
   else:
      print("Neznámý příkaz!")

   #Boj

   if dungeon[tilex][tiley] == "@":
      print('Vstoupil jsi na území monstra!')
      enemyhp = 20
      while "@" in dungeon[tilex][tiley]:
         cmd = input("Bojuj!->")
         if cmd == "attack":
            damage = r.randint(objdata[curweapon][1], objdata[curweapon][2])
            print(f"Ubral jsi monstru {damage} životů!")
            enemyhp -= damage
         if enemyhp <= 0:
            print("Zabil jsi monstrum!")
            dungeon[tilex][tiley] = " "

   #Zapínání konce

   if dungeon[tilex][tiley] == "E":
      print("Chceš z kobky odejít? (ano/ne)")
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
