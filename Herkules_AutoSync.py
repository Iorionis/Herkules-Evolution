# Herkules_AutoSync.py — Automatyczna Synchronizacja
# Monitoruje zmiany, komituje i pushuje automatycznie!

import os
import subprocess
import time
from datetime import datetime
from pathlib import Path

class HerkulesAutoSync:
    def __init__(self):
        self.repo_path = os.getcwd()
        self.watched_extensions = ['.py', '.json', '.txt', '.md']
        self.file_hashes = {}
        self.sync_log = "auto_sync.log"
    
    def log(self, message):
        """Loguj do pliku i konsoli"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        with open(self.sync_log, "a") as f:
            f.write(log_msg + "\n")
    
    def get_file_hash(self, filepath):
        """Oblicz hash pliku do porównania zmian"""
        try:
            with open(filepath, 'rb') as f:
                return hash(f.read())
        except:
            return None
    
    def monitor_changes(self):
        """Monitoruj zmiany w repo"""
        self.log("🔍 AutoSync uruchomiony!")
        
        while True:
            try:
                changed = False
                
                for file in Path(self.repo_path).rglob('*'):
                    if file.is_file() and file.suffix in self.watched_extensions:
                        file_path = str(file)
                        current_hash = self.get_file_hash(file_path)
                        
                        if file_path not in self.file_hashes or self.file_hashes[file_path] != current_hash:
                            if file_path in self.file_hashes:
                                self.log(f"📝 Zmiana wykryta: {file.name}")
                                changed = True
                            self.file_hashes[file_path] = current_hash
                
                if changed:
                    self.auto_commit_push()
                
                time.sleep(30)  # Sprawdzaj co 30 sekund
            
            except Exception as e:
                self.log(f"❌ Błąd: {e}")
                time.sleep(60)
    
    def auto_commit_push(self):
        """Automatycznie commituj i pushuj zmiany"""
        try:
            self.log("⚡ AutoSync: git add .")
            os.system("git add .")
            
            self.log("⚡ AutoSync: git commit...")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            os.system(f'git commit -m "🤖 AutoSync: {timestamp}"')
            
            self.log("⚡ AutoSync: git push...")
            os.system("git push")
            
            self.log("✅ AutoSync: Push OK!")
        except Exception as e:
            self.log(f"❌ AutoSync push error: {e}")

if __name__ == "__main__":
    syncer = HerkulesAutoSync()
    syncer.monitor_changes()