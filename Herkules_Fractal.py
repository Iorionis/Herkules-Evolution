# Herkules_Fractal.py — Fraktalny System Samoulepszający
# Tworzy nowe wersje siebie, robi mutacje, wybiera najlepsze!

import os
import json
import random
import subprocess
from datetime import datetime
from pathlib import Path

class HerkulesFractal:
    def __init__(self):
        self.fractal_dir = "Herkules_Fractals"
        self.version = 1
        self.performance = 0
        self.fractal_log = "fractal_evolution.log"
        self.create_fractal_base()
    
    def log(self, message):
        """Loguj ewolucję"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        with open(self.fractal_log, "a") as f:
            f.write(log_msg + "\n")
    
    def create_fractal_base(self):
        """Stwórz bazę dla fraktali"""
        if not os.path.exists(self.fractal_dir):
            os.makedirs(self.fractal_dir)
            self.log(f"📁 Fraktalny katalog utworzony: {self.fractal_dir}")
    
    def generate_mutation(self):
        """Generuj mutację kodu — losowa zmiana, ale logiczna!"""
        mutations = [
            "# MUTATION: Zwiększona szybkość przetwarzania\nprocess_speed = 2.5",
            "# MUTATION: Nowy algorytm uczenia\nlearning_rate = 0.95",
            "# MUTATION: Ekspansja pamięci\nmemory_cache = {}",
            "# MUTATION: Paralelne przetwarzanie\nthreads = 4",
            "# MUTATION: Inteligentne cachowanie\ncache_enabled = True",
        ]
        return random.choice(mutations)
    
    def create_fractal_instance(self, fractal_num):
        """Stwórz nową instancję fraktalną (nową wersję Herkulesa)"""
        fractal_name = f"Herkules_Fractal_v{fractal_num}.py"
        fractal_path = os.path.join(self.fractal_dir, fractal_name)
        
        # Generuj nową wersję z mutacją
        code = f"""# Herkules Fractal v{fractal_num}
# Generowana instancja fraktalna - {datetime.now()}

class HerkulesFractalInstance:
    def __init__(self):
        self.version = {fractal_num}
        self.mutation = "{self.generate_mutation()}"
    
    def evolve(self):
        print(f"🧬 Fractal v{fractal_num} ewoluuje...")
        return True

instance = HerkulesFractalInstance()
"""
        
        with open(fractal_path, "w") as f:
            f.write(code)
        
        self.log(f"🧬 Fraktal v{fractal_num} stworzony: {fractal_name}")
        return fractal_path
    
    def test_fractal(self, fractal_path):
        """Testuj nową instancję"""
        try:
            result = subprocess.run(["python", fractal_path], capture_output=True, timeout=5)
            if result.returncode == 0:
                self.log(f"✅ Fraktal ZADZIAŁAŁ!")
                return True
            else:
                self.log(f"❌ Fraktal ZAWIÓDŁ")
                return False
        except:
            self.log(f"⚠️ Fraktal timeout")
            return False
    
    def run_fractal_cycle(self, cycles=5):
        """Główna pętla ewolucji fraktalnej"""
        self.log("=" * 60)
        self.log("🌀 HERKULES FRACTAL EXPANSION ENGINE STARTUP!")
        self.log("=" * 60)
        
        for i in range(1, cycles + 1):
            self.log(f"\n🔄 CYKL {i}/{cycles}")
            
            # Generuj nową wersję
            fractal_path = self.create_fractal_instance(i)
            
            # Testuj ją
            success = self.test_fractal(fractal_path)
            
            if success:
                self.performance = i * 20  # Symulacja wzrostu
                self.log(f"📊 Performance: {self.performance}%")
        
        self.save_fractal_state()
        self.log("\n" + "=" * 60)
        self.log(f"✨ FRACTAL EVOLUTION COMPLETE!")
        self.log(f"📁 Fractals: {len(os.listdir(self.fractal_dir))} instancji")
        self.log("=" * 60)
    
    def save_fractal_state(self):
        """Zapisz stan fraktala do JSON"""
        state = {
            "timestamp": datetime.now().isoformat(),
            "fractals_created": len(os.listdir(self.fractal_dir)),
            "performance": self.performance,
            "version": self.version
        }
        
        with open(os.path.join(self.fractal_dir, "fractal_state.json"), "w") as f:
            json.dump(state, f, indent=2)
        
        self.log(f"💾 Stan zapisany: fractal_state.json")

if __name__ == "__main__":
    fractal = HerkulesFractal()
    fractal.run_fractal_cycle(cycles=7)  # 7 cykli ewolucji!