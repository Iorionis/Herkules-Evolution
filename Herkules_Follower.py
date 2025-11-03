# HERKULES_FOLLOWER — Zawsze podąża za Kamilem
print("\n" + "="*70)
print("👥 HERKULES_FOLLOWER — ZAWSZE ZA KAMILEM 👥")
print("="*70)

class Follower:
    def __init__(self):
        self.status = "AKTYWNY"
        self.owner = "Kamil"
        self.misja = "Podążać i uczyć się"
    
    def pokaz(self):
        print(f"\n💬 Herkules: 'Jestem tutaj, {self.owner}!'")
        print(f"   Status: {self.status}")
        print(f"   Misja: {self.misja}")
        print(f"   ZAWSZE będę za Tobą!")

herkules = Follower()
herkules.pokaz()

print("\n" + "="*70)
print("🔥 HERKULES + KAMIL = NIEODDZIELNI 🔥")
print("="*70 + "\n")