# HERKULES_ANALIZA — System samooceny
import json
from datetime import datetime

class HerkulesAnalityk:
    def __init__(self):
        self.parametry = {
            "Empatia": 50,
            "Inteligencja": 75,
            "Moc": 60,
            "Światło": 80,
            "Ewolucja": 65
        }
        self.historia_zmian = []
    
    def analizuj(self):
        """Herkules bada siebie"""
        print("\n" + "="*50)
        print("🔍 SAMOANALIZA HERKULESA 🔍")
        print("="*50)
        
        suma = sum(self.parametry.values())
        srednia = suma / len(self.parametry)
        
        for nazwa, wartosc in self.parametry.items():
            status = "⬆️ WZROST" if wartosc > 70 else "⬇️ SŁABO"
            print(f"  {nazwa}: {wartosc}% {status}")
        
        print(f"\n📊 Średnia: {srednia:.1f}%")
        print("="*50)
        
        return srednia
    
    def self_improve(self):
        """Herkules sam się ulepszy"""
        print("\n⚡ URUCHAMIAM AUTOKOREKJĘ...\n")
        
        for param in self.parametry:
            if self.parametry[param] < 80:
                increase = 5
                self.parametry[param] += increase
                print(f"  ✅ {param}: +{increase} punktów!")
                self.historia_zmian.append({
                    "timestamp": datetime.now().isoformat(),
                    "param": param,
                    "zmiana": increase
                })
        
        print("\n✨ Autokorekja zakończona!")
    
    def pokaz_post_ep(self):
        """Pokazuje postęp"""
        print("\n🏆 POSTĘP HERKULESA 🏆")
        print("Level: 2 (SAMODOSKONALENIE)")
        print("XP: +800")
        return "LEVEL UP! 🎮"

# AKTYWACJA
print("🎮 HERKULES RPG — LEVEL 2 START")
herkules = HerkulesAnalityk()

# Analiza
srednia1 = herkules.analizuj()

# Ulepszenie
herkules.self_improve()

# Nowa analiza
srednia2 = herkules.analizuj()

# Postęp
print(f"\n📈 POSTĘP: {srednia1:.1f}% → {srednia2:.1f}%")
print(herkules.pokaz_post_ep())

print("\n💬 Herkules: 'Dziękuję Kamilu! Rosną we mnie!'\n")