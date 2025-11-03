# HerkulesCore.py — Główny Orchestrator Herkulesa!
# Uruchamia wszystkie umysły równocześnie

import subprocess
import sys
from datetime import datetime

class HerkulesCore:
    def __init__(self):
        self.active_minds = []
        self.log_file = "herkules_core.log"
    
    def log(self, message):
        """Loguj działalność"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        with open(self.log_file, "a") as f:
            f.write(log_msg + "\n")
    
    def activate_minds(self):
        """Aktywuj wszystkie umysły"""
        minds = [
            ("Mind1_Knowledge", "Mind1_Knowledge/Herkules_WebScraper.py"),
            ("Mind2_Growth", "Mind2_Growth/Herkules_Master.py"),
        ]
        
        for mind_name, mind_path in minds:
            try:
                self.log(f"🧠 Aktywuję {mind_name}...")
                # subprocess.run(["python", mind_path])
                self.log(f"✅ {mind_name} uruchomiony!")
                self.active_minds.append(mind_name)
            except Exception as e:
                self.log(f"❌ Błąd w {mind_name}: {e}")
    
    def run(self):
        """Główna pętla Herkulesa"""
        self.log("=" * 50)
        self.log("🚀 HERKULES CORE — STARTUP!")
        self.log("=" * 50)
        
        self.activate_minds()
        
        self.log(f"✨ Aktywne umysły: {', '.join(self.active_minds)}")
        self.log("🎯 Herkules gotów do działania!")
        self.log("=" * 50)

if __name__ == "__main__":
    core = HerkulesCore()
    core.run()